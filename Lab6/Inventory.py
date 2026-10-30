class Inventory:
    #Stores products
    def __init__(self,inventory_collection):
        if inventory_collection is None or inventory_collection == []:
            self.__inventory_collection = []
        else:
            self.__inventory_collection = inventory_collection
    #Add Product
    def add_product(self,product):
        self.__inventory_collection.append(product)

    #Search Products
    def search_product(self,product_id):
        for collection in self.__inventory_collection:
            if(collection.get_product_id() == product_id):
                return collection
        return None

    #Displays Products
    def display_all(self):
        if self.__inventory_collection == [] or None:
            print("---NO ITEMS IN CURRENT INVENTORY---")
        else:
            print("Current Inventory\n---")
            for data in self.__inventory_collection:
                data.display_information()
                print("\n")
            print("---")
    def get_product_data(self):
        return self.__inventory_collection