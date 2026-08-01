# === Stage 32: Добавь журнал действий пользователя ===
# Project: TeamPulse
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user, action_type, description, timestamp=None):
        if timestamp is None:
            from datetime import datetime
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        entry = {
            'user': user,
            'action': action_type,
            'description': description,
            'time': timestamp
        }
        self.entries.append(entry)

    def get_log(self):
        return self.entries.copy()

    def clear(self):
        self.entries.clear()

# Пример использования
log = ActionLog()
log.log("Алекс", "чек-ин", "Работаю над модулем задач")
log.log("Мария", "блокер", "Нет доступа к CI/CD")
print(f"Записей в журнале: {len(log.get_log())}")
