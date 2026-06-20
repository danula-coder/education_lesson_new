# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: TeamPulse
def sort_entries(entries, key='date'):
    reverse = False if key == 'name' else True
    def get_sort_key(item):
        try: return item['date'] if key == 'date' else (item.get('priority', 0) * -1) if key == 'priority' else item['title'].lower()
        except TypeError: return ''
    return sorted(entries, key=get_sort_key, reverse=reverse)
