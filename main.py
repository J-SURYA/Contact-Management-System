from contact import Contact
from ContactManager import ContactManager
def main():
    manager = ContactManager()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            manager.addContact(contact)

        elif choice == "2":
            manager.displayContacts()

        elif choice == "3":
            name = input("Enter name to search: ")
            manager.searchContact(name)

        elif choice == "4":
            name = input("Enter name to update: ")
            manager.updateContact(name)

        elif choice == "5":
            name = input("Enter name to delete: ")
            manager.deleteContact(name)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()