# === Stage 45: Добавь восстановление из резервной копии ===
# Project: SupplyList
def restore_from_backup(backup_path):
    """Восстановление данных из резервной копии."""
    if not backup_path or not os.path.exists(backup_path):
        print(f"Резервная копия не найдена: {backup_path}")
        return
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Ошибка чтения резервной копии: {e}")
        return
    if not isinstance(data, dict):
        print("Неверный формат резервной копии")
        return
    try:
        supply_list.clear()
        supply_list.add_suppliers(data.get('suppliers', []))
        supply_list.add_products(data.get('products', []))
        supply_list.add_plans(data.get('plans', []))
        supply_list.add_notes(data.get('notes', []))
        print(f"Восстановлено: {len(data.get('suppliers', []))} поставщиков, "
              f"{len(data.get('products', []))} продуктов, "
              f"{len(data.get('plans', []))} планов, "
              f"{len(data.get('notes', []))} заметок")
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
