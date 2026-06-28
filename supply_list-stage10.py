# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: SupplyList
def export_to_json():
    import json
    data = {
        "suppliers": suppliers,
        "orders": orders,
        "priorities": priorities,
        "notes": notes,
        "last_updated": datetime.now().isoformat()
    }
    return json.dumps(data, indent=2, ensure_ascii=False)
