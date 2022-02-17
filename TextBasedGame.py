# Anthony Vigil
# Project Two

# Define Instructions
def show_instructions():
    # print a main menu and the commands
   print("Bounty Hunter Text Game")
   print("Collect 6 items to win the game, or be defeated by Drudkh.")
   print("Move commands: Go South, Go North, Go East, Go West, or Exit")
   print("Add to Inventory: get 'item name'\n")

# Define Main function
def main():
    show_instructions()
    areas = {'HF-18 Entrance': {'South': 'Mechanic Area', 'North': 'Storage Area', 'East': 'Loading Area',
                                'West': 'Shield Control Room', 'item': None},
             'Mechanic Area': {'North': 'HF-18 Entrance', 'East': 'Fueling Area', 'item': 'Restraining Pod'},
             'Fueling Area': {'West': 'Mechanic Area', 'item': 'Armor'},
             'Launching Area': {'South': 'Loading Area', 'item': 'Drudkh'},
             'Storage Area': {'East': 'Control Room', 'South': 'HF-18 Entrance', 'item': 'Jetpack'},
             'Shield Control Room': {'East': 'HF-18 Entrance', 'item': 'Rifle-Blaster'},
             'Control Room': {'West': 'Storage Area', 'item': 'Helmet'},
             'Loading Area': {'West': 'HF-18 Entrance', 'North': 'Launching Area', 'item': 'Rockets'}
             }

# Starting room
    current_area = 'HF-18 Entrance'
# List to store collected items
    inventory = []

# Loop to simulate moves between areas based on the user input
    while True:
        # If current_room is Launch Area then breaking the loop
        if current_area == 'Launching Area':
            print("\nYou are in the", current_area)
            print("You see Drudkh!", )
            if len(inventory) == 6:
                print("\nCongratulations! You have collected all the items and defeated Drudkh")
            else:
                print("\nPEW PEW PEW...GAME OVER!")
            break

    # Printing current_area
        print("\nYou are in the", current_area)

    # Taking user opinion to pick the item or not
        if areas[current_area]['item'] != None:
            print("You see a", areas[current_area]['item'])
            decision = input("Get " + areas[current_area]['item'] + "?(Y/N): ").upper()
        # Validating user input
            while decision not in ['Y', 'N']:
                print("Invalid input. Try again")
                decision = input("Get " + areas[current_area]['item'] + "?(Y/N): ").upper()
            if decision == 'Y':
                inventory.append(areas[current_area]['item'])
                areas[current_area]['item'] = None
        else:
            print("Already collected item or nothing in this room")

    # Printing inventory
        print("Inventory:", inventory)

    # Taking user input for direction to move
        navigate = input("Direction to move? (East, West, North, South, or Exit): ").title()
        navigation = list(areas[current_area].keys())
        navigation.remove('item')

    # For user to exit if input in navigate
        if (navigate == 'Exit'):
            exit(0)

    # Validating direction
        while navigate not in navigation:
            print("Invalid direction from " + current_area + ". Try again")
            navigate = input("Direction to move? (East, West, North, South, or Exit): ").title()


    # Setting next_area
        next_area = areas[current_area][navigate]
        print("You have just moved to", next_area)
        print("------------------------------------------------")

    # Updating current_area
        current_area = next_area

# Printing end message
    print("\nThanks for playing the game. Hope you enjoyed it.")

# Calling main function
main()