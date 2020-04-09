from room import Room
from player import Player

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
    print(f"{player.current_room.description}")
    # * Waits for user input and decides what to do.
    user = input("Where would you like to go? [n]orth [e]ast [s]outh [w]est [q]uit \n").lower()
    # If the user enters "q", quit the game.
    if user == "q":
        print("Thanks for playing!")
        exit()
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif user == "n":
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
        # Print an error message if the movement isn't allowed.
        else:
            print("Sorry can't go in that direction!")
        
    elif user == "e":
        if player.current_room.e_to != None:
            player.current_room = player.current_room.e_to

        else:
            print("Sorry can't go in that direction!")

    elif user == "s":
        if player.current_room.s_to != None:
            player.current_room = player.current_room.s_to

        else:
            print("Sorry can't go in that direction!")

    elif user == "w":
        if player.current_room.w_to != None:
            player.current_room = player.current_room.w_to

        else:
            print("Sorry can't go in that direction!")

