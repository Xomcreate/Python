
# sales app storage in dictionary


def calculate_total_sales():
    print("Welcome to the Sales APP")
    print("Enter sales quantity for fixed items. Type 'done' to finish.\n")

    # Fixed items and their prices
    items = {
        "fried fish": 700,
        "bum short": 10000,
        "head band": 500,
        "Bags": 4400
    }

    total_sales = 0  # To store the total sales amount
    sales_entries = []  # To store details of each sale

    print("Available Items and Prices:")
    for item, price in items.items():
        print(f"- {item}: ${price:.2f}")
    print()

    while True:
        # Get the item name
        item = input("Enter item name (or type 'done' to finish): ").capitalize()
        if item.lower() == 'done':
            break  # Exit the loop

        if item not in items:
            print(f"{item} is not in the list of available items. Please try again.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity sold for {item}: "))
            price = items[item]
            total_cost = quantity * price  # Calculate total cost for the item
            sales_entries.append({'item': item, 'quantity': quantity, 'price': price, 'total_cost': total_cost})
            total_sales += total_cost
            print(f"Total cost for {item}: ${total_cost:.2f}\n")
        except ValueError:
            print("Invalid input! Please enter a number for quantity.\n")

    # Display the summary of sales
    print("\nSales Summary:")
    print("-" * 40)
    for entry in sales_entries:
        print(f"Item: {entry['item']}, Quantity: {entry['quantity']}, "
              f"Price: ${entry['price']:.2f}, Total Cost: ${entry['total_cost']:.2f}")
    print("-" * 40)
    print(f"Total Sales for the Day: ${total_sales:.2f}")
    print("Thank you for using the Sales  App!")


# Run the function
calculate_total_sales()
