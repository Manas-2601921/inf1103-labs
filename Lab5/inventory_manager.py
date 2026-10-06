
import json;
import os;

failedAttempts = 0

def handle_valid_product_input():
    global failedAttempts
    welcomeBannner = f"=============================\nINVENTORY MANAGEMENT SYSTEM\n============================="
    print(welcomeBannner)
    print("---Menu---")
    options = f"1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit"
    print(options)
    print("------")
    userOption = input("Enter option: ")
    if userOption.isdigit() == True:
        return int(userOption)

def display_all(productData):
    productList = []
    if not productData:
        print("---NO ITEMS IN CURRENT INVENTORY---")
    else:
        print("Current Inventory\n---")
        for product in productData:
            print(f"ID: {product["productid"]} | Name: {product["Name"]} | Price: ${str(product["Price"])} | Stock: {str(product["Stock"])}")
            print("---")

def handle_user_input_options(userInputOptions,dataToHandle):
    productData = dataToHandle
    if(userInputOptions ==1):
        display_all(productData)
    elif(userInputOptions == 2):
        print("Add a new product")
        newProductID = input("ProductID: ")
        newProductName = input("Product Name: ")
        newProductPrice = input("Product Price: ")
        newStockQuantity = input("Stock Quantity: ")
    
        productData.append({"productid":newProductID,"Name": newProductName, "Price": float(newProductPrice), "Stock": int(newStockQuantity)})
    elif(userInputOptions == 3):
        productIDUpdate = input("Enter product ID: ")
        for item in productData:
            if(item["productid"] == productIDUpdate):
                print(f"Product Found:\n Name:{item['Name']}\nCurrent Stock:{item['Stock']}")
                newQuantity = int(input("New stock quantity: "))
                item['Stock'] = newQuantity
                print("Stock Updated successfully!")
    elif(userInputOptions ==4):
        productIDUpdate = int(input("Enter product ID: "))
        for item in productData:
            if(item["productid"] == productIDUpdate):
                print(f"Product Found:---\n Name:{item['Name']}\nCurrent Stock:{item['Stock']}\n---")
    elif(userInputOptions ==5):
        save_inventory(productData)

    else:
        print("Saving inventory before exit...")
        save_inventory(productData)
        print("Thank you for using Inventory Management System.\nProgram Terminated")
def save_inventory(itemsToAdd):
    with open('inventory.json','w',encoding="utf-8") as fileHandler:
        json.dump(itemsToAdd,fileHandler)
    print("Iventory successfully saved to inventory.json")
    return True

def load_inventory():
        if not os.path.exists('inventory.json'):
            with open('inventory.json','w',encoding='utf-8') as fileWriter:
                json.dump([],fileWriter)
        else:
            print("inventory.json found")
            with open('inventory.json','r',encoding='utf-8') as fileReader:
                products = json.load(fileReader)
                print("inventory loaded successfully")
                return products


def generate_report():
    totalquantity = 0
    print("===== Audit Report ====")
    with open('inventory.txt','r+',encoding="utf-8") as fileHandler:
        records = fileHandler.readlines()
        print("Total transactions recorded: " + str(len(records)) )
        for record in records:
            quantity = int(record.split(',')[2])
            totalquantity = totalquantity + quantity
        print("Total Units Processed: " + str(totalquantity) )
        print("Number of Failed/Rejected Entries: " + str(failedAttempts))
        
data = load_inventory()
print("\n")
while True:
    validatedUserInput = handle_valid_product_input() 
    handle_user_input_options(validatedUserInput,data)