# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: SupplyList
class Item:
    def __init__(self, name: str, supplier: str, price: float, quantity: int, priority: int = 1, notes: str = "") -> None:
        self.name = name.strip() or "Нет названия"
        self.supplier = supplier.strip() or "Неизвестный поставщик"
        if price < 0: raise ValueError("Цена не может быть отрицательной")
        self.price = round(price, 2)
        if quantity < 0: raise ValueError("Количество не может быть отрицательным")
        self.quantity = max(0, int(quantity))
        if priority < 1 or priority > 5: raise ValueError("Приоритет должен быть от 1 до 5")
        self.priority = priority
        self.notes = notes.strip()

    def to_dict(self) -> dict:
        return {"name": self.name, "supplier": self.suppliers, "price": self.price, "quantity": self.quantity, "priority": self.priority, "notes": self.notes}
