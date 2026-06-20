# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: SupplyList
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if key in record_fields and records[record_id][key] != value:
            records[record_id][key] = value
            changed_count += 1
    
    print(f"Запись {record_id} обновлена. Изменено полей: {changed_count}")
    return True
