phonebook = {}

while True:
    print("\nPhonebook Menu")
    print("1. Add")
    print("2. View")
    print("3. Delete")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":  # Add a new contact
        name = input("Enter the name: ").strip()
        phone = input("Enter the phone number: ").strip()
        if name and phone:
            phonebook[name] = phone
            print(f"Added: {name} - {phone}")
        else:
            print("Name and phone number cannot be empty.")
    
    elif choice == "2":  # View all contacts
        if phonebook:
            print("\nPhonebook Entries:")
            for name, phone in phonebook.items():
                print(f"{name}: {phone}")
        else:
            print("Phonebook is empty.")
    
    elif choice == "3":  # Delete a contact
        if phonebook:
            name = input("Enter the name to delete: ").strip()
            if name in phonebook:
                del phonebook[name]
                print(f"{name} has been deleted.")
            else:
                print(f"{name} not found in the phonebook.")
        else:
            print("Phonebook is empty. Nothing to delete.")
    
    elif choice == "4":  # Exit the program
        print("Exiting the Phonebook. Goodbye!")
        break
    
    else:  # Invalid input
        print("Invalid choice. Please try again.")
