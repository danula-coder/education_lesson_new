# === Stage 17: Добавь группировку записей по категориям ===
# Project: TeamPulse
def categorize_entries(entries):
    categories = {}
    for entry in entries:
        if "category" not in entry:
            continue
        cat = entry["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(entry)
    return dict(sorted(categories.items()))
