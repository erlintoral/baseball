# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: SupplyList
def show_menu():
    print("\n=== SupplyList: Меню действий ===")
    print("1. Показать список товаров с остатками")
    print("2. Добавить новый товар")
    print("3. Изменить цену или поставщика товара")
    print("4. Удалить товар из списка")
    print("5. Просмотреть заметки по конкретному товару")
    print("6. Вывести сводную статистику (итоговая стоимость)")
    print("0. Завершить работу")
    choice = input("Введите номер действия: ")
    return int(choice)

def handle_choice(choice):
    if choice == 1:
        for item in items:
            print(f"{item['name']}: Остаток={item.get('stock', 0)}, Цена={item.get('price', 0)}")
    elif choice == 2:
        name = input("Название товара: ")
        stock = int(input("Количество на складе: "))
        price = float(input("Цена за единицу: "))
        supplier = input("Поставщик: ")
        notes = input("Заметки (или Enter): ")
        items.append({"name": name, "stock": stock, "price": price, "supplier": supplier, "notes": notes})
    elif choice == 3:
        idx = int(input("Индекс товара для изменения (0-based): "))
        if 0 <= idx < len(items):
            item = items[idx]
            print(f"Текущие данные: {item['name']}, Цена={item.get('price')}, Поставщик={item.get('supplier')}")
            new_price = input("Новая цена (или Enter для пропуска): ")
            if new_price:
                item["price"] = float(new_price)
            new_supplier = input("Новый поставщик (или Enter для пропуска): ")
            if new_supplier:
                item["supplier"] = new_supplier
    elif choice == 4:
        name = input("Название товара для удаления: ")
        for i, item in enumerate(items):
            if item["name"].lower() == name.lower():
                del items[i]
                print(f"Товар '{name}' удалён.")
                break
        else:
            print(f"Товар '{name}' не найден.")
    elif choice == 5:
        name = input("Название товара для просмотра заметок: ")
        for item in items:
            if item["name"].lower() == name.lower():
                notes = item.get("notes", "Нет заметок")
                print(f"Заметки по '{name}': {notes}")
                break
        else:
            print(f"Товар '{name}' не найден.")
    elif choice == 6:
        total_value = sum(item.get("stock", 0) * item.get("price", 0) for item in items)
        print(f"Итоговая стоимость запасов: {total_value:.2f}")
    else:
        exit()

while True:
    choice = show_menu()
    if choice == 0:
        break
