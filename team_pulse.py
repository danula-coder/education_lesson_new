# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: TeamPulse
import json
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = "teampulse_data.json"

def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "team_members": ["Алексей", "Мария", "Дмитрий"],
            "tasks": [],
            "mood_logs": [],
            "blockers": []
        }

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_task(description, assignee=None, priority="medium"):
    data = load_data()
    task = {
        "id": len(data["tasks"]) + 1,
        "description": description,
        "assignee": assignee or "Не назначен",
        "priority": priority,
        "status": "open",
        "created_at": datetime.now().isoformat()
    }
    data["tasks"].append(task)
    save_data(data)
    return task

def log_mood(member_name, mood_level, comment=""):
    data = load_data()
    entry = {
        "member": member_name,
        "level": mood_level,
        "comment": comment,
        "timestamp": datetime.now().isoformat()
    }
    data["mood_logs"].append(entry)
    save_data(data)
    return entry

def add_blocker(issue, impact="medium"):
    data = load_data()
    blocker = {
        "id": len(data["blockers"]) + 1,
        "issue": issue,
        "impact": impact,
        "reported_at": datetime.now().isoformat()
    }
    data["blockers"].append(blocker)
    save_data(data)
    return blocker

# Инициализация и демо-заполнение при первом запуске
if not Path(DATA_FILE).exists():
    print("Инициализация базы данных TeamPulse...")
    add_task("Настроить CI/CD пайплайн", "Алексей", "high")
    add_task("Протестировать API эндпоинты", "Мария", "medium")
    log_mood("Алексей", 4, "Сложная задача по миграции")
    log_mood("Мария", 5, "Всё идёт по плану")
    add_blocker("Отсутствие тестовых данных в продакшене", "high")
    print("Демо-данные добавлены успешно.")
