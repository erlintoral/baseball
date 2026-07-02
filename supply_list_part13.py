# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: SupplyList
class SearchFilter:
    def __init__(self, data):
        self.data = data
    
    def search(self, query=None, fields=None):
        if not query or not fields:
            return list(self.data)
        
        query_lower = query.lower()
        filtered = []
        
        for item in self.data:
            match_count = 0
            for field_name in fields:
                value = str(item.get(field_name, '')).lower()
                if query_lower in value:
                    match_count += 1
            
            # Если совпадения найдены хотя бы в одном из указанных полей
            if match_count > 0:
                filtered.append(item)
        
        return filtered

# Пример использования (раскомментируйте для теста):
# supply_list = SupplyList()
# results = SearchFilter(supply_list.items).search(query="комплект", fields=["name", "supplier_name"])
