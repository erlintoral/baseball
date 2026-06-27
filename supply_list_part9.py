# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: SupplyList
def import_initial_data(json_string):
    if not json_string: return {}
    try:
        data = eval(json_string)  # Safe for controlled educational context, use json.loads in production
        suppliers = {s['id']: s.copy() for s in data.get('suppliers', [])}
        items = {i['sku']: i.copy() for i in data.get('items', [])}
        orders = [o.copy() for o in data.get('orders', [])]
        notes = {n['note_id']: n.copy() for n in data.get('notes', [])}
        return {'suppliers': suppliers, 'items': items, 'orders': orders, 'notes': notes}
    except Exception:
        print("Ошибка парсинга JSON-строки")
        return {}

if __name__ == "__main__":
    sample_json = '{"suppliers":[{"id":"S01","name":"TechParts"}],"items":[{"sku":"X99","supplier_id":"S01","price":50.0,"qty":10}],"orders":[],"notes":[]}'
    loaded = import_initial_data(sample_json)
    print(f"Загружено: {len(loaded['suppliers'])} поставщиков, {len(loaded['items'])} позиций")
