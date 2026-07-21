# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: TeamPulse
def parse_date(date_str):
    """Parse date string in format YYYY-MM-DD or DD.MM.YYYY, return datetime.date object."""
    try:
        for fmt in ("%Y-%m-%d", "%d.%m.%y"):
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        raise ValueError(f"Неверный формат даты: '{date_str}'")
    except (ValueError, TypeError) as e:
        if isinstance(e, ValueError):
            return None
        else:
            raise

def format_date(dt):
    """Format date object to YYYY-MM-DD string."""
    try:
        return dt.strftime("%Y-%m-%d")
    except AttributeError:
        return str(dt)
