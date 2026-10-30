import os 
import json
from Product import Product

class FileHandler:
    def __init__(self,file_name):
        self.__file_name = file_name

    def load_file(self):
        data = []
        if not os.path.exists(self.__file_name):
            with open(self.__file_name,'w',encoding='utf-8') as fileWriter:
                json.dump([],fileWriter)
                return []
        else:
            print(f"{self.__file_name} found")
            with open(self.__file_name,'r',encoding='utf-8') as fileReader:
                json_data = json.load(fileReader)
                for item in json_data:
                    data.append(Product(item["productid"],item["Name"], item["Price"], item["Stock"]))
                print(f"file loaded successfully")
                return data

    def save_file(self,itemsToAdd):
        saveData = []
        for item in itemsToAdd:
            saveData.append(item.product_to_dict())
        with open(self.__file_name,'w',encoding="utf-8") as fileHandler:
            json.dump(saveData,fileHandler)
        print("Data has been saved successfully")
