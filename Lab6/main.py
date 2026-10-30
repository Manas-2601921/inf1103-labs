from Product import Product
from Inventory import Inventory
from FileHandler import FileHandler

def handle_valid_product_input():
    welcomeBannner = f"=============================\nINVENTORY MANAGEMENT SYSTEM\n============================="
    print(welcomeBannner)
    print("---Menu---")
    options = f"1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit"
    print(options)
    print("------")
    userOption = input("Enter option: ")
    if userOption.isdigit() == True:
        return int(userOption)

def handle_user_input_options(user_input_option, inventory):
    file_handler = FileHandler("inventory.json")

    if user_input_option == 1:
        inventory.display_all()

    elif user_input_option == 2:
        print("Add a new product")
        new_product_id = input("ProductID: ")
        new_product_name = input("Product Name: ")
        new_product_price = input("Product Price: ")
        new_stock_quantity = input("Stock Quantity: ")
        try:
            new_product = Product(new_product_id, new_product_name, float(new_product_price), int(new_stock_quantity))
        except ValueError:
            print("Price must be a number and quantity must be a whole number.")
        else:
            inventory.add_product(new_product)
            print("Product has been added successfully.")

    elif user_input_option == 3:
        product_id_update = input("Enter product ID: ")
        found_product = inventory.search_product(product_id_update)
        if found_product is not None:
            print("Product Found:")
            found_product.display_information()
            try:
                new_quantity = int(input("New stock quantity: "))
            except ValueError:
                print("Invalid stock quantity entered. Enter an integer value.")
            else:
                found_product.update_stock(new_quantity)
                found_product.display_information()
                print("Stock Updated successfully!")
        else:
            print(f"No product with the id: {product_id_update} exists. No record to update here.")

    elif user_input_option == 4:
        product_id_search = input("Enter product ID: ")
        found_product = inventory.search_product(product_id_search)
        if found_product is not None:
            print("Product Found:")
            found_product.display_information()
        else:
            print(f"No product with the id: {product_id_search} exists.")

    elif user_input_option == 5:

        file_handler.save_file(inventory.get_product_data())

    elif user_input_option == 6:
        print("Saving inventory before exit...")
        file_handler.save_file(inventory.get_product_data())
        print("Thank you for using Inventory Management System.\nProgram Terminated")

    else:
        print("Invalid option number. Enter an option number between 1-6.")


def main():
    fh1 = FileHandler("inventory.json")
    currentData = fh1.load_file()
    inventory = Inventory(currentData)
    while True:
        userOption = handle_valid_product_input()
        handle_user_input_options(userOption, inventory)
        if(userOption == 6):
            break
if __name__ == "__main__":
    main()