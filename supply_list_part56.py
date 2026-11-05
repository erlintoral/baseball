# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: SupplyList
def bulk_update_selected():
    if not selected_items:
        print("Нет выбранных записей для обновления.")
        return
    print(f"Выбрано записей для обновления: {len(selected_items)}")
    print("Введите новое значение для каждого поля (нажмите Enter для сохранения без изменений):")
    supplier_input = input("Поставщик: ").strip()
    price_input = input("Цена: ").strip()
    quantity_input = input("Остаток: ").strip()
    priority_input = input("Приоритет: ").strip()
    notes_input = input("Заметка: ").strip()
    for item in selected_items:
        if supplier_input:
            item.supplier = supplier_input
        if price_input:
            try:
                item.price = float(price_input)
            except ValueError:
                print(f"Неверный формат цены для '{item.name}'.")
        if quantity_input:
            try:
                item.quantity = float(quantity_input)
            except ValueError:
                print(f"Неверный формат остатка для '{item.name}'.")
        if priority_input:
            item.priority = priority_input
        if notes_input:
            item.notes = notes_input
        print(f"Обновлено: {item.name}")
