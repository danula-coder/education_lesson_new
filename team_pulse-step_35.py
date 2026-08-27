# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: TeamPulse
def get_next_action_advice(team):
    """Generate a single-line recommendation for the team based on its current state.
    
    Looks at blockers, mood trends, and task completion rates to suggest
    what the team should focus on next week.
    """
    if not team:
        return "Start by creating the first team with some members and a project."
    
    active_blockers = sum(1 for m in team if any(b.status == "active" for b in m.blockers))
    avg_mood = sum(m.mood_score for m in team) / len(team) if team else 0
    completed_tasks = sum(1 for t in team if t.status == "done")
    total_tasks = sum(len(t.tasks) for t in team)
    completion_rate = completed_tasks / total_tasks if total_tasks else 0

    if active_blockers > len(team) * 0.5:
        return f"Clear blockers first — {active_blockers} active blockers are slowing progress."
    if avg_mood < 3:
        return "Team mood is low — consider a team check-in or morale activity."
    if completion_rate < 0.3:
        return "Low task completion — prioritize breaking down tasks into smaller pieces."
    if not team[0].tasks:
        return "Add some tasks to get started — define goals for this week."
    return "Everything looks good — keep up the momentum and set next week's targets."
