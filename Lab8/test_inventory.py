from Supplier import Supplier
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct

# Prediction: the Product still works after removal, because the Inventory
# only holds a reference; the Product object exists independently of it.
supplier = Supplier("S001", "Bold", "bold@gmail.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 10, 2.5, supplier)

inventory_a = Inventory([])
inventory_b = Inventory([])

inventory_a.add_product(laptop)
assert inventory_a.find_product("P001") is laptop

inventory_a.remove_product(laptop.get_product_id())
assert inventory_a.find_product("P001") is None
laptop.display_information()  # still usable after removal

inventory_b.add_product(laptop)
assert inventory_b.find_product("P001") is laptop

inventory_b.remove_product(laptop.get_product_id())
inventory_b.remove_product(laptop.get_product_id())  # removing a missing id is a no-op
assert laptop.get_product_id() == "P001"
