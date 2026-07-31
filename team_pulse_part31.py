# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: TeamPulse
def toggle_active_profile(self):
        """Переключить активный профиль: пользователь выбирает из списка, а текущий становится 'inactive'."""
        if not self.profiles:
            print("Нет сохранённых профилей.")
            return
        name = input(f"Введите имя нового активного профиля (или '{self.active_profile_name}' для отмены): ").strip()
        if not name or name == self.active_profile_name:
            return
        for prof in self.profiles.values():
            if prof["name"] == name:
                if prof["active"]:
                    print("Этот профиль уже активен.")
                    return
                old = self.active_profile_name
                prof["active"] = True
                self.active_profile_name = name
                print(f"Профиль '{old}' → неактивен. Новый активный: '{name}'.")
                return
        else:
            print("Профиль с таким именем не найден.")
