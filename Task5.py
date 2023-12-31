# Initialize an empty contact list
contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contact = {
        "Name": name,
        "Phone Number": phone,
        "Email": email,
        "Address": address,
    }
    
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    
    for idx, contact in enumerate(contacts, 1):
        print(f"Contact {idx}:")
        for key, value in contact.items():
            print(f"{key}: {value}")
        print("\n")

def search_contact(query):
    results = []
    for contact in contacts:
        if query.lower() in contact["Name"].lower() or query in contact["Phone Number"]:
            results.append(contact)
    
    if not results:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for idx, contact in enumerate(results, 1):
            print(f"Contact {idx}:")
            for key, value in contact.items():
                print(f"{key}: {value}")
            print("\n")

def update_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        choice = int(input("Enter the contact number to update: "))
        if 1 <= choice <= len(contacts):
            contact = contacts[choice - 1]
            for key in contact.keys():
                new_value = input(f"Enter new {key}: ")
                contact[key] = new_value
            print("Contact updated successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        choice = int(input("Enter the contact number to delete: "))
        if 1 <= choice <= len(contacts):
            deleted_contact = contacts.pop(choice - 1)
            print(f"Contact '{deleted_contact['Name']}' deleted successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.")

# Main loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        query = input("Enter name or phone number to search: ")
        search_contact(query)
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
