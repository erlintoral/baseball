# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: SupplyList
def print_summary(items, suppliers):
    if not items:
        return None
    total_cost = sum(i['price'] * i.get('qty', 0) for i in items)
    in_stock = [i for i in items if i.get('rest') and i['rest'] >= (i.get('qty', 0))]
    out_of_stock = [i for i in items if not i.get('rest') or i['rest'] < (i.get('qty', 0))]
    avg_price = sum(i['price'] * i.get('qty', 1) for i in items) / sum(i.get('qty', 1) for i in items) if any(i.get('qty', 0) > 0 for i in items) else 0
    print(f"Total cost: {total_cost}, In stock: {len(in_stock)}, Out of stock: {len(out_of_stock)}, Avg price per unit: {avg_price:.2f}")
