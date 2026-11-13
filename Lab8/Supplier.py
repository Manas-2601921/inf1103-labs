class Supplier:
    def __init__(self,supplier_id,name,contact_email):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    def display_information(self)->None:
        print(f"Supplier Id: {self.__supplier_id}")
        print(f"Supplier Name: {self.__name}")
        print(f"Supplier Email: {self.__contact_email}") 
    def supplier_to_dict(self)->dict:
        return {"supplier_id":self.__supplier_id, "supplier_name":self.__name, "supplier_contact_email":self.__contact_email}
