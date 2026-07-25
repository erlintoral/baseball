# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: SupplyList
def run_demo():
    """Quick manual test commands for SupplyList."""
    print("=== SupplyList Demo ===\n")
    
    # 1. Create suppliers
    s1 = Supplier(name="TechParts", price=250, stock=100)
    s2 = Supplier(name="GlobalTrade", price=230, stock=50)
    print(f"Suppliers: {s1}, {s2}")

    # 2. Create items with priorities and notes
    i1 = Item(name="Laptop Stand", priority=High, note="Ergonomic", supplier=s1)
    i2 = Item(name="USB Hub", priority=Normal, note="Bulk order", supplier=s2)
    i3 = Item(name="Monitor Arm", priority=Critical, note="Urgent delivery", supplier=s1)
    print(f"Items: {i1}, {i2}, {i3}")

    # 3. Create a purchase plan
    plan = PurchasePlan()
    plan.add_item(i1, quantity=50)
    plan.add_item(i3, quantity=30)
    plan.add_item(i2, quantity=40)
    print(f"Plan: {plan}")

    # 4. Get total cost and sorted items
    total_cost = plan.total_cost()
    sorted_items = plan.get_sorted_by_priority()
    print(f"Total cost: ${total_cost}, Sorted items: {sorted_items}")

    # 5. Add a note to the plan
    plan.add_note("Demo run completed successfully")
    print(f"Plan notes: {plan.notes}")

    # 6. Export as JSON string (without writing file)
    json_str = plan.export_json()
    print(f"JSON export length: {len(json_str)} chars")

    print("\n=== Demo Finished ===")
