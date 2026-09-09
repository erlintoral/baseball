# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: SupplyList
import shutil, os, json

def backup_data_file(db_path):
    if not os.path.exists(db_path):
        return None
    backup_dir = os.path.join(os.path.dirname(db_path), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    base = os.path.basename(db_path)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{base}.{stamp}.bak")
    shutil.copy2(db_path, backup_path)
    return backup_path
