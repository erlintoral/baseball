# === Stage 20: Добавь восстановление записей из архива ===
# Project: SupplyList
def restore_from_archive(archive_path):
    """Восстанавливает записи из архива."""
    import json
    with open(archive_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, dict) and '_meta' in data:
        meta = data['_meta']
        records = [r for r in data.values() if not isinstance(r, (dict, list)) or 'id' in r]
        return records if records else []
    elif isinstance(data, list):
        return data
    else:
        raise ValueError("Неизвестный формат архива")
