# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: SupplyList
import argparse

def main():
    parser = argparse.ArgumentParser(description="SupplyList - Plan your purchases")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("add", help="Add a new supplier")
    sub.add_parser("list", help="List all suppliers")
    sub.add_parser("order", help="Place a new order")
    sub.add_parser("stock", help="Check current stock")
    sub.add_parser("notes", help="View/edit notes")
    sub.add_parser("help", help="Show this help")

    args = parser.parse_args()
    print(f"SupplyList v1.0 - Command: {args.command}")

if __name__ == "__main__":
    main()
