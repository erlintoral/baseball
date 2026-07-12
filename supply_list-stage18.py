# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: SupplyList
def add_tags(items, tags):
    if not isinstance(tags, list) or not all(isinstance(t, str) for t in tags):
        raise TypeError("tags must be a list of strings")
    for item in items:
        for tag in tags:
            item.tags.add(tag)

def remove_tags(items, tags):
    if not isinstance(tags, list) or not all(isinstance(t, str) for t in tags):
        raise TypeError("tags must be a list of strings")
    for item in items:
        for tag in tags:
            item.tags.discard(tag)
