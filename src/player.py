# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def take_item(self, item):
        self.items.append(item)
        print(f"You picked up {item.name}\n")

    def drop_item(self, item):
        self.items.remove(item)
        print(f"You dropped {item.name}")

    def player_items(self):
        if len(self.items) == 0:
            print("You don't have any items!")
        else:
            for item in self.items:
                print(f"You currently have {item.name}, here is a brief description: {item.description}")
