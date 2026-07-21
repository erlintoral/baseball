# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: SupplyList
def print_order_summary(order: Order) -> None:
    """Компактный вывод одной записи заказа."""
    supplier = order.supplier
    status = "✓" if order.is_fulfilled else "✗"
    print(f"[{order.id}] {status} | Заказ #{order.order_id}")
    print(f"  Поставщик: {supplier.name} ({supplier.location})")
    print(f"  Товар:     {order.product_name}, кол-во: {order.quantity}")
    print(f"  Цена/ед.: ${order.price:.2f} → Итого: ${order.total_price:.2f}")
    if order.priority:
        print(f"  Приоритет: {'HIGH' if order.priority == 'high' else 'MEDIUM'}")
    if order.notes:
        print(f"  Заметка:   {order.notes}")
    print()

def list_orders(orders: List[Order]) -> None:
    """Вывод списка всех заказов."""
    print("=== Список закупок ===\n")
    for i, order in enumerate(orders, start=1):
        print_order_summary(order)
