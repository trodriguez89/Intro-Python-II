class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"You picked up {self.name}. Here's a description of it: {self.description}")

    def on_drop(self):
        print(f"You dropped {self.name}")