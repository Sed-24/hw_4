
def main():
    print("Welcome to the assistant bot Fox!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
        except ValueError:
            print("Please specify the command")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif "hello" == command:
            print("How can I help you?")
        elif "add" in command:
            print(add_contact(*args))
        elif "change" in command:
            print(change_contact(*args))
        elif "phone" in command:
            print(show_phone(*args))
        elif "all" in command:
            print(show_all())
        else:
            print("Invalid command.")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(*add):
    try:
        if add[0] in contact:
            return "The contact already exists"
        else:
            contact[add[0]] = add[1]
            return "Contact added."
    except IndexError:
        return "Contact is not specified"


def change_contact(*change):
    try:
        if change[0] in contact:
            contact[change[0]] = change[1]
            return "Contact updated."
        else:
            return "Contact not found"

    except IndexError:
        return "Contact is not specified"


def show_phone(*phone):
    try:
        if phone[0] in contact:
            return contact[phone[0]]
        else:
            return "Contact not found"

    except IndexError:
        return "Contact is not specified"


def show_all():
    if len(contact) > 0:
        return contact
    return 'The phone book is empty'


if __name__ == "__main__":
    contact = {}
    main()
