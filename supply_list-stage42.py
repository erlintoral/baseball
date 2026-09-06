# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: SupplyList
import sys

def enable_color(enabled: bool):
    if not hasattr(enable_color, "saved"):
        enable_color.saved = True
    if enabled:
        sys.stdout.reconfigure(encoding='utf-8')
        if sys.stdout.isatty():
            enable_color.enabled = True
    else:
        enable_color.enabled = False
    return enable_color.enabled

if enable_color.enabled:
    C = "\033["
    BOLD = f"{C}1;1m"
    RESET = f"{C}0m"
    RED = f"{C}31m"
    GREEN = f"{C}32m"
    YELLOW = f"{C}33m"
    CYAN = f"{C}36m"
    BG_RED = f"{C}41m"
    BG_GREEN = f"{C}42m"
    BG_YELLOW = f"{C}43m"
    BG_CYAN = f"{C}46m"
    dim = f"{C}2m"
    def style(text, fg, bg, bold=False):
        code = ""
        if bold: code += BOLD
        if fg: code += fg
        if bg: code += bg
        return code + str(text) + RESET
    def header(text): return style(text, CYAN, None, True)
    def ok(text): return style(text, GREEN, BG_GREEN, True)
    def warn(text): return style(text, YELLOW, BG_YELLOW, True)
    def err(text): return style(text, RED, BG_RED, True)
    def info(text): return style(text, GREEN, None)
    def dim_text(text): return dim + str(text) + RESET
else:
    def style(text, *args): return str(text)
    def header(text): return str(text)
    def ok(text): return str(text)
    def warn(text): return str(text)
    def err(text): return str(text)
    def info(text): return str(text)
    def dim_text(text): return str(text)
