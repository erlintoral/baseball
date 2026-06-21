# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: SupplyList
def delete_item(item_id: int, item_type: str) -> bool:
    if not isinstance(item_type, str):
        raise ValueError("item_type должен быть строкой")
    
    try:
        index = None
        if item_type == "supplier":
            for i, s in enumerate(suppliers):
                if s["id"] == item_id:
                    index = i
                    break
        elif item_type == "product":
            for i, p in enumerate(products):
                if p["id"] == item_id:
                    index = i
                    break
        elif item_type == "purchase_order":
            for i, po in enumerate(purchase_orders):
                if po["id"] == item_id:
                    index = i
                    break
        else:
            raise ValueError(f"Неизвестный тип записи: {item_type}")

        if index is None:
            print(f"Запись с id={item_id} и типом={item_type} не найдена.")
            return False
        
        deleted_item = items[item_type].pop(index)
        print(f"Успешно удалена запись: {deleted_item['name']} (id={item_id})")
        
        if item_type == "supplier":
            for p in products:
                if p["supplier_id"] == item_id:
                    p["supplier_name"] = None
                    p["last_price"] = 0.0
        elif item_type == "product":
            for po in purchase_orders:
                if po["product_id"] == item_id:
                    po["status"] = "cancelled"
        
        return True
        
    except Exception as e:
        print(f"Ошибка при удалении: {e}")
        return False
