# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: SupplyList
def weekly_stats(suppliers, start_date=None):
    """Return dict {week: {'count': int, 'total_cost': float}} grouped by ISO week."""
    if not suppliers:
        return {}
    dates = [s.get('date') for s in suppliers if s.get('date')]
    if not dates:
        return {}
    if start_date is None:
        min_dt = min(datetime.fromisoformat(d) for d in dates)
        start_date = (min_dt.isocalendar()[1] - 1) * 7 + min_dt.weekday()
    else:
        sd = datetime.fromisoformat(start_date)
        if sd.weekday() >= 5:
            start_date = (sd.isocalendar()[1] - 1) * 7 + sd.weekday()
        else:
            start_date -= timedelta(days=sd.weekday())
    weeks = defaultdict(lambda: {'count': 0, 'total_cost': 0.0})
    for s in suppliers:
        if not s.get('date'):
            continue
        d = datetime.fromisoformat(s['date'])
        w_start = start_date + timedelta(weeks=(d - start_date).days // 7)
        iso_w = (w_start.isocalendar()[1], w_start.isocalendar()[0])
        weeks[iso_w]['count'] += 1
        weeks[iso_w]['total_cost'] += float(s.get('price', 0))
    return {f"{i}-{j}": v for i, j in sorted(weeks.keys()) if isinstance(j, int) and not isinstance(j, datetime)}
