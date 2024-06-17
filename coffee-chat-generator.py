import random
import string
import csv

# Define dictionary for team members
team_members = {}

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
                    # Assign 3 topics for each generated pairs or trio    
                    for pair in pairings_output:
                        # Pick random topics from the file
                        random_topics = random.sample(topics, 3)
                        if len(pair)  == 2:
                              print(f"Pair: {pair[0][1]['first_name']} {pair[0][1]['last_name']} and {pair[1][1]['first_name']} {pair[1][1]['last_name']}")
                        elif len(pair) == 3:
                            print(f"Trio: {pair[0][1]['first_name']} {pair[0][1]['last_name']}, {pair[1][1]['first_name']} {pair[1][1]['last_name']}, and {pair[2][1]['first_name']} {pair[2][1]['last_name']}")
                        print("Assigned Topics:")
                        for topic in random_topics:
                            print(f"- {topic}")
                        print("---------------------\n")           
                
                elif selected_option == 2:
                    add_member_loop()
                
                elif selected_option == 3:
                    remove_members()
                
                elif selected_option == 4:
                    topics = retrieve_topics()
                    add_topics(topics)
                
                elif selected_option == 5:
                    topic_questions = retrieve_topics()
                    view_topics(topic_questions)
                
                elif selected_option == 6:
                    read_members_from_csv()
                    for tag, details in team_members.items():
                        print(f"Tag: {tag} | First Name: {details['first_name']} | Last Name: {details['last_name']}")
                    print("---------------------\n")

                elif selected_option == 7:
                    print("")
                    break
                
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_pairings():
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

def add_members(first_name, last_name):
    # Call a function to assign unique tag then let user enter and first and last name.
    tag = generate_unique_tag()
    team_members[tag] = {'first_name': first_name, 'last_name': last_name}
    print(f"{first_name} {last_name} has been added.")

def add_member_loop():
    read_members_from_csv()
    while True:
        first_name = input("Enter first name (or type 'quit' to stop): ")
        if first_name.strip().lower() == 'quit':
            break
        last_name = input("Enter last name: ")
        tag = generate_unique_tag()
        team_members[tag] = {'first_name': first_name, 'last_name': last_name}
        print(f"Added member {first_name} {last_name} with tag {tag}.")
        write_members_to_csv()

def read_members_from_csv(filename='team_members.csv'):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    tag, first_name, last_name = row
                    team_members[tag] = {'first_name': first_name, 'last_name': last_name}
        print("Team members loaded from CSV.\n")
    except FileNotFoundError:
        print("CSV file not found. Starting with an empty team members list.")

def write_members_to_csv(filename='team_members.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for tag, details in team_members.items():
            writer.writerow([tag, details['first_name'], details['last_name']])
    print("Team members saved to CSV.")

def remove_members():
    pass

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