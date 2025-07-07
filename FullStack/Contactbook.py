def add_contact(contacts):
    """Adds a new contact to the contact list."""
    name = input("Enter contact name: ").strip()
    while True:
        phone = input("Enter phone number (10 digits): ").strip()
        if phone.isdigit() and len(phone) == 10:
            contacts.append({"name": name, "phone": phone})
            print(f"Contact '{name}' added successfully!")
            break
        else:
            print("Invalid phone number. Please enter a 10-digit numeric phone number.")

def view_contacts(contacts):
    """Displays all contacts in the contact list."""
    if not contacts:
        print("No contacts to display.")
        return

    print("\n--- All Contacts ---")
    for i, contact in enumerate(contacts):
        print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}")
    print("--------------------")

def search_contact(contacts):
    """Searches for a contact by name (case-insensitive)."""
    if not contacts:
        print("No contacts to search.")
        return

    search_name = input("Enter the name to search: ").strip().lower()
    found_contacts = [contact for contact in contacts if contact['name'].lower() == search_name]

    if found_contacts:
        print(f"\n--- Search Results for '{search_name}' ---")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
        print("------------------------------------------")
    else:
        print(f"No contact found with the name '{search_name}'.")

def contact_book_program():
    """Main function to run the contact book program."""
    contacts = []

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Exit")
        print("-------------------------")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    contact_book_program()

