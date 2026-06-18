# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: SupplyList
class SupplyList:
    def __init__(self):
        self._items = {}
    
    def add_item(self, name: str, supplier: str, price: float, stock: int, priority: int, notes: str = "") -> None:
        key = f"{name}_{supplier}"
        if key in self._items and self._items[key]["price"] == price:
            self._items[key]["stock"] += stock
            self._items[key]["notes"] += (", " + notes) if notes else ""
        else:
            self._items[key] = {"name": name, "supplier": supplier, "price": price, "stock": stock, "priority": priority, "notes": notes}

    def get_items(self):
        return list(self._items.values())
