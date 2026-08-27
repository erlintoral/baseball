# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: SupplyList
def check_integrity():
    issues = []
    for item in items:
        if item["price"] <= 0:
            issues.append(f"Item {item['name']}: price must be positive")
        if item["qty"] < 0:
            issues.append(f"Item {item['name']}: qty must be non-negative")
        if item["priority"] not in (0, 1, 2, 3):
            issues.append(f"Item {item['name']}: priority must be 0-3")
    for order in orders:
        if order["qty"] <= 0:
            issues.append(f"Order {order['item_name']}: qty must be positive")
        if order["price"] <= 0:
            issues.append(f"Order {order['item_name']}: price must be positive")
    for supplier in suppliers:
        if supplier["price"] <= 0:
            issues.append(f"Supplier {supplier['name']}: price must be positive")
    for note in notes:
        if note["text"] == "":
            issues.append("Note has empty text")
    if issues:
        print("Integrity issues found:")
        for i in issues:
            print(f"  - {i}")
        return False
    print("Data integrity check passed.")
    return True

def repair_data():
    for item in items:
        item["price"] = max(item["price"], 0.01)
        item["qty"] = max(item["qty"], 0)
        item["priority"] = max(0, min(3, item["priority"]))
    for order in orders:
        order["qty"] = max(order["qty"], 1)
        order["price"] = max(order["price"], 0.01)
    for supplier in suppliers:
        supplier["price"] = max(supplier["price"], 0.01)
    for note in notes:
        note["text"] = " "
    print("Data repaired successfully.")
    return True
