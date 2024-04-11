# Noelle Bishop
# Text-based game in which the player moves through rooms, collects items, and wins or loses.

def show_instructions():
    """Displays game premise and instructions."""
    print("                   Masquerade Battle in the Ballroom!\n"
          "                                 * * *\n"
          "          Collect 6 items throughout the mansion to win the game\n"
          "                   or be out-danced by your evil clone.")
    print('*', '-' * 72, '*')
    print("- Move commands: type 'south', 'north', 'east', or 'west'\n"
          "- Grab item command: type 'get [item name]' (e.g., get fancy hat)\n"
          "- Type 'help' to see the instructions again.\n"
          "- Type 'exit' to close the game.\n")


def player_status(rooms, current_room, inventory_list):
    """Displays player's current location, inventory, and items they can get."""
    print('-' * 25)
    print('You are in the {}!'.format(current_room))
    print('Inventory:', inventory_list,)

    # Conditional branches below check first if an item exists in current_room.
    # Then, based on the singular or plural nature of each item, the 'You see' message adjusts for grammar correctness.
    if 'item' in rooms[current_room].keys():
        if (rooms[current_room]['item'] == 'fancy hat' or
           rooms[current_room]['item'] == 'necklace' or
           rooms[current_room]['item'] == 'ballroom gown' or
           rooms[current_room]['item'] == 'mask'):
            print('\n- You see a {}.'.format(rooms[current_room]['item']))
        elif (rooms[current_room]['item'] == 'platform heels' or
              rooms[current_room]['item'] == 'flowers'):
            print('\n- You see {}.'.format(rooms[current_room]['item']))
        elif rooms[current_room]['item'] == 'your evil clone!':
            print('\n- You see {}'.format(rooms[current_room]['item']))
    print('-' * 25)


def main_game():
    """The main gameplay happens here in a while loop, using a dict to switch between rooms and get items."""
    # Start player in the Conservatory, initialize the inventory list and num_items variable, and display instructions.
    current_room = 'Conservatory'
    inventory_list = []
    num_items = 0
    show_instructions()

    # The dictionary links a room to other rooms and items.
    # Directions are lowercase for easier input validation in main gameplay.
    rooms = {
        'Conservatory': {'south': 'Study', 'west': 'Sunroom', 'north': 'Home Theater', 'east': 'Indoor Pool'},
        'Study': {'north': 'Conservatory', 'east': 'Gym', 'item': 'fancy hat'},
        'Gym': {'west': 'Study', 'item': 'platform heels'},
        'Sunroom': {'east': 'Conservatory', 'item': 'flowers'},
        'Home Theater': {'south': 'Conservatory', 'east': 'Walk-in Closet', 'item': 'necklace'},
        'Walk-in Closet': {'west': 'Home Theater', 'item': 'ballroom gown'},
        'Indoor Pool': {'west': 'Conservatory', 'north': 'Ballroom', 'item': 'mask'},
        'Ballroom': {'south': 'Indoor Pool', 'item': 'your evil clone!'}
    }

    '''
    The while loop supports continuous move/get item commands and breaks when player types 'exit' or wins the game.
    Main movement occurs on lines 79 - 80, and multiple if/else branches validate input.
    Line 79 checks if player_move exists as a value of the current_room key.
    Line 80 then assigns current_room as the value of the player_move key within the value of the current_room key.
    Ex: player_move = 'east' in 'Conservatory' then pulls the value of the 'east': 'Indoor Pool' pair in 'Conservatory'.
    This same functionality is used for item grabbing on Lines 94-95.
    '''
    while current_room != 'exit':  # Loop makes the game operate as long as 'exit' is not entered.
        player_status(rooms, current_room, inventory_list)
        player_move = input('Enter your command: \n> ').lower()  # lower() function ensures input validity.
        player_move = player_move.replace('go ', '')  # Validates input if user types 'go [direction]'.
        player_move = player_move.replace('a ', '')  # Validates input if user types 'get a [item]'.

        if player_move == 'help':
            show_instructions()
        elif player_move == 'exit':
            current_room = 'exit'  # This breaks the loop and ends the game.
        else:  # This is where player movement and item grabbing occurs.
            if player_move in rooms[current_room]:  # Checks if player_move is a valid command from the current room.
                current_room = rooms[current_room][player_move]  # Assigns new current_room from rooms key-value pair.
                if current_room == 'Ballroom':  # Villain room.
                    player_status(rooms, current_room, inventory_list)  # Displays room status before win/lose message.
                    if num_items == 6:  # Condition to win the game.
                        print("Congratulations!!! You collected all 6 items and\n"
                              "embarrassed your clone in a ballroom dance-off. GAME WON")
                        print('-' * 25)
                        current_room = 'exit'  # This breaks the loop and ends the game.
                    else:  # Player loses the game if num_items does not equal 6.
                        print("Uh oh... You arrived at the ballroom without all 6 items.\n"
                              "Your clone put your dance moves to shame. GAME OVER")
                        print('-' * 25)
                        current_room = 'exit'  # This breaks the loop and ends the game.
            elif 'item' in rooms[current_room].keys():  # Only activates if an item is in current_room.
                if (player_move == f"get {rooms[current_room]['item']}" or
                   player_move == f"take {rooms[current_room]['item']}"):  # Player must type the item in current_room.
                    print('-' * 25)
                    print('You added the {} to your inventory.'.format(rooms[current_room]['item']))
                    print("That'll come in handy!")
                    inventory_list.append(rooms[current_room]['item'])  # Adds the item to the inventory.
                    num_items += 1  # Increments num_items to reflect the added item.
                    rooms[current_room].pop('item')  # Removes the item from the dictionary.
                else:
                    '''
                    The if statement below lets a player leave and come back to a room with an item without
                    grabbing the item. Otherwise, they'd get the "nothing happened" message below until
                    they grabbed the item. This gives them the freedom to explore the game at their own pace.
                    '''
                    if player_move in rooms[current_room]:
                        current_room = rooms[current_room][player_move]
                    else:  # Activates if player neither gets an item nor goes a valid direction.
                        print('-' * 25)
                        print("Hmm.. nothing happened. Try something else or type 'help' to see the instructions.")
            else:  # Activates if player does not go a valid direction.
                print('-' * 25)
                print("You ran into a wall. Ouch! Try something else or type 'help' to see the instructions.")
    input('Thanks for playing! See you later!')  # Requires 'enter' before program closes, so closing message is seen.


main_game()  # Call the main_game function to start the game.
