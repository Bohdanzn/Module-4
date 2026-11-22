def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command = parts[0].lower()
    args = parts[1:]
    return command, args
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Use: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Use: change <name> <new_phone>"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated with new phone number {new_phone}."
    else:
        return f"Contact {name} not found."
def show_contact(args, contacts):
    if len(args) != 1:
        return "Invalid command. Use: show <name>"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Contact {name} not found."
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
def main():
    contacts = {}
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)
        if command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_contact(args, contacts))
        elif command == "showall":
            print(show_all_contacts(contacts))
        elif command in ["exit", "close", "goodbye"]:
            print("Goodbye!")
            break
        else:
            print("Invalid command. Available commands: add, change, show, showall, exit.")
if __name__ == "__main__":
    main()
    