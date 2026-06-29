# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: SupplyList
def save_to_json(data, filename="supply_list.json"):
    import json
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные успешно сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def load_from_json(filename="supply_list.json"):
    import json
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Начните с пустого списка.")
        return []

if __name__ == "__main__":
    # Пример использования для проверки сохранения и загрузки
    test_data = {"suppliers": [], "orders": []}
    save_to_json(test_data)
    loaded_data = load_from_json()
    print(f"Загруженные данные: {loaded_data}")
