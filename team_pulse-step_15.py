# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: TeamPulse
def calculate_weekly_stats(entries):
    from datetime import date, timedelta
    
    if not entries:
        return {}
    
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    
    weekly_data = {
        'tasks_completed': 0,
        'mood_avg': 0.0,
        'blockers_count': 0,
        'checkins_count': 0
    }
    
    for entry in entries:
        entry_date = date.fromisoformat(entry['date'])
        
        if week_start <= entry_date <= week_end:
            weekly_data['tasks_completed'] += entry.get('completed_tasks', 0)
            weekly_data['mood_avg'] += entry.get('mood_score', 0)
            weekly_data['blockers_count'] += len(entry.get('blockers', []))
            weekly_data['checkins_count'] += 1
    
    if weekly_data['checkins_count'] > 0:
        weekly_data['mood_avg'] /= weekly_data['checkins_count']
    
    return weekly_data
