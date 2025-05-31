# ----------------------------------- Assignment # 6 --------------------------------------------

# NAME : Taaha Akbar Cheema
# ROLL NO:  PIAIC 204780
# Batch No : 70

 #--------------------------------Project 1: Smart Grocery Store Assistant--------------------

# Product catalog: key = item name, value = (price, stock)
product_catalog = {
    "apple": (100, 10),
    "banana": (60, 20),
    "orange": (80, 15),
    "mango": (150, 5)
}

# Function to view available products
def display_products():
    print("\nAvailable Products:")
    for product, (price, stock) in product_catalog.items():
        print(f"{product.capitalize()} - Rs.{price}, In stock: {stock}")
        # Alert if stock is low
        if stock < 5:
            print(f"*** ALERT: Stock for {product.capitalize()} is low! ***")
    print("\n")

# Function to add or update product stock or price
def add_update_product():
    product_name = input("Enter product name to add/update: ").lower()
    if product_name in product_catalog:
        print(f"Updating {product_name.capitalize()}...")
    else:
        print(f"Adding new product {product_name.capitalize()}...")

    price = float(input(f"Enter the price for {product_name}: Rs."))
    stock = int(input(f"Enter the stock for {product_name}: "))

    product_catalog[product_name] = (price, stock)
    print(f"{product_name.capitalize()} has been updated successfully.\n")

# Function to simulate a customer purchase
def purchase_item():
    total_amount = 0
    purchased_items = []

    while True:
        product_name = input("Enter product name to purchase (or type 'done' to finish): ").lower()

        if product_name == 'done':
            break

        if product_name in product_catalog:
            price, stock = product_catalog[product_name]
            if stock > 0:
                quantity = int(input(f"Enter quantity of {product_name} to purchase: "))
                if quantity <= stock:
                    total_amount += price * quantity
                    purchased_items.append((product_name.capitalize(), price, quantity))
                    product_catalog[product_name] = (price, stock - quantity)
                else:
                    print(f"Not enough stock for {product_name}. Only {stock} available.")
            else:
                print(f"Sorry, {product_name.capitalize()} is out of stock.")
        else:
            print(f"{product_name.capitalize()} is not available in the catalog.")

    if purchased_items:
        print("\n*** Bill Summary ***")
        for item in purchased_items:
            print(f"{item[0]} - Rs.{item[1]} x {item[2]} = Rs.{item[1] * item[2]}")
        print(f"\nTotal Amount: Rs.{total_amount}\n")
    else:
        print("No items purchased.\n")

# Main function to control the store assistant's menu
def main():
    while True:
        print("Welcome to the Smart Grocery Store Assistant")
        print("1. View Products")
        print("2. Add/Update Product")
        print("3. Purchase Items")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_products()
        elif choice == '2':
            add_update_product()
        elif choice == '3':
            purchase_item()
        elif choice == '4':
            print("Thank you for using the Smart Grocery Store Assistant. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

# Run the assistant
if __name__ == "__main__":
    main()
