# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: TeamPulse
def demo():
    print("=" * 60)
    print(" TeamPulse — Демонстрация командного журнала настроения и задач")
    print("=" * 60)
    print()

    # Инициализация приложения
    app = TeamPulseApp()
    app.run()
