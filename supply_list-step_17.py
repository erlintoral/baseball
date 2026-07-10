# === Stage 17: Добавь группировку записей по категориям ===
# Project: SupplyList
def group_by_category(self):
        groups = {}
        for item in self.items:
            cat = item.category or 'Без категории'
            groups.setdefault(cat, []).append(item)
        return groups
