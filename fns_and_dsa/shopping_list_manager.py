def display_menu(): 
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            item = input("Enter the item to add: ")
            if item in shopping_list:
                print(f"{item} is altready in the shopping list")
            else:
                shopping_list.append(item)

            elif choice == 2:
                item - input("Enter the item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                else:
                    print(f"{item} is not available in the shopping list")

            elif choice == 3:
                if len(shopping_list) != 0:
                    for item in shopping_list:
                        print(item)
                else:
                    print("Shopping list is empty")

            elif choice == 4:
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
