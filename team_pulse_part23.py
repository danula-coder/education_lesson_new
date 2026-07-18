# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: TeamPulse
def print_table(headers, rows):
    """Compact console table: given column headers and list of row dicts."""
    if not headers or not rows:
        return
    col_w = [len(str(h)) for h in headers]
    for r in rows:
        vals = []
        for i, h in enumerate(headers):
            v = str(r.get(i, ''))
            col_w[i] = max(col_w[i], len(v))
        print('  '.join(v.ljust(col_w[i]) for i, v in enumerate(vals)))
    print('-' * sum(col_w) + '+')

print_table(['Модуль', 'Статус', 'Прогресс'], [
    {'Модуль': 'Файл', 'Статус': 'Сборка', 'Прогресс': '70%'},
    {'Модуль': 'API',   'Статус': 'Работа',  'Прогресс': '45%'},
])
