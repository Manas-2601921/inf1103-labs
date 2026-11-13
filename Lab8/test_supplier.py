from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

#create supplier
test_supplier = Supplier("S2601921", "Manas", "manas@gmail.com")

#Create a PhysicalProduct and a DigitalProduct using test_supplier
laptop = PhysicalProduct("P1", "Laptop", 1200.00, 10, 2.5, test_supplier)
ebook = DigitalProduct("P2", "E-book", 15.00, 100, 3.2, test_supplier)

#Display the supplier information through each Product
laptop.supplier.display_information()
print("\n")
ebook.supplier.display_information()

del test_supplier

try:
    print(test_supplier, "\n")
except NameError as e:
    print(f"\nNameError: {e}", "\n")

#Confirm that the Supplier and Products are separate objects and can exist independently. 
laptop.display_information()
print("\n")
ebook.display_information()