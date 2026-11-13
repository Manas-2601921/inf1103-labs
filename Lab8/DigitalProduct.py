from Product import Product
from Supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, productid:str,name:str,price:float,stock:int,download_size:float,supplier:Supplier):
        super().__init__(productid,name,price,stock,supplier)
        self.__download_size:float = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f}MB")
        print("Product Type: Digital")
    
    @staticmethod
    def get_fulfillment_information()->str:
       return "This product is delivered digitally"

    def product_to_dict(self)->dict:
             data = super().product_to_dict()
             data["download_size"] = self.__download_size
             data["item_type"] = "digital"
             return data