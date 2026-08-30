# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: TeamPulse
import unittest
from datetime import date, timedelta

class TestTeamPulse(unittest.TestCase):
    def test_checkin_adds_entry(self):
        from team_pulse import TeamPulse
        tp = TeamPulse()
        tp.add_checkin("Анна", "Отлично", None, None)
        self.assertEqual(len(tp.entries), 1)
        self.assertEqual(tp.entries[0].author, "Анна")

    def test_add_blocker(self):
        from team_pulse import TeamPulse
        tp = TeamPulse()
        tp.add_blocker("Нет сервера", "Анна")
        self.assertEqual(len(tp.blockers), 1)

    def test_add_task(self):
        from team_pulse import TeamPulse
        tp = TeamPulse()
        tp.add_task("Доделать API", "Анна", "В процессе")
        self.assertEqual(len(tp.tasks), 1)

    def test_add_task_done(self):
        from team_pulse import TeamPulse
        tp = TeamPulse()
        tp.add_task("Доделать API", "Анна", "Готово")
        self.assertEqual(len(tp.tasks), 1)
        self.assertEqual(tp.tasks[0].status, "Готово")

    def test_add_task_cancelled(self):
        from team_pulse import TeamPulse
        tp = TeamPulse()
        tp.add_task("Доделать API", "Анна", "Отменено")
        self.assertEqual(len(tp.tasks), 1)
        self.assertEqual(tp.tasks[0].status, "Отменено")

if __name__ == "__main__":
    unittest.main()
