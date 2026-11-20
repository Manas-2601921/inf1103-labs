from DiscountStrategy import DiscountStrategy
from NoDiscount import NoDiscount
from OrderLine import OrderLine
from Product import Product


class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        if discount is None:
            self.__discount = NoDiscount()
        else:
            self.__discount = discount

    def add_order_line(self, product: Product, order_quantity: int) -> None:
        order_line = OrderLine(product, order_quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product: Product) -> None:
        order_line_to_remove = None
        for order_line in self.__order_lines:
            if order_line.get_product() == product:
                order_line_to_remove = order_line
                break
        if order_line_to_remove is not None:
            self.__order_lines.remove(order_line_to_remove)

    def get_order_lines(self) -> list[OrderLine]:
        return self.__order_lines

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def calculate_total(self) -> float:
        total = 0
        for order_line in self.__order_lines:
            subtotal = order_line.calculate_subtotal()
            total = total + subtotal
        return self.__discount.apply(total)

    def calculate_order_total(self) -> float:
        return self.calculate_total()
