# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: TeamPulse
TEMPLATES = {
    'daily_checkin': {
        'title': 'Ежедневный чек-ин',
        'fields': [
            ('mood', 'Состояние', ['happy', 'neutral', 'stressed']),
            ('energy', 'Энергия', ['high', 'medium', 'low']),
            ('focus', 'Фокус', ['high', 'medium', 'low']),
        ]
    },
    'task_entry': {
        'title': 'Новая задача',
        'fields': [
            ('title', 'Название задачи', None),
            ('priority', 'Приоритет', ['critical', 'high', 'medium', 'low']),
            ('category', 'Категория', ['dev', 'design', 'marketing', 'other']),
            ('due_date', 'Дедлайн', None),
        ]
    },
    'blocker_entry': {
        'title': 'Блокер',
        'fields': [
            ('title', 'Описание блокера', None),
            ('severity', 'Серьезность', ['critical', 'high', 'medium']),
            ('impact', 'Влияние', ['team', 'project', 'individual']),
        ]
    },
    'weekly_summary': {
        'title': 'Недельная сводка',
        'fields': [
            ('highlights', 'Ключевые достижения', None),
            ('challenges', 'Вызовы', None),
            ('goals_next_week', 'Цели на следующую неделю', None),
        ]
    }
}
