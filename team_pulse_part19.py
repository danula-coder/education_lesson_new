# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: TeamPulse
def archive_older_records(records, cutoff_days=30):
    """Archive records older than cutoff_days into a separate list."""
    import datetime
    cutoff = datetime.date.today() - datetime.timedelta(days=cutoff_days)
    active, archived = [], []
    for rec in records:
        if rec['date'] < cutoff or rec.get('status') == 'done':
            archived.append(rec)
        else:
            active.append(rec)
    return active, archived
