# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: SupplyList
def monthly_stats(records, start_date=None):
    """Group records by month and return a dict: {month_key: [records]}."""
    if not records:
        return {}
    months = []
    for r in records:
        date_str = r.get("date") or str(r)
        try:
            dt = datetime.fromisoformat(date_str)
            month_key = (dt.year, dt.month)
            if start_date:
                sd = datetime.fromisoformat(start_date).replace(day=1)
                if (dt.year, dt.month) < (sd.year, sd.month):
                    continue
        except Exception:
            month_key = r.get("date") or "Unknown"
        months.append(month_key)
    grouped = {}
    for m in months:
        grouped.setdefault(m, []).append(r)
    return grouped
