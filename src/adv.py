from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Add items
shovel = Item("Shovel", "Can use to dig holes or bury items.")
lamp = Item("Lamp", "Will light your pathway.")
binoculars = Item("Binoculars", "Used to see something far away.")
pen = Item("Pen", "Helpful for writing things down.")
money = Item("Gold Coins", "I'm rich!")

# Add items to rooms
room["outside"].items.append(shovel)
room["foyer"].items.append(lamp)
room["overlook"].items.append(binoculars)
room["narrow"].items.append(pen)
room["treasure"].items.append(money)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Please enter your name: "), room["outside"])
# Write a loop that:

while True:
    # * Prints the current room name
    print(f"You are currently in {player.current_room.name}")
    # * Prints the current description (the textwrap module might be useful here).
    print(f"{player.current_room.description}\n")
    # * Waits for user input and decides what to do.
    user = input("What would you like to do? To travel to different rooms:\n [n] - North [e] - East [s] - South [w] - West\n [i] - Inventory - To view your inventory\n [list items] - to view items in the room \n [take item] - to pick up item \n [drop item] - to drop item\n [q] - Quit \n --> ").lower()
    item_input = user.split()
    # print(len(item_input), item_input[0])
    # If the user enters "q", quit the game.
    if len(item_input) == 1:
        if item_input[0] == "q":
            print(f"Thanks for playing {player.name}!")
            exit()
    
    # If the user enters a cardinal direction, attempt to move to the room there.
        elif item_input[0] == "n":
            if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to
        # Print an error message if the movement isn't allowed.
            else:
                print("Sorry can't go in that direction!")
        
        elif item_input[0] == "e":
            if player.current_room.e_to != None:
                player.current_room = player.current_room.e_to

            else:
                print("Sorry can't go in that direction!")

        elif item_input[0] == "s":
            if player.current_room.s_to != None:
                player.current_room = player.current_room.s_to

            else:
                print("Sorry can't go in that direction!")

        elif item_input[0] == "w":
            if player.current_room.w_to != None:
                player.current_room = player.current_room.w_to

        elif item_input[0] == "i":
            player.player_items()

        elif item_input[0] != "n" or item_input[0] != "e" or item_input[0] != "s" or item_input[0] != "w" or item_input[0] != "i" :
            print("Please use a valid entry!\n")

        else:
            print("Sorry can't go in that direction!")


    elif len(item_input) == 2:
        if item_input[0] == "list":
            player.current_room.list_items()

        elif item_input[0] == "take":
            player.take_item(player.current_room.items[0])
            player.current_room.remove_item(player.current_room.items[0])

        elif item_input[0] == "drop":
            player.current_room.add_item(player.items[0])
            player.drop_item(player.items[0])

        elif item_input[0] != "list" or item_input[0] != "take" or item_input[0] != "drop":
            print("Please use a valid entry!\n")
            
    else:
        print("Oops incorrect entry!")



