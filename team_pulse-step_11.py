# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: TeamPulse
import json, os

DATA_FILE = "teampulse_data.json"

def save_state(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"[Ошибка сохранения] {e}")
