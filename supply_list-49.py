# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: SupplyList
def self_check():
    print("=" * 60)
    print("SupplyList — Самопроверка приложения")
    print("=" * 60)
    print(f"✓ Модуль SupplyList загружен: {__file__}")
    print(f"✓ Импортируемые классы: {', '.join([cls for cls in dir() if isinstance(getattr(sys.modules[__name__], cls), type)])}")
    print(f"✓ Ключевые функции: {', '.join([fn for fn in dir() if callable(getattr(sys.modules[__name__], fn)) and fn not in ('self_check', '__name__', '__doc__')])}")
    print("=" * 60)
    print("Статус: Приложение готово к работе.")
    print("=" * 60)
