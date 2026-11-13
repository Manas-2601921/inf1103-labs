from OrderLine import OrderLine
from Product import Product

class Order:
    def __init__(self,order_id:str):
        self.__order_id = order_id
        self.__order_lines:list[OrderLine] = []

    def add_order_line(self, product:Product, order_quantity:int):
        order_line = OrderLine(product, order_quantity) 
        self.__order_lines.append(order_line) 

    def remove_order_line(self, product:Product):
        order_line_to_remove = None
        for order_line in self.__order_lines:
            if order_line.get_product() == product:
                order_line_to_remove = order_line
                break
        if order_line_to_remove is not None:
            self.__order_lines.remove(order_line_to_remove) 

    def get_order_lines(self):
        return self.__order_lines

    def calculate_order_total(self):
        total = 0
        for order_line in self.__order_lines:
            sub_total = order_line.calculate_subtotal()
            total = total + sub_total
        return total

