# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: TeamPulse
def show_main_menu():
    print("\n=== TeamPulse: Командный журнал ===")
    print("1. Добавить чек-ин (настроение + задачи)")
    print("2. Записать блокеры команды")
    print("3. Просмотреть недельную сводку")
    print("4. Выход из программы")
    try:
        choice = input("Выберите действие [1-4]: ").strip()
        return int(choice) if choice.isdigit() else None
    except ValueError:
        return None

def handle_choice_menu():
    while True:
        option = show_main_menu()
        if option == 1:
            add_checkin()
        elif option == 2:
            log_blockers()
        elif option == 3:
            print_weekly_summary()
        elif option == 4:
            print("До встречи в TeamPulse!")
            break
