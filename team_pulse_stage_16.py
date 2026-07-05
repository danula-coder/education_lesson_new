# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: TeamPulse
def calculate_monthly_stats(entries):
    from datetime import date, timedelta
    
    stats = {}
    today = date.today()
    
    for entry in entries:
        try:
            d = date.fromisoformat(entry['date'])
            if (d.year == today.year and d.month == today.month) or \
               (today.day <= 15 and d.year < today.year):
                key = f"{d.year}-{d.month:02}"
                stats[key] = stats.get(key, {'tasks': 0, 'mood_sum': 0, 'blockers': []})
                
                if entry['task']: stats[key]['tasks'] += 1
                if entry['mood']: stats[key]['mood_sum'] += entry['mood']
                if entry['blocker']: stats[key]['blockers'].append(entry['blocker'])
        except ValueError:
            continue
            
    return {k: v for k, v in sorted(stats.items())}
