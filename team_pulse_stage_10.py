# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: TeamPulse
def export_state_to_json():
    import json
    from datetime import datetime
    state = {
        "project": "TeamPulse",
        "timestamp": datetime.utcnow().isoformat(),
        "team_mood": team_mood,
        "tasks": tasks_list,
        "blockers": blockers_list,
        "weekly_summary": weekly_summary
    }
    return json.dumps(state, indent=2)
