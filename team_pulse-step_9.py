# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: TeamPulse
import json, sys

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Валидация обязательных полей
        required_keys = ["team_name", "members"]
        for key in required_keys:
            if key not in data:
                raise KeyError(f"Отсутствует ключ: {key}")
            
            if isinstance(data[key], list):
                for item in data[key]:
                    if not isinstance(item, dict):
                        raise TypeError("Элементы списка должны быть словарями")
        
        # Установка дефолтных значений для отсутствующих опциональных полей
        defaults = {
            "created_at": None,
            "settings": {"theme": "light", "notifications_enabled": True}
        }
        data.update(defaults)
        
        return data
    
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)

# Пример использования (раскомментируйте для тестирования):
if __name__ == "__main__":
    sample_json = '''
    {
        "team_name": "Alpha Squad",
        "members": [
            {"id": 1, "name": "Алексей", "role": "Frontend"},
            {"id": 2, "name": "Мария", "role": "Backend"}
        ],
        "created_at": "2023-10-01T09:00:00Z"
    }
    '''
    
    loaded_data = load_initial_data(sample_json)
    print(f"Загружена команда: {loaded_data['team_name']}")
    print(f"Членов: {len(loaded_data['members'])}")
