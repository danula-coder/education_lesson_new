# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: TeamPulse
def read_team_pulse_file():
    path = "team_puzzle.py"
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def write_team_pulse_file(content):
    path = "team_puzzle.py"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
