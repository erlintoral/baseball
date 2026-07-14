# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: SupplyList
def archive_records(entries, days=365):
    """Archive entries older than `days` or with quantity <= 0."""
    cutoff = time.time() - days * 86400
    archived = []
    for e in entries:
        if (e['added'] < cutoff and e.get('quantity', 0) > 0):
            continue
        archived.append(e)
    return archived

def mark_archived(entries, archived_ids=None):
    """Mark records as archived by setting status to 'archived'."""
    for e in entries:
        if e['id'] in (archived_ids or []):
            e['status'] = 'archived'
