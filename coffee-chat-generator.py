
def main():
    selected_option = display_menu()
    print(selected_option)
    print("\n")

def display_menu():
    
    print("\nMenu:")
    print("1. Generate New Pairings")
    print("2. Add Members")
    print("3. Remove Members")
    print("4. Add Topic/Question")
    print("5. Remove Topic Question")
    print("\n")

    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                print("\n")
        except ValueError:
            print("Invalid input. Please enter a number.")
            print("\n")

def generator():
    pass


if __name__ == "__main__":
    main()