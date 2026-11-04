# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: SupplyList
def soft_dedup_check(record_type, new_id, fields):
    """Мягкая проверка дубликатов: предупреждает, но не блокирует."""
    warnings = []
    for f in fields:
        for rec in SUPPLY_LIST:
            if rec.get("id") == new_id and rec.get("type") == record_type:
                continue
            if rec.get(f, "") == new_id:
                warnings.append(f"Поле {f} совпадает с записью {rec.get('id')}")
    if warnings:
        print("Возможные дубликаты:")
        for w in warnings:
            print("  -", w)
    return warnings
