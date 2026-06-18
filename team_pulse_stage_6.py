# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: TeamPulse
def filter_entries(entries, filters=None):
    if not filters: return entries
    result = []
    for e in entries:
        match_status = (not filters.get('status')) or (e['status'] == filters['status'])
        match_category = (not filters.get('category')) or (e['category'] == filters['category'])
        match_tags = True
        if 'tags' in filters and e.get('tags'):
            for tag in filters['tags']:
                if tag not in e['tags']: match_tags = False; break
        elif 'tags' in filters: match_tags = False
        if match_status and match_category and match_tags: result.append(e)
    return result
