inventory = 0
failedAttempts = 0

def get_valid_input():
    global failedAttempts
    global inventory
    userInput = input("Enter a stock quantity: ")
    if userInput == "quit":
        return "quit"
    elif userInput.isdigit() == False:
        failedAttempts = failedAttempts + 1
        return "quit"
    else:
        intInputToValidate = int(userInput)
        if intInputToValidate < 0:
            failedAttempts = failedAttempts + 1
            print("Stock quatity cannot be an negative integer.")
        if inventory + intInputToValidate > 500:
            print("total inventory cannot exceed 500 units")
            failedAttempts = failedAttempts + 1
            return "quit"
        else:
            return intInputToValidate