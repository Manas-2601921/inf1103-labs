from Product import Product
class DigitalProduct(Product):
    def __init__(self, productid,name,price,stock,download_size):
        super().__init__(productid,name,price,stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f}MB")
        print("Product Type: Digital")

    def get_fulfillment_information():
        print("This product is delivered digitally")

    def product_to_dict(self):
             data = super().product_to_dict()
             data["download_size"] = self.__download_size
             data["item_type"] = "digital"
             return data