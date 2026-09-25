import os;

failedAttempts = 0

def handle_valid_product_input():
    global failedAttempts
    userProductName = input("Enter Product Name(or 'quit' to exit): ")
    if isinstance(userProductName,int) == True:
        failedAttempts = failedAttempts + 1
        return "quit"
    if userProductName == "quit":
        return "quit"
    else:
        userQuantity = input("Enter Quantity: ")
        if userQuantity.isdigit() == False:
            failedAttempts = failedAttempts + 1
            return "quit"
        else:
            return userProductName,userQuantity
def save_inventory(productName, productQuantity):
    with open('inventory.txt','r+',encoding="utf-8") as fileHandler:
        fileRecords = fileHandler.read().splitlines()
        recordsLength = len(fileRecords)
        if recordsLength == 0:
            itemToWrite = "1001, " + productName + ", " + productQuantity 
            fileHandler.write(itemToWrite)
            print("\n")
            print("New order added:")
            print(itemToWrite)
            totalInventoryStr = str(len(fileRecords))
            print("Tax: $0.10 | Total Inventory: ", totalInventoryStr)
            print("\n")
            print("Orders successfully saved to orders.txt")
            return True
        else:
            print(fileRecords)
            comparNum = int(fileRecords[0].split(",")[0])
            for record in fileRecords:
                orderNum = int(record.split(",")[0])
                if(orderNum > comparNum):
                    comparNum = orderNum

            orderNumToAdd = str(comparNum + 1)
            itemToWrite = orderNumToAdd + ", " + productName + ", " + productQuantity 
            fileHandler.write("\n"+itemToWrite)
            print("\n")
            print("New order added:")
            print(itemToWrite)
            print("\n")
            print("Orders successfully saved to orders.txt")
            return True

def load_inventory():
    if not os.path.exists('inventory.txt'):
        with open('inventory.txt', 'w', encoding='utf-8') as fileWriter:
            pass  # creates an empty inventory.txt
    with open('inventory.txt','r',encoding='utf-8') as fileReader:
        products = fileReader.read()
    print("Current Orders:\n")
    print(products)

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
        
load_inventory()
print("\n")
while True:
    validatedUserInput = handle_valid_product_input() 
    if validatedUserInput == "quit":
        break
    else:
        productToAdd = validatedUserInput[0]
        quantityToAdd = validatedUserInput[1]
        result = save_inventory(productToAdd,quantityToAdd)
generate_report()