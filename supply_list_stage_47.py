# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: SupplyList
def demo():
    """Показывает основной пользовательский сценарий SupplyList."""
    print("=== SupplyList Demo ===\n")

    # Создаём несколько поставщиков с ценами и остатками
    suppliers = [
        {"name": "TechCorp", "price": 150.0, "stock": 100, "priority": "High", "notes": "Надёжный поставщик электроники"},
        {"name": "GlobalParts", "price": 120.0, "stock": 200, "priority": "Medium", "notes": "Лучшие цены на детали"},
        {"name": "FastShip", "price": 180.0, "stock": 50, "priority": "High", "notes": "Быстрая доставка, но дорого"},
    ]

    # Добавляем позиции в список закупок
    items = [
        {"item": "Ноутбук Pro", "quantity": 5, "supplier": "TechCorp", "notes": "Для офиса"},
        {"item": "Монитор 24\"", "quantity": 3, "supplier": "GlobalParts", "notes": "Для дизайнеров"},
        {"item": "Клавиатура", "quantity": 10, "supplier": "TechCorp", "notes": "Механическая"},
        {"item": "Мышь беспроводная", "quantity": 8, "supplier": "FastShip", "notes": "Для тестирования"},
    ]

    # Показываем общий статус
    print("📦 Поставщики:")
    for s in suppliers:
        print(f"  • {s['name']}: ${s['price']}/шт, {s['stock']} шт, приоритет: {s['priority']}")

    print(f"\n🛒 Список закупок: {len(items)} позиций")
    for i in items:
        print(f"  • {i['item']}: {i['quantity']} шт от {i['supplier']}")

    # Считаем общую стоимость
    total_cost = sum(i['quantity'] * next(s['price'] for s in suppliers if s['name'] == i['supplier']) for i in items)
    print(f"\n💰 Общая стоимость: ${total_cost:.2f}")

    # Сортировка по приоритету
    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    sorted_items = sorted(items, key=lambda x: priority_order.get(x['supplier'].split(' ')[0], 3))
    print(f"\n📋 Покупки по приоритету:")
    for i in sorted_items:
        print(f"  • {i['item']}: {i['quantity']} шт от {i['supplier']}")

    print("\n✅ Demo завершен успешно!")
    return items, suppliers
