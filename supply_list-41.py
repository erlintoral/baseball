# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: SupplyList
def dry_run(operation, *args):
    """Simulate an operation without applying it; return a dry-run result dict."""
    from datetime import datetime
    now = datetime.now().isoformat()
    return {
        "mode": "dry-run",
        "operation": operation,
        "args": args,
        "timestamp": now,
        "status": "simulated",
    }
