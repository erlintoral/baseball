# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: SupplyList
def migrate_data(old_data):
    if old_data is None:
        return {
            "items": [],
            "suppliers": [],
            "priorities": [],
            "notes": [],
            "version": 1
        }
    return {
        "items": old_data.get("items", []),
        "suppliers": old_data.get("suppliers", []),
        "priorities": old_data.get("priorities", []),
        "notes": old_data.get("notes", []),
        "version": old_data.get("version", 1)
    }
