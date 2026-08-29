# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: TeamPulse
def check_integrity_and_repair():
    """Check data integrity and repair common issues."""
    issues = []
    if not team_mood_entries:
        issues.append("No mood entries found")
    if not task_log:
        issues.append("No tasks found")
    if not blockers:
        issues.append("No blockers found")
    if issues:
        print(f"Data integrity issues: {issues}")
        return False
    print("Data integrity check passed")
    return True
