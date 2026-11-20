import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ProductFactory import ProductFactory
from Supplier import Supplier


def test_factory_products() -> None:
    supplier = Supplier("S2601921", "Manas", "manas@gmail.com")
    physical_product = ProductFactory.create("physical", "P1", "Laptop", 1200.00, 10, supplier, additional_weight=2.5)
    digital_product = ProductFactory.create("digital", "P2", "E-book", 15.00, 100, supplier, download_size=3.2)

    print("Physical product:", type(physical_product).__name__)
    print("Shipping cost:", physical_product.calculate_shipping_costs())
    print("Digital product:", type(digital_product).__name__)


def test_unknown_product() -> None:
    supplier = Supplier("S2601921", "Manas", "manas@gmail.com")

    try:
        ProductFactory.create("service", "P3", "Install", 30.00, 5, supplier)
    except ValueError as error:
        print("Unknown product:", error)


def test_product_validation() -> None:
    supplier = Supplier("S2601921", "Manas", "manas@gmail.com")

    for price in (0, -1):
        try:
            ProductFactory.create("physical", "P1", "Laptop", price, 0, supplier)
        except ValueError as error:
            print(f"Invalid price {price}:", error)

    try:
        ProductFactory.create("digital", "P2", "E-book", 15.00, -1, supplier)
    except ValueError as error:
        print("Invalid stock:", error)


if __name__ == "__main__":
    test_factory_products()
    test_unknown_product()
    test_product_validation()
