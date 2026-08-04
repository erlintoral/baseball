# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: SupplyList
import sys


def undo_last_action():
    """Откат последнего действия: возвращает состояние до последнего вызова."""
    global last_action, last_state
    if not last_action:
        print("Нет предыдущего действия для отката.")
        return
    # Восстанавливаем состояние из ранее сохраненного
    sys.modules['supplylist'].data = last_state.copy()
    print(f"Действие '{last_action}' отменено. Данные восстановлены.")


def save_state():
    """Сохраняет текущее состояние данных для возможного отката."""
    global last_action, last_state
    if 'supplylist' not in sys.modules:
        raise ImportError("Модуль supplylist не найден")
    import supplylist as sl
    last_state = sl.data.copy()


# Пример использования undo_last_action и save_state
last_action = None
last_state = None

def add_item(item):
    """Добавление нового элемента в список."""
    global last_action, last_state
    if 'supplylist' not in sys.modules:
        raise ImportError("Модуль supplylist не найден")
    import supplylist as sl
    # Сохраняем состояние перед добавлением
    save_state()
    sl.data.append(item)
    last_action = f"Добавлено: {item}"


def remove_item(item):
    """Удаление элемента из списка."""
    global last_action, last_state
    if 'supplylist' not in sys.modules:
        raise ImportError("Модуль supplylist не найден")
    import supplylist as sl
    # Сохраняем состояние перед удалением
    save_state()
    sl.data.remove(item)
    last_action = f"Удалено: {item}"
