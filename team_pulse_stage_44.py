# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: TeamPulse
def backup_data_file(filepath, backup_dir="."):
    """Создает резервную копию файла данных с автоматическим переименованием."""
    if not os.path.exists(filepath):
        return None
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(filepath)}.bak_{timestamp}")
    try:
        with open(filepath, 'r', encoding='utf-8') as src:
            content = src.read()
        with open(backup_path, 'w', encoding='utf-8') as dst:
            dst.write(content)
        return backup_path
    except Exception as e:
        print(f"Ошибка резервного копирования: {e}")
        return None
