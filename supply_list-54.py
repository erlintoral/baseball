# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: SupplyList
class Favorites:
    def __init__(self, db):
        self.db = db
        self._table = db.table('favorites')
        if not self._table.exists():
            self._table.create('id INTEGER PRIMARY KEY AUTOINCREMENT, record_id INTEGER NOT NULL UNIQUE, created_at TEXT DEFAULT (datetime(\'now\'))')

    def toggle(self, record_id):
        fav = self._table.where('record_id = ?', (record_id,)).first()
        if fav:
            self._table.delete(fav)
            return False
        self._table.insert({'record_id': record_id})
        return True

    def is_favorited(self, record_id):
        return self._table.where('record_id = ?', (record_id,)).first() is not None

    def get_favorites(self):
        return self._table.select_all()
