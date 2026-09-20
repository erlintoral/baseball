# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: SupplyList
class ChangeLog:
    """Журнал изменений данных с отметками времени."""

    def __init__(self):
        self._entries = []

    def log(self, action: str, target: str, detail: str = ""):
        self._entries.append({
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "target": target,
            "detail": detail,
        })

    def get_entries(self) -> list:
        return list(self._entries)

    def clear(self):
        self._entries.clear()
