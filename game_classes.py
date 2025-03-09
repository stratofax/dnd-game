import os
import random
import time
from typing import Dict, List, Optional, Tuple

class Item:
    def __init__(self, name: str, description: str, power: int = 0):
        self.name = name
        self.description = description
        self.power = power  # Power value for combat

    def __str__(self) -> str:
        return self.name

class Room:
    def __init__(self, name: str, description: str, image_file: Optional[str] = None):
        self.name = name
        self.description = description
        self.image_file = image_file
        self.items = []
        self.connections = {}  # direction -> room_id

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> Optional[Item]:
        for i, item in enumerate(self.items):
            if item.name.lower() == item_name.lower():
                return self.items.pop(i)
        return None

    def add_connection(self, direction: str, room_id: str) -> None:
        self.connections[direction.lower()] = room_id

    def get_connection(self, direction: str) -> Optional[str]:
        return self.connections.get(direction.lower())

    def display(self) -> None:
        print(f"\n=== {self.name} ===")
        print(self.description)

        if self.image_file and os.path.exists(self.image_file):
            print(f"[Image: {self.image_file}]")
            # In a real game, you would display the image here

        if self.items:
            print("\nYou see:")
            for item in self.items:
                print(f"- {item.name}: {item.description}")

        print("\nPossible exits:")
        for direction in self.connections:
            print(f"- {direction.capitalize()}")

class Player:
    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.inventory = []
        self.current_room_id = "start"  # Default starting room

    def add_to_inventory(self, item: Item) -> None:
        self.inventory.append(item)
        print(f"Added {item.name} to your inventory.")

    def remove_from_inventory(self, item_name: str) -> Optional[Item]:
        for i, item in enumerate(self.inventory):
            if item.name.lower() == item_name.lower():
                return self.inventory.pop(i)
        return None

    def get_total_power(self) -> int:
        return sum(item.power for item in self.inventory)

    def display_inventory(self) -> None:
        if not self.inventory:
            print("Your inventory is empty.")
            return

        print("\n=== Inventory ===")
        for item in self.inventory:
            print(f"- {item.name}: {item.description} (Power: {item.power})")
        print(f"Total Power: {self.get_total_power()}")
        print(f"Health: {self.health}")
