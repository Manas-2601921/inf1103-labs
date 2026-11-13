from abc import ABC, abstractmethod
from Supplier import Supplier

class Product(ABC):
    def __init__(self, productid:str, name:str, price:float, stock:int, supplier:Supplier):
        self.__productid = productid
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier = supplier

    @property
    def price(self):
        return self.__price
    @property
    def supplier(self):
        return self.__supplier

    def get_product_id(self):
        return self.__productid

    def update_stock(self,quantity:int):
        self.__stock = quantity

    def display_information(self):
        print(f"ProductId: {self.__productid}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")
        self.__supplier.display_information()

    def product_to_dict(self):
        supplier_dict = self.__supplier.supplier_to_dict()
        return({"productid": self.__productid, "Name": self.__name, "Price": self.__price, "Stock": self.__stock}|supplier_dict)

    @abstractmethod
    def get_fulfillment_information():
        pass
    
