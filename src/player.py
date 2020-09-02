# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}'    