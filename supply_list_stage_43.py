# === Stage 43: Добавь пагинацию длинных списков ===
# Project: SupplyList
def paginate(items, page_size=20):
    """Разбивает список на страницы, возвращая текущую и общее количество."""
    total_pages = (len(items) + page_size - 1) // page_size
    start = (page_size * (total_pages - 1)) % page_size
    end = start + page_size
    return {
        "items": items[start:end],
        "current_page": total_pages - (len(items[start:end]) == 0 and page_size or 0) or total_pages,
        "total_pages": total_pages,
        "total_items": len(items)
    }
