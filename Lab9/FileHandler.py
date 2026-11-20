import json
import os

from Product import Product
from ProductFactory import ProductFactory
from Supplier import Supplier


class FileHandler:
    def __init__(self, file_name: str):
        self.__file_name: str = file_name

    def load_file(self) -> list[Product]:
        data: list[Product] = []
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, "w", encoding="utf-8") as file_writer:
                json.dump([], file_writer)
            return []

        print(f"{self.__file_name} found")
        with open(self.__file_name, "r", encoding="utf-8") as file_reader:
            json_data = json.load(file_reader)
            for item in json_data:
                supplier = Supplier(item["supplier_id"], item["supplier_name"], item["supplier_contact_email"])
                data.append(ProductFactory.create(item["item_type"], item["productid"], item["Name"], item["Price"], item["Stock"], supplier, additional_weight=item.get("additional_weight", 0.0), download_size=item.get("download_size", 0.0)))
        print("file loaded successfully")
        return data

    def save_file(self, items_to_add: list[Product]) -> None:
        save_data = []
        for item in items_to_add:
            save_data.append(item.product_to_dict())
        with open(self.__file_name, "w", encoding="utf-8") as file_handler:
            json.dump(save_data, file_handler)
        print("Data has been saved successfully")
