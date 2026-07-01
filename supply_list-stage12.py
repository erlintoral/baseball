# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: SupplyList
def load_from_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict) and 'items' in data:
            for item_data in data['items']:
                add_item(item_data)
        elif isinstance(data, list):
            for item_data in data:
                add_item(item_data)
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных из {filepath}: {type(e).__name__}")
