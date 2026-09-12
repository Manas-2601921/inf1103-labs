inventory = 0
failedAttempts = 0

while True:
    userInput = input("Enter a stock quantity: ")
    if userInput == "quit":
        break
    if userInput.isdigit() == False:
        print("Stock quatity must be an integer.")
        failedAttempts = failedAttempts + 1
        continue
    else:
        userInputInt = int(userInput)
        if(userInputInt <0):
            print("Stock quatity cannot be an negative integer.")
            failedAttempts = failedAttempts + 1
            continue
        inventory = inventory + userInputInt
        if(inventory > 500):
            print("total inventory cannot exceed 500 units")
            failedAttempts = failedAttempts + 1
            break
print("Total Inventory Quantity: ",inventory)
print("Number of failed/rejected entries: ",failedAttempts)