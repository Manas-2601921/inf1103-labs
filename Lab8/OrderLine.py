from Product import Product
class OrderLine:
    def __init__(self, product:Product, order_quantity:int):
        self.__product:Product = product
        self.__order_quantity = order_quantity
    def calculate_subtotal(self): 
        return float(self.__product.price * self.__order_quantity)
    def get_product(self):
        return self.__product
    def display_orderline(self):
        self.__product.display_information()
        print(f"Order Quantity: {self.__order_quantity}")