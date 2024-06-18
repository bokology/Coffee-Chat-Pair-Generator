import random
import string
import csv

# Define dictionary for team members
team_members = {}

# Set number of topics to assign to pairings
NUM_TOPICS = int(5)

MENU_STRING = """
    1. Generate New Pairings
    2. Add Members
    3. Remove Members
    4. Add Topics
    5. View Topics
    6. View Members
    7. Quit Application
"""

def main():
    # Loop the menu until user opts to quit.
    while True:
        print(MENU_STRING)
        try:
            selected_option = int(input("\nEnter your choice (1-7): "))            
            # Check if user input is within range of valid numbers.
            if 1 <= selected_option <= 7:
                # Generate random pairs and random topic assignments.
                if selected_option == 1:
                    pairings_output = generate_pairings()
                    topics = retrieve_topics()
                    # Assign 5 topics for each generated pairs or trio    
                    assign_topics_to_pairs(pairings_output, topics)                   
                # Call the add member function
                elif selected_option == 2:
                    add_member_loop()
                # Call the remove member function
                elif selected_option == 3:
                    read_members_from_csv()
                    target_tag = input("\nPlease input user tag of member to be removed: ")
                    remove_members(target_tag)
                # Call add topics function. Adds to an existing list if it already exists.
                elif selected_option == 4:
                    topics = retrieve_topics()
                    add_topics(topics)
                # View saved topics
                elif selected_option == 5:
                    topic_questions = retrieve_topics()
                    view_topics(topic_questions)
                # Display list of team members. This is read from a file.
                elif selected_option == 6:
                    read_members_from_csv()
                    for tag, details in team_members.items():
                        print(f"Tag: {tag} | {details['first_name']} {details['last_name']}")
                    print("---------------------\n")
                # Give the user the option to quit.
                elif selected_option == 7:
                    print("")
                    break                
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_pairings():
    # Check members list file
    read_members_from_csv()
    members = list(team_members.items())
    # Shuffle the list randomly
    random.shuffle(members)
    # Pair members
    pairings = []
    for i in range(0, len(members) - 1, 2):
        pairings.append((members[i], members[i + 1]))
    # If there is an odd number of members, create a three-way pairing (trio)
    if len(members) % 2 != 0:
        # Check if the pairings are not empty
        if len(pairings) > 0:
            # If there is at least one pair, remove the last pair
            last_pair = pairings.pop()
            # Append the last member to the last pair, making them a trio.
            last_pair = (*last_pair, members[-1])
            # Append the new trio to the list of pairings
            pairings.append(last_pair)
        else:
            pairings.append((members[-3], members[-2], members[-1]))
    return pairings

def assign_topics_to_pairs(pairings_output, topics):
    for pair in pairings_output:
        # Pick random topics from the file
        random_topics = random.sample(topics, NUM_TOPICS)
        if len(pair)  == 2:
                print(f"Pair: {pair[0][1]['first_name']} {pair[0][1]['last_name']} "
                    f"and {pair[1][1]['first_name']} {pair[1][1]['last_name']}")
        elif len(pair) == 3:
            print(f"Trio: {pair[0][1]['first_name']} {pair[0][1]['last_name']}, "
                    f"{pair[1][1]['first_name']} {pair[1][1]['last_name']}, and "
                    f"{pair[2][1]['first_name']} {pair[2][1]['last_name']}")
        print("Assigned Topics:")
        for topic in random_topics:
            print(f"- {topic}")
        print("---------------------\n")

def add_member_loop():
    # Get existing member list from file
    read_members_from_csv()
    while True:
        first_name = input("Enter first name (or type 'quit' to stop): ")
        if first_name.strip().lower() == 'quit':
            break
        last_name = input("Enter last name: ")
        # Generate unique identifier for newly enrolled member
        tag = generate_unique_tag()
        team_members[tag] = {'first_name': first_name, 'last_name': last_name}
        print(f"Added member {first_name} {last_name} with tag {tag}.")
        # Write back newly enrolled member details to file
        write_members_to_csv()

def read_members_from_csv(filename='team_members.csv'):
    # Retrieve member list from csv file. If file is not found we work with an empty list.
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    tag, first_name, last_name = row
                    team_members[tag] = {'first_name': first_name, 'last_name': last_name}
    except FileNotFoundError:
        print("CSV file not found. Starting with an empty team members list.")

def write_members_to_csv(filename='team_members.csv'):
    # Write back newly enrolled names to members file
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for tag, details in team_members.items():
            writer.writerow([tag, details['first_name'], details['last_name']])
    print("Team members saved to CSV.")

def remove_members(tag):
    if tag in team_members:
        del team_members[tag]
        print(f"Removed member with tag {tag}.")
        write_members_to_csv()
    else:
        print(f"No member found with tag {tag}.")

def generate_unique_tag():
    # Random alphanumeric tag. Makes sure generated tags are unique.
    while True:
        tag = ''.join(random.choices(string.digits, k=3))
        if tag not in team_members:
            return tag

def retrieve_topics(filename='topics.txt'):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            topics = file.readlines()
        topic_list = [topic.strip() for topic in topics]
        return topic_list
    except FileNotFoundError:
        print("Warning! Topic file not found. Please add topics using the menu.")
        return[]

def add_topics(topics):
    while True:
        new_topic = input("Enter a new topic (or type 'quit' to go back to the menu.): ")
        if new_topic.strip().lower() == 'quit':
           break
        topics.append(new_topic)
        print(f"Added topic: {new_topic}")
    write_topics_to_file(topics)
 
def write_topics_to_file(topics, filename='topics.txt'):
    with open(filename, mode='w', encoding='utf-8') as file:
        for topic in topics:
            file.write(f"{topic}\n")
    print("Topics saved to file.")

def view_topics(topics):
    for topic in topics:
        print(topic)

if __name__ == "__main__":
    main()