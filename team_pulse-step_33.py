# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: TeamPulse
def undo_last_action():
    """Откат последнего действия: удаляет последнюю запись из истории, если она не пустая."""
    if not _history:
        print("Нет действий для отката.")
        return None
    
    last_entry = _history.pop()
    if last_entry["action"] == "checkin":
        user = last_entry["user"]
        if user in users:
            del users[user]
            print(f"Отменен чек-ин пользователя {user}.")
    elif last_entry["action"] == "blocker":
        blocker_id = last_entry["id"]
        if blocker_id in blockers:
            del blockers[blocker_id]
            print(f"Отменен блокер #{blocker_id}.")
    elif last_entry["action"] == "task":
        task_id = last_entry["id"]
        if task_id in tasks:
            del tasks[task_id]
            print(f"Отменена задача #{task_id}.")
    
    return last_entry
