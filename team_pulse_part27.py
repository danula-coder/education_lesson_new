# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: TeamPulse
def reset_demo_data():
    """Сбросить все данные к дефолтным."""
    global task_log, mood_log, blocker_log, weekly_summary
    
    default_tasks = [
        {"id": 1, "title": "Приветствие в команде", "status": "completed"},
        {"id": 2, "title": "Настройка окружения", "status": "in_progress"},
        {"id": 3, "title": "Создать задачу", "status": "todo"},
    ]
    
    default_moods = [
        {"day": 1, "score": 7},
        {"day": 2, "score": 8},
        {"day": 3, "score": 6},
        {"day": 4, "score": 9},
        {"day": 5, "score": 7},
    ]
    
    default_blockers = [
        {"id": 1, "description": "Нет Wi-Fi", "resolved": False}
    ]
    
    task_log = default_tasks
    mood_log = default_moods
    blocker_log = default_blockers
    weekly_summary = None
    
    print("✅ Демо-данные сброшены")

def clear_state():
    """Полная очистка всех данных."""
    global task_log, mood_log, blocker_log, weekly_summary
    
    task_log.clear()
    mood_log.clear()
    blocker_log.clear()
    weekly_summary = None
    
    print("🗑️ Все данные очищены")

reset_demo_data()
clear_state()
