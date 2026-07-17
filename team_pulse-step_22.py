# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: TeamPulse
def check_overdue_reminders():
    """Проверяет просроченные напоминания и выводит предупреждения."""
    overdue = []
    for entry in all_entries:
        if entry.get("type") == "reminder" and entry.get("status") != "done":
            deadline = entry.get("deadline", "")
            if deadline and datetime.now() > datetime.strptime(deadline, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc):
                overdue.append(entry)
    return overdue
