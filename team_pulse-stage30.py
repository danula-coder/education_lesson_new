# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: TeamPulse
class UserProfile:
    def __init__(self, name, mood=None, blockers=None):
        self.name = name
        self.mood = mood or "neutral"
        self.blockers = blockers or []
    
    def update_mood(self, new_mood):
        if new_mood in ("great", "good", "ok", "bad"):
            self.mood = new_mood
    
    def add_blocker(self, blocker):
        if blocker not in self.blockers:
            self.blockers.append(blocker)
    
    def remove_blocker(self, blocker):
        if blocker in self.blockers:
            self.blockers.remove(blocker)

def register_profile(name, mood=None, blockers=None):
    return UserProfile(name, mood, blockers)
