# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: SupplyList
def switch_profile():
    """Переключение активного пользовательского профиля."""
    global active_user
    print("Доступные профили:")
    for i, u in enumerate(users):
        status = " (текущий)" if u["name"] == active_user["name"] else ""
        print(f"  {i + 1}. {u['name']}{status}")
    choice = input("Введите номер профиля или 'q' для отмены: ").strip()
    if choice.lower() == 'q':
        return
    idx = int(choice) - 1
    if 0 <= idx < len(users):
        active_user = users[idx]
        print(f"Переключено на профиль: {active_user['name']}")
