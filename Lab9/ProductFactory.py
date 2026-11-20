from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
from Product import Product
from Supplier import Supplier


class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier, *, additional_weight: float = 0.0, download_size: float = 0.0) -> Product:
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, additional_weight, supplier)
        if product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, download_size, supplier)
        raise ValueError(f"Unknown product type: {product_type}")
