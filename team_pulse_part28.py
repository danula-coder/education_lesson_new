# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: TeamPulse
def compute_project_metrics(entries):
    """Returns a dict with key project stats."""
    total = len(entries) or 1
    mood_counts = {}
    blocker_count = 0
    checked_in = 0
    for e in entries:
        if 'mood' in e:
            m = e['mood'].strip().lower()
            mood_counts[m] = mood_counts.get(m, 0) + 1
        if e.get('status') == 'checked-in':
            checked_in += 1
        if e.get('type') == 'blocker':
            blocker_count += 1

    avg_mood_score = 5.0
    for m in ('great', 'good'):
        avg_mood_score -= mood_counts.get(m, 0) / total * 2
    for m in ('bad', 'terrible'):
        avg_mood_score -= mood_counts.get(m, 0) / total * 3

    return {
        'total_entries': total,
        'mood_distribution': mood_counts,
        'average_mood_score': round(avg_mood_score, 2),
        'checked_in_count': checked_in,
        'blocker_count': blocker_count,
        'engagement_rate': round(checked_in / total * 100, 1) if total else 0,
    }
