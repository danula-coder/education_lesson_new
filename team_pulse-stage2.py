# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: TeamPulse
class TeamPulseModel:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, mood: str, task: str, blocker: str) -> bool:
        if not all([mood in ['happy', 'neutral', 'sad'], len(task.strip()) > 0]):
            return False
        if blocker and len(blocker.strip()) < 3:
            return False
        self.entries.append({'date': datetime.now().strftime('%Y-%m-%d'), 'mood': mood, 'task': task, 'blocker': blocker or None})
        return True
    
    def get_weekly_summary(self) -> dict:
        from collections import Counter
        if not self.entries:
            return {'count': 0, 'avg_mood_score': 0}
        dates = [e['date'] for e in self.entries]
        week_start = max(dates).replace(day=1)
        week_entries = [e for e in self.entries if e['date'].startswith(week_start.strftime('%Y-%m'))]
        mood_scores = {'happy': 3, 'neutral': 2, 'sad': 1}
        total_score = sum(mood_scores[e['mood']] for e in week_entries)
        return {
            'count': len(week_entries),
            'avg_mood_score': round(total_score / len(week_entries), 2) if week_entries else 0,
            'common_blockers': Counter(e['blocker'] for e in week_entries if e['blocker']).most_common(3)
        }

from datetime import datetime
