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

room['outside'].n_to = room['foyer'] # == Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""")
room['foyer'].s_to = room['outside'] # == Room("Outside Cave Entrance","North of you, the cave mount beckons")
room['foyer'].n_to = room['overlook'] 
room['foyer'].e_to = room['narrow'] # == Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""")
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

#Listens for input of name
name = input("Welcome traveler. What is your name?: ") or 'Link'

#Defaults current_room attr in `Player` class to outside room
player = Player(name, room['outside'])

#prints name and description from current_room
print(f"{player.current_room.name}") # == Room("Outside Cave Entrance","North of you, the cave mount beckons"); Outside Cave Entrance == name
print(f"{player.current_room.description}") # == Room("Outside Cave Entrance","North of you, the cave mount beckons"); North of you, the cave mount beckons == description

def new_location():
    print(player.current_room)

def wrong_move():
    print("Invalid move try again.")

#sets selection to an empty string
selection = ''

print('\n current room', player.current_room)
print('-------------------------------------------')
print('\n',  getattr(room['outside'], 'n_to'))
print('-------------------------------------------')
print('\n test 2', room['outside'].n_to)
print('-------------------------------------------')
print('\n current room.n_to', player.current_room.n_to)
print('-------------------------------------------')

while selection != 'q': # while selection input isn't `q` listen for more inputs
    selection = input("Please select a direction from the following: [n,s,e,w] >>> ")
    if selection == 'n': #if selection is `n`, `try` to set `current_room` attr to be `.n_to` attr in the Room object.
        try:
            player.current_room = player.current_room.n_to
            new_location()
        except AttributeError: # if current_room attr doesn't contain `.n_to` attr in the Room object run `wrong_move` function.
            wrong_move()
    elif selection == 's':
        try:
            player.current_room = player.current_room.s_to
            new_location()
        except AttributeError:
            wrong_move()
    elif selection == 'e':
        try:
            player.current_room = player.current_room.e_to
            new_location()
        except AttributeError:
            wrong_move()
    elif selection == 'w':
        try:
            player.current_room = player.current_room.w_to
            new_location()
        except AttributeError:
            wrong_move()
    elif selection == 'q':
        print("Closing the game.")
    else:
        print("Not a valid direction.")

