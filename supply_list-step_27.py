# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: SupplyList
def reset_demo_data():
    """Сбросить данные в демо-режиме."""
    global suppliers, items, notes
    suppliers = [
        {"id": 1, "name": "TechParts", "stock": 500},
        {"id": 2, "name": "GadgetWorld", "stock": 300},
        {"id": 3, "name": "ElectroBay", "stock": 700},
    ]
    items = [
        {"id": 1, "supplier_id": 1, "name": "Микроконтроллер", "price": 25.0, "qty_ordered": 0, "priority": 3, "note": ""},
        {"id": 2, "supplier_id": 2, "name": "Сенсорный экран", "price": 15.0, "qty_ordered": 0, "priority": 1, "note": ""},
        {"id": 3, "supplier_id": 3, "name": "Блок питания", "price": 8.5, "qty_ordered": 0, "priority": 2, "note": ""},
    ]
    notes = [
        {"item_id": 1, "text": "Закупить для прототипа"},
        {"item_id": 3, "text": "Нужен запас на зиму"},
    ]


def clear_all():
    """Очистить все данные."""
    global suppliers, items, notes
    suppliers = []
    items = []
    notes = []
