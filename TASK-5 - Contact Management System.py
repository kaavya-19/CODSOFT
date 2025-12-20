# CodSoft Python Internship Task
# Task Name: Contact Management System
# Author: Kaavya B M


scontacts = []

def show_menu():
    print("\n--- CONTACT MANAGEMENT SYSTEM ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- CONTACT LIST ---")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")

def search_contact():
    key = input("Enter name or phone number to search: ").lower()
    found = False

    for contact in contacts:
        if key in contact["name"].lower() or key in contact["phone"]:
            print("\nContact Found:")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True

    if not found:
        print("No matching contact found.")

def update_contact():
    view_contacts()
    try:
        choice = int(input("Enter contact number to update: "))
        contact = contacts[choice - 1]

        print("Leave blank to keep existing value")

        name = input(f"New name ({contact['name']}): ") or contact["name"]
        phone = input(f"New phone ({contact['phone']}): ") or contact["phone"]
        email = input(f"New email ({contact['email']}): ") or contact["email"]
        address = input(f"New address ({contact['address']}): ") or contact["address"]

        contact.update({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })

        print("Contact updated successfully!")

    except:
        print("Invalid selection!")

def delete_contact():
    view_contacts()
    try:
        choice = int(input("Enter contact number to delete: "))
        removed = contacts.pop(choice - 1)
        print(f"Deleted contact: {removed['name']}")
    except:
        print("Invalid selection!")

# Main Program Loop
while True:
    show_menu()
    option = input("Choose an option (1-6): ")

    if option == "1":
        add_contact()
    elif option == "2":
        view_contacts()
    elif option == "3":
        search_contact()
    elif option == "4":
        update_contact()
    elif option == "5":
        delete_contact()
    elif option == "6":
        print("Exiting Contact Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
