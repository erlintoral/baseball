# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: SupplyList
def validate_date(date_str):
    """Validate date string in DD.MM.YYYY format, return error message or None."""
    if not date_str:
        return "Дата не может быть пустой."
    try:
        parts = date_str.split(".")
        if len(parts) != 3:
            return "Неверный формат даты. Ожидается DD.MM.YYYY."
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
            return "Некорректные значения дня, месяца или года."
    except ValueError:
        return "Неверный формат даты. Ожидается DD.MM.YYYY."
    return None

def format_error(msg, field=""):
    """Format a user-friendly error message."""
    if field:
        return f"Ошибка в поле '{field}': {msg}"
    return msg
