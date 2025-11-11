import csv
import os
from typing import Dict, List, Optional

try:
    import pandas as pd
    HAS_PANDAS = True
except Exception:
    HAS_PANDAS = False


DATA_FILE = "inventory.csv"
CSV_HEADERS = ["id", "name", "category", "price", "quantity"]


class Item:
    def __init__(self, id: str, name: str, category: str, price: float, quantity: int):
        self.id = id.strip()
        self.name = name.strip()
        self.category = category.strip()
        self.price = float(price)
        self.quantity = int(quantity)

    @property
    def stock_value(self) -> float:
        return self.price * self.quantity

    def to_row(self) -> List[str]:
        return [self.id, self.name, self.category, f"{self.price:.2f}", str(self.quantity)]

    @staticmethod
    def from_row(row: Dict[str, str]) -> "Item":
        return Item(
            id=row["id"],
            name=row["name"],
            category=row["category"],
            price=float(row["price"]),
            quantity=int(row["quantity"]),
        )


class Inventory:
    def __init__(self):
        self.items: Dict[str, Item] = {}

    # ---------- CRUD ---------- #
    def check_item(self, item: Item) -> bool:
        if item.id in self.items:
            return False
        self.items[item.id] = item
        return True

    def remove_itemcheck(self, item_id: str) -> bool:
        return self.items.pop(item_id, None) is not None

    def update_quantity(self, item_id: str, delta: int) -> bool:
        item = self.items.get(item_id)
        if not item:
            return False
        item.quantity = max(0, item.quantity + delta)
        return True

    def set_quantity(self, item_id: str, quantity: int) -> bool:
        item = self.items.get(item_id)
        if not item:
            return False
        item.quantity = max(0, quantity)
        return True

    # ---------- Queries ---------- #
    def list_items(self) -> List[Item]:
        return list(self.items.values())

    def find_by_name(self, keyword: str) -> List[Item]:
        kw = keyword.lower()
        result = []
        for i in self.items.values():
            if kw in i.name.lower():
                result.append(i)
        return result

    def items_by_category(self) -> dict[str, int]:
        result = {}
        for item in self.items.values():
            category = item.category
            if category not in result:
                result[category] = 0
            result[category] += 1

        return result

def ensure_csv_exists():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)


def load_inventory() -> Inventory:
    inv = Inventory()
    ensure_csv_exists()
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row and row.get("id"):
                inv.check_item(Item.from_row(row))
    return inv



def save_inventory(inv: Inventory):
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADERS)
        for item in inv.list_items():
            writer.writerow(item.to_row())


def print_items(items: List[Item]):
    if not items:
        print("No items.")
        return
    print("-" * 78)
    print(f"{'ID':<10} {'Name':<24} {'Category':<15} {'Price':>8} {'Qty':>6} {'Value':>9}")
    print("-" * 78)
    for it in items:
        print(f"{it.id:<10} {it.name:<24} {it.category:<15} {it.price:>8.2f} {it.quantity:>6} {it.stock_value:>9.2f}")
    print("-" * 78)


# --------------- INPUT HELPERS ---------------- #
def prompt_float(label: str) -> float:
    while True:
        try:
            return float(input(label))
        except ValueError:
            print("Please enter a number.")


def prompt_int(label: str) -> int:
    while True:
        try:
            return int(input(label))
        except ValueError:
            print("Please enter an integer.")


# --------------- MENU ACTIONS ----------------- #
def action_add(inv: Inventory):
    print("\nAdd new item")
    id_ = input("ID: ").strip()
    name = input("Name: ").strip()
    category = input("Category: ").strip()
    price = prompt_float("Price: ")
    qty = prompt_int("Quantity: ")
    ok = inv.check_item(Item(id_, name, category, price, qty))
    if ok:
        save_inventory(inv)
        print("Added.")
    else:
        print("ID already exists. Use a different ID.")


def action_remove(inv: Inventory):
    print("\nRemove item")
    id_ = input("ID: ").strip()
    if inv.remove_itemcheck(id_):
        save_inventory(inv)
        print("Removed.")
    else:
        print("Not found.")


def action_update_qty(inv: Inventory):
    print("\nUpdate quantity")
    id_ = input("ID: ").strip()
    mode = input("Set (s) or Change (c)? ").strip().lower()
    if mode == "s":
        qty = prompt_int("New quantity: ")
        ok = inv.set_quantity(id_, qty)
    else:
        delta = prompt_int("Change by (e.g., +5 or -3): ")
        ok = inv.update_quantity(id_, delta)
    if ok:
        save_inventory(inv)
        print("Updated.")
    else:
        print("Not found.")


def action_search(inv: Inventory):
    kw = input("\nSearch name contains: ").strip()
    print_items(inv.find_by_name(kw))


def action_list(inv: Inventory):
    print("\nAll items:")
    print_items(inv.list_items())



# --------------- MAIN LOOP -------------------- #
def main():
    inv = load_inventory()

    while True:
        print("\n=== Inventory Manager ===")
        print("1) List items")
        print("2) Add item")
        print("3) Remove item")
        print("4) Update quantity")
        print("5) Search by name")
        print("0) Exit")
        choice = input("Select: ").strip()

        if choice == "1":
            action_list(inv)
        elif choice == "2":
            action_add(inv)
        elif choice == "3":
            action_remove(inv)
        elif choice == "4":
            action_update_qty(inv)
        elif choice == "5":
            action_search(inv)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

