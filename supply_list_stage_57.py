# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: SupplyList
def bulk_delete(items, keys, confirm=True):
    if not keys:
        return 0
    if confirm and len(keys) > 1:
        print(f"Удалить выбранные покупки ({len(keys)} шт.)? (y/n): ", end="")
        resp = input().strip().lower()
        if resp not in ("y", "yes"):
            return 0
    for k in keys:
        try:
            items.pop(k, None)
        except Exception as e:
            print(f"Ошибка удаления id={k}: {e}")
    return len(keys)


def bulk_delete_menu(items):
    if not items:
        print("Список покупок пуст.")
        return
    print("ID доступных покупок:")
    ids = list(items.keys())
    for i, k in enumerate(ids, 1):
        print(f"{i}. {k}")
    print("0 — отмена")
    print("Введите ID через запятую (например: 1,3,5): ", end="")
    raw = input().strip()
    if raw == "0":
        return
    try:
        keys = [int(x) for x in raw.split(",") if x.strip()]
    except ValueError:
        print("Неверный формат ввода.")
        return
    keys = [k for k in keys if k in items]
    if not keys:
        print("Ничего не выбрано.")
        return
    removed = bulk_delete(items, keys)
    if removed:
        print(f"Удалено покупок: {removed}")
        print("Оставшиеся ID покупок:")
        for k in items:
            print(k)
