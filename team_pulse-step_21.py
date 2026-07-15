# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: TeamPulse
class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    @property
    def is_overdue(self):
        return datetime.date.today() > self.due_date

    @property
    def days_left(self):
        delta = self.due_date - datetime.date.today()
        return delta.days if delta.days >= 0 else f"-{abs(delta.days)}"


class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, title, due_date_str):
        try:
            due_date = datetime.date.fromisoformat(due_date_str)
        except ValueError as e:
            print(f"Неверный формат даты: {e}")
            return False
        if not 1 <= due_date.day <= 31 and 1 <= due_date.month <= 12:
            print("Дата выходит за пределы календаря, проверьте ввод.")
            return False
        self.reminders.append(Reminder(title, due_date))
        return True

    def show_reminders(self):
        if not self.reminders:
            print("\nНапоминаний нет.")
            return
        today = datetime.date.today()
        print(f"\n📌 Напоминания (сегодня — {today}):")
        for r in self.reminders:
            status = "⚠️ ПРОСРОЧЕНО" if r.is_overdue else f"До {r.due_date} ({r.days_left}) дней"
            print(f"  • {r.title}: {status}")


# Пример использования
reminder_manager = ReminderManager()

while True:
    title = input("\nВведите заголовок напоминания (или 'done' для завершения): ").strip().lower()
    if title == "done":
        break
    due_date = input("Дата выполнения (YYYY-MM-DD): ").strip()
    ok = reminder_manager.add_reminder(title, due_date)

reminder_manager.show_reminders()
