import random

# Define dictionary for team members
team_members = {}

# Define dictionary for topics/questions

topic_questions = {}

def main():
    # Display a text menu and get user selection
    selected_option = display_menu()
    
    if selected_option == 1:
        print(selected_option)
    
    elif selected_option == 2:
        pass

    elif selected_option == 3:
        pass

    elif selected_option == 4:
        pass

    elif selected_option ==5:
        pass

    elif selected_option ==6:
        quit()

    print("\n")

def display_menu():
    
    print("\nMenu:")
    print("1. Generate New Pairings")
    print("2. Add Members")
    print("3. Remove Members")
    print("4. Add Topic Questions")
    print("5. Remove Topic Question")
    print("6. Quit Application")
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