# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: SupplyList
VIEW_NAMES = ["all", "high_priority", "low_stock", "cheapest"]

def add_custom_view(list_data, view_name):
    if view_name not in VIEW_NAMES:
        raise ValueError("Недопустимое имя представления")
    filtered = list_data["items"]
    if view_name == "high_priority":
        filtered = [i for i in filtered if i["priority"] >= "high"]
    elif view_name == "low_stock":
        threshold = list_data.get("low_stock_threshold", 5)
        filtered = [i for i in filtered if i["stock"] <= threshold]
    elif view_name == "cheapest":
        filtered = sorted(filtered, key=lambda x: x["price"])
    list_data["views"] = list_data.get("views", {})
    list_data["views"][view_name] = filtered
    return list_data
