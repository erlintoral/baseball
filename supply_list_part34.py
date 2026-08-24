# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: SupplyList
TEMPLATES = {
    "hardware": {"name": "Hardware", "fields": ["supplier", "price", "quantity", "priority", "note"]},
    "office": {"name": "Office", "fields": ["supplier", "price", "quantity", "priority", "note"]},
}

def get_template(name):
    return TEMPLATES.get(name, TEMPLATES["hardware"])

def create_from_template(template_name, overrides=None):
    tpl = get_template(template_name)
    defaults = {f: "" for f in tpl["fields"]}
    if overrides:
        defaults.update(overrides)
    return defaults
