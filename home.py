class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Contact added: {contact.name}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact}")

    def update_contact(self, contact_index, name, phone, email):
        if 0 <= contact_index < len(self.contacts):
            contact = self.contacts[contact_index]
            contact.name = name
            contact.phone = phone
            contact.email = email
            print(f"Contact updated: {contact.name}")
        else:
            print("Invalid contact index.")

    def delete_contact(self, contact_index):
        if 0 <= contact_index < len(self.contacts):
            removed_contact = self.contacts.pop(contact_index)
            print(f"Contact deleted: {removed_contact.name}")
        else:
            print("Invalid contact index.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Options:")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.view_contacts()
            contact_index = int(input("Enter the contact number to update: ")) - 1
            name = input("Enter new contact name: ")
            phone = input("Enter new contact phone: ")
            email = input("Enter new contact email: ")
            contact_book.update_contact(contact_index, name, phone, email)
        elif choice == '4':
            contact_book.view_contacts()
            contact_index = int(input("Enter the contact number to delete: ")) - 1
            contact_book.delete_contact(contact_index)
        elif choice == '5':
            print("Exiting the contact book app.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
