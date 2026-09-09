# === Stage 43: Добавь пагинацию длинных списков ===
# Project: TeamPulse
def paginate(items, page_size=10):
    """Split a long list into pages of fixed size."""
    pages = []
    for i in range(0, len(items), page_size):
        pages.append(items[i:i + page_size])
    return pages

def display_page(pages, current_page_idx=0):
    """Show one page with navigation hints."""
    if not pages:
        print("Список пуст.")
        return
    page = pages[current_page_idx]
    print(f"\n--- Страница {current_page_idx + 1} из {len(pages)} ---")
    for item in page:
        print(f"  • {item}")
    print(f"  [Назад] {current_page_idx - 1} | [Вперёд] {current_page_idx + 1}")

# Пример использования
tasks = [f"Задача {i}" for i in range(1, 51)]
task_pages = paginate(tasks, 10)
display_page(task_pages, 0)
