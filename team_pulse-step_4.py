# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: TeamPulse
def edit_entry(entry_id: int, new_data: dict) -> bool:
    if not isinstance(new_data, dict):
        raise ValueError("new_data must be a dictionary")
    
    for i, entry in enumerate(entries):
        if entry['id'] == entry_id:
            entries[i] = {**entry, **new_data}
            print(f"Запись #{entry_id} обновлена.")
            return True
    
    print(f"Запись с ID {entry_id} не найдена.")
    return False
