# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: TeamPulse
def generate_weekly_summary(data):
    if not data:
        return "Нет данных для сводки."
    
    mood_counts = {}
    blockers = []
    tasks_completed = 0
    
    for entry in data:
        mood = entry.get("mood", "neutral")
        mood_counts[mood] = mood_counts.get(mood, 0) + 1
        
        if entry.get("blockers"):
            blockers.extend(entry["blockers"])
        
        if entry.get("checkins"):
            tasks_completed += sum(1 for item in entry["checkins"] if item.get("done", False))
    
    total_entries = len(data)
    avg_mood_score = 0.5 # Упрощенная оценка: neutral=0.5, happy=1.0, sad=0.0
    mood_map = {"happy": 1.0, "neutral": 0.5, "sad": 0.0}
    for entry in data:
        avg_mood_score += mood_map.get(entry.get("mood", "neutral"), 0.5)
    avg_mood_score /= total_entries
    
    summary = f"Сводка за период:\n"
    summary += f"- Всего чек-инов выполнено: {tasks_completed}\n"
    summary += f"- Средний уровень настроения команды: {'😊' if avg_mood_score > 0.7 else '😐' if avg_mood_score > 0.3 else '😟'} ({avg_mood_score:.1f}/1.0)\n"
    
    if mood_counts:
        most_common_mood = max(mood_counts, key=mood_counts.get)
        summary += f"- Наиболее частое настроение: {most_common_mood}\n"
    
    if blockers:
        unique_blockers = list(set(blockers))[:5] # Берем топ 5 уникальных блокеров
        summary += f"- Уникальные блокеры (первые 5): {', '.join(unique_blockers)}\n"
    else:
        summary += "- Блокеров не зафиксировано.\n"
    
    return summary
