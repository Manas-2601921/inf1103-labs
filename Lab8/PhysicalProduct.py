from CanBeShipped import CanBeShipped
from Product import Product
from Supplier import Supplier
class PhysicalProduct(Product,CanBeShipped):
    def __init__(self,productid:str,name:str,price:float,stock:int, additional_weight:float,supplier:Supplier):
        super().__init__(productid,name,price,stock,supplier)
        self.__additional_weight = additional_weight

    def display_information(self):
        super().display_information()
        print(f"Additional Weight: {self.__additional_weight:.2f}kg")
        print("Product Type: Physical")
    @staticmethod
    def get_fulfillment_information():
            print("This product requires physical shipping")

    def calculate_shipping_costs(self):
         base_fee = 5.00
         rate_per_kg = 2.00
         shipping_fee = base_fee + self.__additional_weight * rate_per_kg
         return shipping_fee

    def product_to_dict(self):
         data = super().product_to_dict()
         data["additional_weight"] = self.__additional_weight
         data["item_type"] = "physical"
         return data