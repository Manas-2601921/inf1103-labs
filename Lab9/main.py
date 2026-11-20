import os

from FileHandler import FileHandler
from Inventory import Inventory
from ProductFactory import ProductFactory
from Supplier import Supplier
from input_helpers import get_positive_float
from load_products import load_products

lab_folder = os.path.dirname(os.path.abspath(__file__))


def handle_valid_product_input() -> int | None:
    welcome_banner = "=============================\nINVENTORY MANAGEMENT SYSTEM\n============================="
    print(welcome_banner)
    print("---Menu---")
    options = (
        "1. Display All Products\n"
        "2. Add Product\n"
        "3. Update Stock\n"
        "4. Search Product\n"
        "5. Save Inventory\n"
        "6. Exit"
    )
    print(options)
    print("------")
    user_option = input("Enter option: ")
    if user_option.isdigit():
        return int(user_option)
    return None


def handle_user_input_options(user_input_option: int | None, inventory: Inventory) -> None:
    file_handler = FileHandler(os.path.join(lab_folder, "inventory.json"))

    if user_input_option == 1:
        inventory.display_all()

    elif user_input_option == 2:
        print("Add a new product")
        try:
            product_type_option = int(input("Is the product:\n1. Physical\n2. Digital\nEnter your option here: "))
            if product_type_option not in (1, 2):
                print("Incorrect option entered. Please enter option number 1 or 2 only.")
                return

            product_id = input("ProductID: ")
            product_name = input("Product Name: ")
            product_price = get_positive_float("Product Price: ")
            stock_quantity = int(input("Stock Quantity: "))
            additional_weight = 0.0
            download_size = 0.0

            if product_type_option == 1:
                additional_weight = float(input("Enter the additional weight of your product: "))
                product_type = "physical"
            else:
                download_size = float(input("Enter the download size of your product: "))
                product_type = "digital"

            supplier_id = input("Enter supplier id: ")
            supplier_name = input("Enter supplier name: ")
            supplier_contact_email = input("Enter supplier contact email: ")
            supplier = Supplier(supplier_id, supplier_name, supplier_contact_email)

            if product_type_option == 1:
                new_product = ProductFactory.create(product_type, product_id, product_name, product_price, stock_quantity, supplier, additional_weight=additional_weight)
            else:
                new_product = ProductFactory.create(product_type, product_id, product_name, product_price, stock_quantity, supplier, download_size=download_size)

            inventory.add_product(new_product)
            print("Product has been added successfully.")
        except ValueError as error:
            print(f"Invalid product details: {error}")

    elif user_input_option == 3:
        product_id_update = input("Enter product ID: ")
        found_product = inventory.find_product(product_id_update)
        if found_product is not None:
            print("Product Found:")
            found_product.display_information()
            try:
                new_quantity = int(input("New stock quantity: "))
                found_product.update_stock(new_quantity)
            except ValueError as error:
                print(f"Invalid stock quantity: {error}")
            else:
                found_product.display_information()
                print("Stock Updated successfully!")
        else:
            print(f"No product with the id: {product_id_update} exists. No record to update here.")

    elif user_input_option == 4:
        product_id_search = input("Enter product ID: ")
        found_product = inventory.find_product(product_id_search)
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


def main() -> None:
    file_handler = FileHandler(os.path.join(lab_folder, "inventory.json"))
    current_data = file_handler.load_file()
    inventory = Inventory(current_data)

    if current_data == []:
        supplier = Supplier("S001", "Manas", "manas@gmail.com")
        load_products(os.path.join(lab_folder, "products.csv"), inventory, supplier)

    while True:
        user_option = handle_valid_product_input()
        handle_user_input_options(user_option, inventory)
        if user_option == 6:
            break


if __name__ == "__main__":
    main()
