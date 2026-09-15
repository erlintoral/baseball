# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: SupplyList
def _split_line(line):
    """Parse a CSV-style line into (key, value) pair, handling quoted values."""
    if line.startswith('"') and line.endswith('"'):
        line = line[1:-1]
    idx = line.find(':')
    if idx == -1:
        raise ValueError(f"Invalid line format: {line}")
    return line[:idx].strip(), line[idx + 1:].strip()


def _format_value(v):
    """Format a value for display: numbers stay numbers, others become strings."""
    if isinstance(v, (int, float)):
        return v
    return str(v)


def format_order(order):
    """Return a human-readable string for a single order."""
    parts = []
    parts.append(f"Order #{order['id']}")
    parts.append(f"  Supplier: {order['supplier']['name']}")
    parts.append(f"  Item: {order['item']}")
    parts.append(f"  Price: {_format_value(order['price'])}")
    parts.append(f"  Priority: {order['priority']}")
    parts.append(f"  Notes: {order.get('notes', '')}")
    parts.append(f"  Qty: {order['qty']}")
    parts.append(f"  Status: {order['status']}")
    return "\n".join(parts)


def format_summary(suppliers, orders, items):
    """Return a compact summary of the entire supply list."""
    lines = ["=== SupplyList Summary ===", f"Items: {len(items)}", f"Suppliers: {len(suppliers)}", f"Orders: {len(orders)}"]
    for order in orders:
        lines.append(format_order(order))
    return "\n".join(lines)
