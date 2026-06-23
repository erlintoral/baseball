# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: SupplyList
def filter_items(status=None, category=None, tags=None):
    filtered = []
    for item in items:
        if status and item.get('status') != status: continue
        if category and item.get('category') != category: continue
        if tags is not None:
            item_tags = set(item.get('tags', []))
            if not any(tag in item_tags for tag in tags): continue
        filtered.append(item)
    return filtered

def search_items(query=None, status=None, category=None, tags=None):
    results = filter_items(status=status, category=category, tags=tags)
    if query:
        q_lower = query.lower()
        results = [r for r in results if any(q_lower in str(v).lower() for v in r.values())]
    return results

def get_stats_by_status():
    counts = {}
    for item in items:
        s = item.get('status', 'unknown')
        counts[s] = counts.get(s, 0) + 1
    return counts
