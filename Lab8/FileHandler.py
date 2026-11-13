import os 
import json
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
from Product import Product

class FileHandler:
    def __init__(self,file_name:str):
        self.__file_name:str = file_name

    def load_file(self)->list[Product]:
        data:list[Product] = []
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
                        supplier = Supplier(item["supplier_id"], item["supplier_name"], item["supplier_contact_email"])
                        data.append(PhysicalProduct(item["productid"],item["Name"], item["Price"], item["Stock"], item["additional_weight"],supplier))
                    else:
                        supplier = Supplier(item["supplier_id"], item["supplier_name"], item["supplier_contact_email"])
                        data.append(DigitalProduct(item["productid"],item["Name"], item["Price"], item["Stock"], item["download_size"],supplier))
                print(f"file loaded successfully")
                return data

    def save_file(self,items_to_add:list[Product])->None:
        saveData = []
        for item in items_to_add:
            saveData.append(item.product_to_dict())
        with open(self.__file_name,'w',encoding="utf-8") as fileHandler:
            json.dump(saveData,fileHandler)
        print("Data has been saved successfully")
