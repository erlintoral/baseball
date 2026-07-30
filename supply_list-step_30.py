# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: SupplyList
class Profile:
    def __init__(self, name, category='general', priority=1):
        self.name = name
        self.category = category
        self.priority = priority

    def to_dict(self):
        return {'name': self.name, 'category': self.category, 'priority': self.priority}


def add_profiles(storage):
    profiles = [Profile('Manager', 'management', 1), Profile('Buyer', 'procurement', 2)]
    for p in profiles:
        storage['profiles'].append(p)
    return storage.get('profiles', [])
