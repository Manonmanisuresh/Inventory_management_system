import csv

def load_inventory():
    try:
        with open('inventory.csv', newline='') as file:
            reader = csv.reader(file)
            inventory = list(reader)
        return inventory
    except FileNotFoundError:
        return []

def save_inventory(inventory):
    with open('inventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(inventory)


def add_product(inventory):
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    for product in inventory:
        if product[0] == product_id:
            print("Product ID already exists.")
            return

    inventory.append([product_id, product_name, category, price, quantity])
    print("Product added successfully.")

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    print("Inventory:")
    print("Product ID | Product Name | Category | Price | Quantity")
    for product in inventory:
        print("{:<11} | {:<12} | {:<8} | {:<6} | {:<8}".format(*product))


def main():
    inventory = load_inventory()

    while True:
        print("\nMenu:")
        print("1. Add Product")
        print("2. Display Inventory")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            display_inventory(inventory)
        elif choice == '3':
            save_inventory(inventory)
            print("Inventory saved successfully. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
