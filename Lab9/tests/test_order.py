import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from BulkDiscount import BulkDiscount
from NoDiscount import NoDiscount
from Order import Order
from PercentageDiscount import PercentageDiscount
from ProductFactory import ProductFactory
from StudentDiscount import StudentDiscount
from Supplier import Supplier


def test_discount_totals() -> None:
    supplier = Supplier("S2601921", "Manas", "manas@gmail.com")
    laptop = ProductFactory.create("physical", "P1", "Laptop", 1200.00, 10, supplier, additional_weight=2.5)
    ebook = ProductFactory.create("digital", "P2", "E-book", 15.00, 100, supplier, download_size=3.2)
    order = Order("O-001")
    order.add_order_line(laptop, 2)
    order.add_order_line(ebook, 3)

    print("No discount:", order.calculate_total())
    order.set_discount(BulkDiscount(200, 20))
    print("Bulk discount:", order.calculate_total())
    order.set_discount(PercentageDiscount(10))
    print("Percentage discount:", order.calculate_total())
    order.set_discount(StudentDiscount())
    print("Student discount:", order.calculate_total())
    order.set_discount(NoDiscount())
    print("No discount:", order.calculate_total())


def test_quantity_validation() -> None:
    supplier = Supplier("S2601921", "Manas", "manas@gmail.com")
    laptop = ProductFactory.create("physical", "P1", "Laptop", 1200.00, 10, supplier, additional_weight=2.5)
    order = Order("O-002")

    for quantity in (0, -1):
        try:
            order.add_order_line(laptop, quantity)
        except ValueError as error:
            print(f"Invalid quantity {quantity}:", error)


if __name__ == "__main__":
    test_discount_totals()
    test_quantity_validation()
