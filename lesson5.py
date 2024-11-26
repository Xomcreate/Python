#  sales order app stored in dictionary 


def sales_order_system():
    print("Welcome to the Sales Order System!\n")

    # Store items and their prices in separate dictionaries
    items = {
        "Apple": "Fruit",
        "Banana": "Fruit",
        "Orange": "Fruit",
        "Milk": "Dairy",
        "Bread": "Bakery",
        "Eggs": "Dairy",
        "Rice": "Grain"
    }
    prices = {
        "Apple": 0.50,
        "Banana": 0.30,
        "Orange": 0.40,
        "Milk": 1.50,
        "Bread": 2.00,
        "Eggs": 3.00,
        "Rice": 1.20
    }

    print("Available Items and Prices:")
    for item, price in prices.items():
        print(f"- {item}: ${price:.2f}")
    print()

    total_order = {}
    max_items = 4
    total_cost = 0

    for i in range(max_items):
        item = input(f"Enter item #{i+1} (or type 'done' to finish): ").capitalize()
        if item.lower() == "done":
            break

        if item not in prices:
            print(f"{item} is not available in the store. Please select a valid item.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity for {item}: "))
            if item in total_order:
                total_order[item] += quantity  # Add to existing quantity
            else:
                total_order[item] = quantity
            total_cost += prices[item] * quantity
            print(f"{item} added to order. Subtotal: ${total_cost:.2f}\n")
        except ValueError:
            print("Invalid quantity. Please enter a valid number.\n")

    # Display final order summary
    print("\nOrder Summary:")
    print("-" * 40)
    for item, quantity in total_order.items():
        item_cost = prices[item] * quantity
        print(f"Item: {item}, Quantity: {quantity}, Price: ${prices[item]:.2f}, Cost: ${item_cost:.2f}")
    print("-" * 40)
    print(f"Total Order Cost: ${total_cost:.2f}")
    print("Thank you for shopping with us!")

# Run the program
sales_order_system()
