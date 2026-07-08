# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: TeamPulse
class Tag:
    def __init__(self, name):
        self.name = name.lower().strip()

    @property
    def display(self):
        return self.name.capitalize() if self.name else "(пустой)"


def add_tag(entries):
    """Add a new tag to the entry and mark it as 'new'."""
    tag_name = input("Введите название тега: ").strip()
    if not tag_name:
        print("Ошибка: тег не может быть пустым.")
        return None, False

    # check for duplicates
    existing = [t.name for t in entries]
    if tag_name.lower() in existing:
        print(f"Тег '{tag_name}' уже существует.")
        return None, False

    new_tag = Tag(tag_name)
    entries.append(new_tag)
    print(f"✅ Тег добавлен: {new_tag.display}")
    return new_tag, True


def delete_tag(entries):
    """Remove an existing tag and update all entry references."""
    if not entries:
        print("Нет тегов для удаления.")
        return None, False

    for i, t in enumerate(entries):
        print(f"  {i + 1}. {t.display} ({len([e.tags for e in _get_all_entries(t)])}))")
    
    choice = input("Выберите номер тега для удаления (или 'q' чтобы выйти): ").strip()
    if choice.lower() == 'q':
        return None, False

    try:
        idx = int(choice) - 1
    except ValueError:
        print("Неверный ввод.")
        return None, False

    if idx < 0 or idx >= len(entries):
        print("Такого тега нет.")
        return None, False

    removed = entries.pop(idx)
    print(f"🗑️ Тег удалён: {removed.display}")
    return removed, True


def _get_all_entries(tag):
    """Return all Entry objects that reference the given Tag."""
    from team_pulse import Entry  # local import to keep file self-contained
    out = []
    for e in Entry._entries:
        if tag.name in [t.name for t in e.tags]:
            out.append(e)
    return out
