from Supplier import Supplier
from Product import Product
from Inventory import Inventory

from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
# Create Supplier 
supplier = Supplier("S2601921", "Manas", "manas@gmail.com")

# Create 2 Products - PhysicalProduct and DigitalProduct
laptop = PhysicalProduct("P1", "Laptop", 1200.00, 10, 2.5, supplier)
ebook = DigitalProduct("P2", "E-book", 15.00, 100, 3.2, supplier)
# Create list and add created products to it
inventory_collection = list()
inventory_collection.append(laptop)
inventory_collection.append(ebook)

# Create Inventory object with the list of products
inventory = Inventory(inventory_collection)

def show_product_details(product: Product) -> None: 
        product.display_information() 
        print(product.get_fulfillment_information())

#Display information and fulfillment details for each product in the inventory
product_data = inventory.get_product_data()
for product in product_data:
    show_product_details(product)
    print("\n")