# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        

    def list_items(self):
        if len(self.items) == 0:
            print("There are no items in here.")
        else:
            for item in self.items:
                print(f"The room contains these items: {item.name}\n")

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)
