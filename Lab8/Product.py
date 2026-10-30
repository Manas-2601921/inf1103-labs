class Product:
    def __init__(self, productid, name, price, stock):
        self.__productid = productid
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__productid

    def update_stock(self,quantity):
        self.__stock = quantity

    def display_information(self):
        print(f"ProductId: {self.__productid}")
        print(f"Name: {self.__name}")
        print(f"Price: {self.__price}")
        print(f"Stock: {self.__stock}")

    def product_to_dict(self):
        return({"productid": self.__productid, "Name": self.__name, "Price": self.__name, "Stock": self.__stock})
    
