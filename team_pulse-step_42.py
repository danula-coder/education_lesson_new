# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: TeamPulse
import sys

ANSI = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m',
    'clear': '\033[2J\033[H',
}

color_enabled = True

def enable_colors():
    global color_enabled
    color_enabled = True

def disable_colors():
    global color_enabled
    color_enabled = False

def colorize(text, code):
    if color_enabled:
        return f'{ANSI[code]}{text}{ANSI["reset"]}'
    return text

def success(text):
    return colorize(text, 'green')

def error(text):
    return colorize(text, 'red')

def warning(text):
    return colorize(text, 'yellow')

def info(text):
    return colorize(text, 'blue')

def title(text):
    return colorize(f'{ANSI["bold"]}{text}{ANSI["reset"]}', 'bold')
