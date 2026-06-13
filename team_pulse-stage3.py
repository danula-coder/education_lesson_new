# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: TeamPulse
class TeamPulse:
    def __init__(self):
        self.records = []
    
    def add_checkin(self, member_name: str, mood: int, blockers: list[str], tasks: list[str]) -> None:
        record = {
            "member": member_name,
            "mood": mood,
            "blockers": blockers,
            "tasks": tasks,
            "timestamp": datetime.now().isoformat()
        }
        self.records.append(record)

    def add_summary(self, week_start: str, week_end: str, summary_text: str) -> None:
        record = {
            "type": "summary",
            "week_range": (week_start, week_end),
            "text": summary_text,
            "timestamp": datetime.now().isoformat()
        }
        self.records.append(record)

    def get_records(self) -> list[dict]:
        return self.records.copy()
