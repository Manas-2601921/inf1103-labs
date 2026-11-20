import sys
from pathlib import Path

lab_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(lab_folder))

from Inventory import Inventory
from Supplier import Supplier
from input_helpers import get_positive_float
from load_products import load_products

inventory = Inventory([])
supplier = Supplier("S2601921", "Manas", "manas@gmail.com")

print("Test 1: load a valid CSV, bad rows are skipped")
load_products(str(lab_folder / "products.csv"), inventory, supplier)
print("Products in inventory:", len(inventory.get_product_data()))

print("\nTest 2: load a file that does not exist")
load_products(str(lab_folder / "missing-products.csv"), inventory, supplier)

print("\nTest 3: invalid input is rejected (try 'abc', then -5, then 12.50)")
price = get_positive_float("Enter a price: ")
print("Accepted price:", price)
