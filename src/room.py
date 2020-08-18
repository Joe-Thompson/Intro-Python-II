# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def list_items(self):
        for i, items in enumerate(self.items):
            print(f"{i + 1}. {items.name}")

    def is_item_here(self, item):
        for i, items in enumerate(self.items):
            if str(items.name).lower() == item:
                return items
            else:
                print(f"{item} is not in this room")

    # TODO working on removing items from room
    def remove_item(self, item):
        print(f"this is the item: {item}")
        self.items.remove(item)

    def __str__(self):
        return f"{self.name}: {self.description}"
