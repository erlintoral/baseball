# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: SupplyList
import json, datetime

def export_report(suppliers, orders, notes):
    report = []
    report.append(f"SupplyList Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    report.append(f"{'='*50}\n")
    for s in suppliers:
        report.append(f"Supplier: {s['name']}")
        report.append(f"  Balance: {s['balance']}")
        report.append(f"  Min: {s['min_balance']}")
        report.append(f"  Max: {s['max_balance']}")
        report.append(f"  Priority: {s['priority']}")
        report.append(f"  Price: {s['price']}")
        report.append(f"  Notes: {s['notes']}\n")
    for o in orders:
        report.append(f"Order: {o['item']}")
        report.append(f"  Supplier: {o['supplier']}")
        report.append(f"  Quantity: {o['quantity']}")
        report.append(f"  Price: {o['price']}")
        report.append(f"  Total: {o['quantity'] * o['price']}\n")
    report.append(f"{'='*50}\n")
    report.append(f"Notes:\n")
    for n in notes:
        report.append(f"  {n}\n")
    return "\n".join(report)
