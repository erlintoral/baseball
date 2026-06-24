# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: SupplyList
def sort_records(records, key='date'):
    priority_map = {'high': 1, 'medium': 2, 'low': 3}
    def get_sort_key(r):
        p_val = priority_map.get(r['priority'].lower(), 9) if r.get('priority') else 9
        d_val = r.get(key, '').split('-')[0] or ''
        n_val = r.get('name', '')
        return (p_val, int(d_val), n_val.lower())
    return sorted(records, key=get_sort_key)
