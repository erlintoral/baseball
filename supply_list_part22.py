# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: SupplyList
def check_overdue_reminders():
    today = datetime.date.today()
    overdue = []
    for item in items:
        if item.reminder_date and item.reminder_date < today:
            overdue.append({
                "item": item,
                "days_overdue": (today - item.reminder_date).days,
                "supplier": item.supplier.name if item.supplier else None,
            })
    return overdue

def print_overdue_summary():
    overdue = check_overdue_reminders()
    if not overdue:
        print("✅ Все напоминания актуальны.")
        return
    print(f"⚠️ Просрочено напоминаний: {len(overdue)}")
    for entry in overdue[:10]:  # показываем первые 10, остальные — сводка
        item = entry["item"]
        supplier_info = f", поставщик: {entry['supplier']}" if entry["supplier"] else ""
        print(f"   - {item.name} ({item.quantity} шт.){supplier_info} просрочено на {entry['days_overdue']} дн.")
    if len(overdue) > 10:
        print(f"   ... и ещё {len(overdue) - 10} позиций")
