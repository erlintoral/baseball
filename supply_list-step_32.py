# === Stage 32: Добавь журнал действий пользователя ===
# Project: SupplyList
class ActionLog:
    def __init__(self):
        self.entries = []
    
    def add(self, user, action_type, description):
        entry = {
            'user': user,
            'action_type': action_type,
            'description': description,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.entries.append(entry)
    
    def log_purchase(self, supplier_name, item_name, quantity):
        self.add('Пользователь', 'Покупка', f'Заказ: {supplier_name}, {item_name}, кол-во: {quantity}')
    
    def log_price_update(self, supplier_name, item_name, new_price):
        self.add('Пользователь', 'Обновление цены', f'{supplier_name}: {item_name} -> {new_price} руб.')
    
    def log_priority_change(self, item_id, old_priority, new_priority):
        if item_id is not None:
            self.add('Пользователь', 'Изменение приоритета', f'ID {item_id}: {old_priority} -> {new_priority}')
    
    def get_log(self):
        return list(reversed(self.entries))

# Инициализация журнала при запуске приложения
action_log = ActionLog()
