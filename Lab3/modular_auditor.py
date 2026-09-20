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
        
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(value):
    taxed_amt = 0.10*value
    final_taxed_amt = taxed_amt + value
    return final_taxed_amt

def generate_report(final_total_value, userFailedAttempts):
    print("The total units in your inventory are: ", final_total_value)
    print("Number of failed/rejected entries: ",userFailedAttempts)
