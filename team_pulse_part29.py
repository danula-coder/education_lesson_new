# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: TeamPulse
APP_CONFIG = {
    "app_name": "TeamPulse",
    "version": "29.0",
    "language": "ru",
    "max_entries_per_day": 10,
    "emoji_set": {"good": "👍", "neutral": "😐", "bad": "👎"},
    "weekly_summary_days": ["monday", "tuesday", "wednesday", "thursday", "friday"],
}

def get_config():
    return APP_CONFIG.copy()

config = get_config()
print(f"TeamPulse v{config['version']} | language: {config['language']}")
