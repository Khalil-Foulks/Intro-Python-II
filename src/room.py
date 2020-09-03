# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        room_string = f'\n Your Location: {self.name} \n Description: {self.description} \n'

        for i in self.items:
            room_string += f"\n Item: {i}. {i.description}"
        return room_string

        