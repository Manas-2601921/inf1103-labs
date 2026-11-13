# show_type_hints.py
import inspect
from Supplier import Supplier
from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Order import Order
from OrderLine import OrderLine
from FileHandler import FileHandler

for cls in (Supplier, Product, PhysicalProduct, DigitalProduct,Inventory, Order, OrderLine, FileHandler):
    print(f"\n{cls.__name__}")
    for name, member in inspect.getmembers(cls, inspect.isfunction):
        if name in cls.__dict__: 
            print(f"  {name}{inspect.signature(member)}")