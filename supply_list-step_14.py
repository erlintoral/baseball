# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: SupplyList
def generate_summary():
    if not suppliers: return print("Данные пусты.")
    total_items = sum(len(items) for items in supplier_data.values())
    low_stock = [(name, item['sku'], item['qty']) 
                  for name, data in supplier_data.items() 
                  for item in data.get('items', []) if item['qty'] < 10]
    print(f"Поставщиков: {len(suppliers)}, Товаров всего: {total_items}")
    if low_stock:
        print("Низкие остатки (<10):")
        for name, sku, qty in low_stock[:5]:
            print(f"  - {name}: {sku} ({qty})")
    else:
        print("Критических остатков нет.")
