# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, room, name, inventory):
        self.room = room
        self.name = name
        self.inventory = inventory

    def where_am_i(self):
        print(f"{self.name}, your current room: {self.room.name}")
        print(f"{self.room.description}")

    def change_room(self, direction):
        new_room = getattr(self.room, f"{direction}_to")
        if new_room is not None:
            self.room = new_room
        else:
            print("The passage is blocked....")

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        print(f"You have added {item.name} to your inventory")
        print(f"Your current inventory: {[inventory.name for inventory in self.inventory]}")
        for items in self.inventory:
            if items.name == item.name:
                self.room.remove_item(item=items)

    def remove_item_inventory(self, item):
        print(f"this is the item: {item}")
        print(f"You have removed {item} from your inventory")
        for i in self.inventory:
            if i.name.lower() == item:
                self.inventory.remove(i)

    def __str__(self):
        return f"{self.name} {self.room}"
