import csv

from Inventory import Inventory
from ProductFactory import ProductFactory
from Supplier import Supplier


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            next(reader, None)
            for row_number, row in enumerate(reader, start=2):
                if not row:
                    continue
                try:
                    if len(row) != 5:
                        raise ValueError("Expected 5 columns.")
                    product_type, product_id, name, price, stock_quantity = row
                    product = ProductFactory.create(product_type, product_id, name, float(price), int(stock_quantity), supplier)
                except ValueError as error:
                    print(f"Skipping row {row_number}: {error}")
                else:
                    inventory.add_product(product)
                    loaded += 1
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")
