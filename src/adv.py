from room import Room
from player import Player
from item import Item

# Declare all the rooms
from typing import List

sword = Item("Sword", "A blade once belonging to an over eager knight...")
lamp = Item("Lamp", "The path ahead is scary and dark. That is why we must find the light...")
key = Item("Key", "This key may be important later on...")
potion = Item("Potion", "The liquid swirls mysteriously, will this help or harm...")
light_armour = Item("Light_Armour", "The material is flexible and quite to move in, but offers little protection...")
heavy_armour = Item("Heavy_Armour", "A strong and sturdy suit of a knight, but loud and clunky...")
amulet = Item("Amulet", "A gift from the gods, or a curse to whomever bears the weight...")
room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", [lamp]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [light_armour, sword]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [heavy_armour, key]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [potion]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [amulet]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
directions = ('n', 's', 'e', 'w')
controls = ['Player Commands',
            'n = North',
            's = South',
            'e = East',
            'w = West',
            'take [ITEM NAME] = choose a room item to take',
            'drop [ITEM NAME] = choose an item to drop from player inventory'
            'q = Quit']
# Make a new player object that is currently in the 'outside' room.
my_player = Player(room['outside'], 'Joe', [])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def move_list():
    for move in controls:
        print(f"{move}")


def check_input_type(lst):
    return list(lst.split(" "))


move_list()
print('\n')
print(f"Our hero {my_player.name} approaches the {my_player.room.name}, {my_player.room.description}, will you enter...")
print("\n")
print("Available room items...")
for item in my_player.room.items:
    print(f"{item.name}: {item.description}")
while True:
    print('\n')
    player_input = input(f"Please choose your action... \n").lower()
    if player_input == 'q':
        quit()
    elif player_input:
        res = len(player_input.split())
        if res == 1:
            my_player.change_room(player_input)
            print(f"{my_player.name}, you are in {my_player.room.name}, {my_player.room.description}")
            print("\n")
            for item in my_player.room.items:
                print(f"{item.name}: {item.description}")
        else:
            player_cmd = check_input_type(player_input)
            check_for_item = my_player.room.is_item_here(player_cmd[1])
            if player_cmd[0] == 'take':
                pick_item_up = my_player.add_item_to_inventory(check_for_item)
            else:
                # TODO work on dropping item logic
                print(f"you are dropping {player_cmd[1]}")

