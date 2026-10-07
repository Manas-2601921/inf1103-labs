
import json;
import os;

def handle_valid_product_input():
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
            print(f"ID: {product['productid']} | Name: {product['Name']} | Price: ${float(product['Price']):.2f} | Stock: {str(product['Stock'])}")

def add_product(dataToAdd):
    newProductID = input("ProductID: ")
    newProductName = input("Product Name: ")
    newProductPrice = input("Product Price: ")            
    newStockQuantity = input("Stock Quantity: ")
    if(newProductID == "" and newProductName == ""):
        print("\nUnable to add products. Some Fields are not entered correctly.")
    else:
        try:               
            newProductData = {"productid":newProductID,"Name": newProductName, "Price": float(newProductPrice), "Stock": int(newStockQuantity)}
            dataToAdd.append(newProductData)
            print("\nProduct added successfully!")
        except ValueError:
            print("\nUnable to add products. Some Fields are not entered correctly.")

def update_stock(productData, productIDUpdate):
    productFound = False
    for item in productData:
        if(item["productid"] == productIDUpdate):
            productFound = True
            print(f"Product Found:\nName:{item['Name']}\nCurrent Stock:{item['Stock']}")
            try:
                newQuantity = int(input("New stock quantity: "))
                item['Stock'] = newQuantity
                print("Stock Updated successfully!")
            except ValueError:
                print("Invalid stock quantity entered. Stock quantity must be an integer.")
    if(productFound == False):
        print("Product not found.")
        

def search_product(productData, productIDSearch):
    productFound = False
    for item in productData:
        if(item["productid"] == productIDSearch):
            print(f"Product Found:\n---\nID: {item['productid']}\nName: {item['Name']}\nPrice: ${float(item['Price']):.2f}\nStock: {item['Stock']}\n---")
            productFound = True
    if productFound == False:
        print("\n\nProduct not found.")
        
    

def save_inventory(itemsToAdd):
    print("Saving inventory...")
    with open('inventory.json','w',encoding="utf-8") as fileHandler:
        json.dump(itemsToAdd,fileHandler)
    print("Inventory successfully saved to inventory.json")
    return True

def load_inventory():
        if not os.path.exists('inventory.json'):
            with open('inventory.json','w',encoding='utf-8') as fileHandler:
                json.dump([],fileHandler)
            print("inventory.json found.")
            return []
        else:
            print("inventory.json found.")
            with open('inventory.json','r',encoding='utf-8') as fileReader:
                products = json.load(fileReader)
                print("inventory loaded successfully")
                return products
            
print(f"=============================\nINVENTORY MANAGEMENT SYSTEM\n=============================\n\n")
data = load_inventory()
print("---Menu---")
options = f"1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit"
print(options)
print("------")
while True:
    validatedUserInput = handle_valid_product_input() 
    if(validatedUserInput ==1):
        display_all(data)
    elif(validatedUserInput == 2):
        print("Add a new product")
        add_product(data)
    elif(validatedUserInput == 3):
        print("Update Stock")
        productIDUpdate = input("Enter product ID: ")
        update_stock(data,productIDUpdate)
    elif(validatedUserInput ==4):
        print("Search Product")
        productIDSearch = input("Enter product ID: ")
        search_product(data,productIDSearch)
    elif(validatedUserInput ==5):
        save_inventory(data)
    elif(validatedUserInput == 6):
        print("Saving inventory before exit...")
        save_inventory(data)
        print("\nThank you for using Inventory Management System.\nProgram Terminated")
        break
    else:
        print("Invalid option entered.")
        continue
            