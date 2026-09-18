# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: TeamPulse
def format_weekly_report(team_data, week_start, week_end):
    """Генерирует финальную текстовую сводку за неделю для команды."""
    lines = []
    lines.append("=" * 50)
    lines.append(f"📊 ЕЖЕНЕДЕЛЬНАЯ СВОДКА: {week_start} — {week_end}")
    lines.append("=" * 50)

    total_tasks = sum(len(team['tasks']) for team in team_data.values())
    total_checkins = sum(len(team['checkins']) for team in team_data.values())
    total_blockers = sum(len(team['blockers']) for team in team_data.values())
    total_mood = sum(team['mood'] for team in team_data.values())
    avg_mood = total_mood / len(team_data) if team_data else 0

    lines.append(f"💼 Всего задач: {total_tasks}")
    lines.append(f"✅ Чек-ины: {total_checkins}")
    lines.append(f"🚧 Блокеры: {total_blockers}")
    lines.append(f"😊 Среднее настроение: {avg_mood:.1f}/10")

    for team_name, team in team_data.items():
        active = [t for t in team['tasks'] if t['status'] != 'done']
        lines.append(f"  • {team_name}: {len(active)} активных задач из {len(team['tasks'])}")
        if team['blockers']:
            blocker_texts = [b['text'] for b in team['blockers']]
            lines.append(f"    Блокеры: {', '.join(blocker_texts)}")

    lines.append("=" * 50)
    return "\n".join(lines)
