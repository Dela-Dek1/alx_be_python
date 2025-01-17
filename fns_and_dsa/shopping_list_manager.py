def display_menu():
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    shopping_list.append(item)
    if item:
        if item in shopping_list:
            print("'{item}' is already in the list.")
        else:
            shopping_list.append(item)
            print("'{item}' has been added to the list.")
    else:
        print("Invalid item name.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print("'{item}' has been removed from the list.")
    else:
        print("'{item}' not found in the list.")

def view_list(shopping_list):
    if shopping_list:
        print("\nCurrent Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print("{i}. {item}")
    else:
        print("\nThe shopping list is empty.")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Exitting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

