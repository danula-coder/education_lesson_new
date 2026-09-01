# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: TeamPulse
import unittest

class TestTeamPulseEdgeCases(unittest.TestCase):
    def setUp(self):
        from team_pulse import TeamPulse
        self.tp = TeamPulse("Test Team")

    def test_empty_team_raises(self):
        with self.assertRaises(ValueError):
            self.tp.add_member("Alice")

    def test_duplicate_member_raises(self):
        self.tp.add_member("Alice")
        with self.assertRaises(ValueError):
            self.tp.add_member("Alice")

    def test_invalid_mood_raises(self):
        self.tp.add_member("Alice")
        with self.assertRaises(ValueError):
            self.tp.check_in("Alice", "maybe")

    def test_invalid_task_priority_raises(self):
        self.tp.add_member("Alice")
        with self.assertRaises(ValueError):
            self.tp.add_task("Alice", "Test", "high")

    def test_invalid_task_status_raises(self):
        self.tp.add_member("Alice")
        self.tp.add_task("Alice", "Test", "high")
        with self.assertRaises(ValueError):
            self.tp.update_task_status("Test", "done")

    def test_invalid_task_assignee_raises(self):
        self.tp.add_member("Alice")
        self.tp.add_task("Alice", "Test", "high")
        with self.assertRaises(ValueError):
            self.tp.assign_task("Test", "Bob")

    def test_invalid_blocker_creator_raises(self):
        self.tp.add_member("Alice")
        with self.assertRaises(ValueError):
            self.tp.add_blocker("Alice", "Blocked", "Alice", "Bob")

    def test_invalid_blocker_priority_raises(self):
        self.tp.add_member("Alice")
        with self.assertRaises(ValueError):
            self.tp.add_blocker("Alice", "Blocked", "Alice", "Bob", "low")

    def test_invalid_blocker_status_raises(self):
        self.tp.add_member("Alice")
        self.tp.add_blocker("Alice", "Blocked", "Alice", "Bob")
        with self.assertRaises(ValueError):
            self.tp.update_blocker_status("Blocked", "Resolved")

    def test_invalid_blocker_assignee_raises(self):
        self.tp.add_member("Alice")
        self.tp.add_blocker("Alice", "Blocked", "Alice", "Bob")
        with self.assertRaises(ValueError):
            self.tp.assign_blocker("Blocked", "Alice")

    def test_invalid_weekly_summary_date_raises(self):
        self.tp.add_member("Alice")
        self.tp.add_task("Alice", "Test", "high")
        with self.assertRaises(ValueError):
            self.tp.generate_weekly_summary("2024-01-01")

    def test_invalid_weekly_summary_member_raises(self):
        self.tp.add_member("Alice")
        with self.assertRaises(ValueError):
            self.tp.generate_weekly_summary("Alice")

    def test_invalid_weekly_summary_format_raises(self):
        self.tp.add_member("Alice")
        with self.assertRaises(ValueError):
            self.tp.generate_weekly_summary("01-01-2024")


if __name__ == '__main__':
    unittest.main()
