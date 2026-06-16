# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: TeamPulse
def delete_entry(entry_id: int) -> bool:
    """Удаление записи по ID с проверкой на существование."""
    if entry_id not in entries_db:
        print(f"Ошибка: запись с ID {entry_id} не найдена.")
        return False
    
    del entries_db[entry_id]
    print(f"Запись с ID {entry_id} успешно удалена.")
    return True

def handle_missing_ids():
    """Обработка отсутствующих идентификаторов при чтении/записи."""
    missing = []
    for key, value in list(entries_db.items()):
        if not isinstance(key, int):
            print(f"Предупреждение: некорректный тип ключа {key}, игнорируется.")
            continue
        # Логика обработки пустых значений или других аномалий может быть добавлена здесь
    return missing
