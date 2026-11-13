from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

#create supplier
test_supplier = Supplier("S001","Manas", "manas@email.com")

#Create a PhysicalProduct and a DigitalProduct using test_supplier
laptop = PhysicalProduct("P1", "Laptop", 1200.00, 10, 2.5, test_supplier)
ebook = DigitalProduct("P2", "E-book", 15.00, 100, 3.2, test_supplier)

#Display the supplier information through each Product
laptop.supplier.display_information()
ebook.supplier.display_information()