# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: TeamPulse
def demo_run():
    """Демо-команды для ручного тестирования: команды, блокеры, настроения."""
    from datetime import date, timedelta
    today = date.today()
    
    # --- Команды ---
    commands_demo = [
        {"id": 1, "title": "Обсудить архитектуру API", "owner": "Алексей", "status": "done"},
        {"id": 2, "title": "Написать тесты для auth", "owner": "Мария", "status": "in_progress"},
        {"id": 3, "title": "Сделать дизайн-макет", "owner": "Дмитрий", "status": "pending"},
    ]

    # --- Блокеры ---
    blockers_demo = [
        {"id": 1, "title": "Нет доступа к CI/CD серверу", "author": "Алексей", "severity": "high"},
        {"id": 2, "title": "Задержка от дизайнера с ассетами", "author": "Мария", "severity": "medium"},
    ]

    # --- Настроения (чек-ины) ---
    moods_demo = [
        {"name": "Алексей", "mood": 4, "note": "Вдохновлен!"},
        {"name": "Мария", "mood": 3, "note": "Нормально"},
        {"name": "Дмитрий", "mood": 2, "note": "Сложный день"},
    ]

    # --- Примеры отчетов за неделю ---
    reports_demo = [
        {
            "week_start": today - timedelta(days=7),
            "week_end": today - timedelta(days=1),
            "tasks_done": 3,
            "blockers_resolved": 1,
            "avg_mood": 3.0,
        }
    ]

    print("=== Демо-данные TeamPulse ===")
    print(f"Текущая дата: {today}")
    print()

    # Вывод команд
    print("--- Команды ---")
    for c in commands_demo:
        status_emoji = {"done": "✅", "in_progress": "🔄", "pending": "⏳"}[c["status"]]
        print(f"  {status_emoji} [{c['id']}] {c['title']} — автор: {c['owner']}")

    # Вывод блокеров
    print()
    print("--- Блокеры ---")
    for b in blockers_demo:
        sev = {"high": "🔴", "medium": "🟡", "low": "🟢"}[b["severity"]]
        print(f"  {sev} [{b['id']}] {b['title']} — автор: {b['author']}")

    # Вывод настроений
    print()
    print("--- Чек-ины настроения ---")
    for m in moods_demo:
        emoji = "😊" if m["mood"] >= 4 else ("😐" if m["mood"] == 3 else "😟")
        print(f"  {emoji} {m['name']}: оценка {m['mood']} — \"{m['note']}\"")

    # Вывод отчета за неделю
    print()
    print("--- Недельная сводка ---")
    for r in reports_demo:
        print(f"  Период: {r['week_start']} → {r['week_end']}")
        print(f"  Выполнено задач: {r['tasks_done']}, Разрешено блокеров: {r['blockers_resolved']}, Среднее настроение: {r['avg_mood']}")

    print()
    print("=== Конец демо ===")
