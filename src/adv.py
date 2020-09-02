from room import Room

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

location = room["outside"]      

while location == room["outside"]:
    print(room["outside"])
    selection = input("Please select a direction from the following: [n] >>>")
    try:
        if selection == 'n':
            print(room["foyer"])
            location = room["foyer"]
    except ValueError:
        print("please select a valid direction: [n]")

while location == room["foyer"]:
    selection = input("Please select a direction from the following: [n,s,w] >>>")
    try:
        if selection == 'n':
            print(room["overlook"])
            location = room["overlook"]
        elif selection == 's':
            print(room["outside"])
            location = room["outside"]
        elif selection == 'w':
            print(room["narrow"])
            location = room["narrow"]
    except ValueError:
        print("please select a valid direction: [n,s,w]")

while location == room["overlook"]:
    selection = input("Please select a direction from the following: [s] >>>")
    try:
        if selection == 's':
            print(room["foyer"])
            location = room["foyer"]
    except ValueError:
        print("please select a valid direction: [s]")

while location == room["narrow"]:
    selection = input("Please select a direction from the following: [n] >>>")
    try:
        if selection == 'n':
            print(room["treasure"])
            location = room["treasure"]
        elif selection == 'w':
            print(room["foyer"])
            location = room["foyer"]
    except ValueError:
        print("please select a valid direction: [n,w]")

while location == room["treasure"]:
    try:
        if selection == 's':
            print(room["narrow"])
            location = room["narrow"]
    except ValueError:
        print("please select a valid direction: [s]")