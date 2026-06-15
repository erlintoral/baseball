# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: SupplyList
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

@dataclass
class Supplier:
    name: str
    contact: str
    
@dataclass 
class Item:
    name: str
    supplier: Supplier
    price: float
    stock: int
    priority: Priority
    notes: str = ""
    
def main():
    suppliers = {
        "TechCorp": Supplier("TechCorp", "+7-900-123-4567"),
        "GlobalParts": Supplier("GlobalParts", "+7-900-987-6543")
    }
    
    items = [
        Item("Laptop Stand", suppliers["TechCorp"], 1500.0, 5, Priority.HIGH, "Urgent for office"),
        Item("USB-C Cable", suppliers["GlobalParts"], 250.0, 20, Priority.MEDIUM),
    ]
    
    print(f"SupplyList initialized with {len(items)} items.")
    for item in sorted(items, key=lambda x: (x.priority.value, -x.stock)):
        print(f"[{item.priority.name}] {item.name}: Stock={item.stock}, Price={item.price} RUB")

if __name__ == "__main__":
    main()
