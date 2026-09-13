# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: TeamPulse
def migrate_to_v2(data: dict) -> dict:
    """Миграция структуры данных: добавление поля 'blocked_by' в задачи.
    
    Если в задаче нет поля 'blocked_by', добавляем его со значением None.
    Также добавляем поле 'mood_history' в пользователей, если его нет.
    """
    if 'version' not in data:
        data['version'] = 'v1'
    
    if data['version'] == 'v1':
        data['version'] = 'v2'
        
        # Миграция задач: добавляем blocked_by
        if 'tasks' in data:
            for task in data['tasks']:
                if 'blocked_by' not in task:
                    task['blocked_by'] = None
        
        # Миграция пользователей: добавляем mood_history
        if 'users' in data:
            for user in data['users']:
                if 'mood_history' not in user:
                    user['mood_history'] = []
    
    return data
