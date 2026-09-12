# === Stage 45: Добавь восстановление из резервной копии ===
# Project: TeamPulse
import json, os, datetime

def load_backup(filename):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_backup(data, filename):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def restore_from_backup(backup_filename, current_filename):
    backup = load_backup(backup_filename)
    if backup is None:
        print("Резервная копия не найдена.")
        return
    print(f"Восстанавливаю из {backup_filename}...")
    with open(current_filename, 'w', encoding='utf-8') as f:
        json.dump(backup, f, indent=2, ensure_ascii=False)
    print("Готово. Данные восстановлены.")
