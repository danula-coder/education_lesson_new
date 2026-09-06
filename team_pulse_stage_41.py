# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: TeamPulse
def dry_run(self, action: str, target: dict, **kwargs):
        """Simulate a mutating operation and return a preview dict without side effects.
        Supports: add_task, complete_task, add_blocker, add_mood, add_checkin,
        add_weekly_summary."""
        preview = {"action": action, "target": target, "dry_run": True}
        preview.update(kwargs)
        if action == "add_task":
            preview["status"] = "pending"
        elif action == "complete_task":
            preview["status"] = "completed"
        elif action == "add_blocker":
            preview["resolved"] = False
        elif action == "add_mood":
            preview["mood"] = kwargs.get("mood", "neutral")
        elif action == "add_checkin":
            preview["mood"] = kwargs.get("mood", "neutral")
        elif action == "add_weekly_summary":
            preview["week"] = kwargs.get("week", "pending")
        return preview
