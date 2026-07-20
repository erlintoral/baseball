# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: SupplyList
def print_supply_table(suppliers: list[dict], max_width=60):
    """Выводит компактную таблицу поставщиков."""
    headers = ["ID", "Название", "Цена", "Остаток", "Приоритет"]
    widths = [len(h) for h in headers]
    rows = []
    for s in suppliers:
        row = [str(s.get("id","")), str(s.get("name",""))[:max_width-2],
               f"{s.get('price',0):.1f}", f"{s.get('stock',0)}", str(s.get("priority",""))]
        rows.append(row)
    for i, h in enumerate(headers):
        widths[i] = max(widths[i], len(h))
    for r in rows:
        for i, v in enumerate(r):
            widths[i] = max(widths[i], min(len(v), 20))

    lines = ["+" + "+".join("-"*w for w in widths) + "+"]
    lines.append("| " + " | ".join(h.center(w).replace("\n"," ") for h,w in zip(headers,widths)) + " |")
    lines.append("|" + "+" + "+".join("-"*w for w in widths) + "|")
    for r in rows:
        line = "|" + " | ".join(v.ljust(min(len(v),20)).replace("\n"," ") for v in r) + " |"
        lines.append(line)
    lines.append("|" + "+" + "+".join("-"*w for w in widths) + "|")
    print("\n".join(lines))
