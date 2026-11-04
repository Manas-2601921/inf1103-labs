import os 
import json
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

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
                    if(item["item_type"]=="physical"):
                        data.append(PhysicalProduct(item["productid"],item["Name"], item["Price"], item["Stock"], item["additional_weight"]))
                    else:
                        data.append(DigitalProduct(item["productid"],item["Name"], item["Price"], item["Stock"], item["download_size"]))
                print(f"file loaded successfully")
                return data

    def save_file(self,items_to_add):
        saveData = []
        for item in items_to_add:
            saveData.append(item.product_to_dict())
        with open(self.__file_name,'w',encoding="utf-8") as fileHandler:
            json.dump(saveData,fileHandler)
        print("Data has been saved successfully")
