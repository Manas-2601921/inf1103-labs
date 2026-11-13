from Supplier import Supplier
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct

#Create a Product and suppplier before creating or adding it to an Inventory.
supplier = Supplier("S001", "Bold", "bold@gmail.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 10, 2.5, supplier)

#Create 2 inventories a and b.
inventory_a = Inventory([])
inventory_b = Inventory([])

#Add the Product to Inventory A.
inventory_a.add_product(laptop)
print("Product added to inventory A:", inventory_a.find_product("P001") is laptop)

#Remove it from Inventory A and confirm that the Product object can still be used.
inventory_a.remove_product(laptop.get_product_id())
print("Product removed from inventory A:", inventory_a.find_product("P001") is None)
laptop.display_information()  

#Add the same Product object to Inventory B. 
inventory_b.add_product(laptop)
print("Product added to inventory B:", inventory_b.find_product("P001") is laptop)


inventory_b.remove_product(laptop.get_product_id())
inventory_b.remove_product(laptop.get_product_id())  # removing a missing id is a no-op

#Confirm that removing the Product from an inventory does not remove or destroy the Product itself.
print("Product still exists after removing:", laptop.get_product_id() == "P001")
