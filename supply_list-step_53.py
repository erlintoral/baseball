# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: SupplyList
def parse_orders(text):
    orders = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split('|')
        if len(parts) != 6:
            continue
        orders.append({
            'supplier': parts[0].strip(),
            'product': parts[1].strip(),
            'price': float(parts[2].strip()),
            'qty': int(parts[3].strip()),
            'priority': int(parts[4].strip()),
            'note': parts[5].strip(),
        })
    return orders
