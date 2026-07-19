# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: TeamPulse
def print_record(record):
    if record is None:
        return
    print(f"  Запись от {record['date']} ({record['type']})")
    print(f"    Автор: {record['author']}")
    if 'mood' in record:
        print(f"    Настроение: {record['mood'].capitalize()}")
    if 'task' in record:
        print(f"    Задача: {record['task']}")
        if 'status' in record:
            print(f"    Статус: {record['status']}")
    if 'blocker' in record:
        print(f"    Блокер: {record['blocker']}")
    if 'checkin' in record and len(record['checkin']) > 0:
        items = ', '.join(f"{c['question']}: {c['answer']}" for c in record['checkin'])
        print(f"    Чек-ин: {items}")
