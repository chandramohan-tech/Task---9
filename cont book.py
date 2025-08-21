import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")

# Search for a contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"📌 Name: {name}")
        print(f"📞 Phone: {contacts[name]['phone']}")
        print(f"✉️ Email: {contacts[name]['email']}")
    else:
        print("❌ Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️ Contact '{name}' deleted.")
    else:
        print("❌ Contact not found.")

# Display all contacts
def display_contacts(contacts):
    if not contacts:
        print("import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")

# Search for a contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"📌 Name: {name}")
        print(f"📞 Phone: {contacts[name]['phone']}")
        print(f"✉️ Email: {contacts[name]['email']}")
    else:
        print("❌ Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️ Contact '{name}' deleted.")
    else:
        print("❌ Contact not found.")

# Display all contacts
def display_contacts(contacts):
    if not contacts:
        print("📭 No contacts available.")
        return
    print("\n--- All Contacts ---")
    for name, info in contacts.items():
        print(f"👤 {name} | 📞 {info['phone']} | ✉️ {info['email']}")
    print("--------------------\n")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\n📒 Contact Book Menu")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            display_contacts(contacts)
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main()
 No contacts available.")
        return
    print("\n--- All Contacts ---")
    for name, info in contacts.items():
        print(f" {name} |  {info['phone']} | ✉️ {info['email']}")
    print("--------------------\n")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\n Contact Book Menu")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            display_contacts(contacts)
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid choice, try again.")

if __name__ == "__main__":
    main()
