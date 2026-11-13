from Product import Product
class Inventory:
    #Stores products
    def __init__(self,inventory_collection:list[Product]):
        if inventory_collection is None or inventory_collection == []:
            self.__inventory_collection:list[Product] = []
        else:
            self.__inventory_collection:list[Product] = inventory_collection
    #Add Product
    def add_product(self,product:Product)->None:
        self.__inventory_collection.append(product)

    def remove_product(self,productid:str)->None:
        product_to_remove = self.find_product(productid)
        if product_to_remove is not None:
            self.__inventory_collection.remove(product_to_remove)

    #Search Products
    def find_product(self,product_id:str)->Product | None:
        for collection in self.__inventory_collection:
            if(collection.get_product_id() == product_id):
                return collection
        return None
    

    #Displays Products
    def display_all(self)->None:
        if self.__inventory_collection == [] or None:
            print("---NO ITEMS IN CURRENT INVENTORY---")
        else:
            print("Current Inventory\n---")
            for data in self.__inventory_collection:
                data.display_information()
                print("\n")
            print("---")
    def get_product_data(self)->list[Product]:
        return self.__inventory_collection

    