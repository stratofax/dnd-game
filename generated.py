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

class Game:
    def __init__(self):
        self.rooms = {}
        self.player = None
        self.boss = None
        self.game_over = False
        self.required_items = 6  # Number of items needed to defeat the boss

    def add_room(self, room_id: str, room: Room) -> None:
        self.rooms[room_id] = room

    def create_boss(self, name: str, description: str, health: int, power: int) -> None:
        self.boss = {
            "name": name,
            "description": description,
            "health": health,
            "power": power
        }

    def initialize_game(self) -> None:
        # Create rooms
        entry = Room(
            "Castle Entrance", 
            "You stand before an ancient castle. The massive wooden doors are partially open, revealing darkness within.",
            "castle_entrance.jpg"
        )
        self.add_room("start", entry)

        main_hall = Room(
            "Main Hall", 
            "A vast hall with a high ceiling. Dusty chandeliers hang above, and tapestries line the walls.",
            "main_hall.jpg"
        )
        self.add_room("hall", main_hall)

        library = Room(
            "Library", 
            "Shelves upon shelves of ancient tomes. The air is thick with dust and the smell of old parchment.",
            "library.jpg"
        )
        self.add_room("library", library)

        armory = Room(
            "Armory", 
            "Weapons of various kinds line the walls. Most are rusted beyond use, but a few might still serve.",
            "armory.jpg"
        )
        self.add_room("armory", armory)

        kitchen = Room(
            "Kitchen", 
            "A large stone hearth dominates one wall. Pots and pans hang from hooks, and a large table sits in the center.",
            "kitchen.jpg"
        )
        self.add_room("kitchen", kitchen)

        dungeon = Room(
            "Dungeon", 
            "A damp, dark place with cells lining the walls. Water drips from the ceiling, and the air is cold.",
            "dungeon.jpg"
        )
        self.add_room("dungeon", dungeon)

        throne_room = Room(
            "Throne Room", 
            "A grand room with a throne on a raised dais. This is where the lord of the castle would sit in judgment.",
            "throne_room.jpg"
        )
        self.add_room("throne", throne_room)

        boss_chamber = Room(
            "Boss Chamber", 
            "A circular chamber with strange runes carved into the floor. The air crackles with dark energy.",
            "boss_chamber.jpg"
        )
        self.add_room("boss", boss_chamber)

        # Connect rooms
        entry.add_connection("north", "hall")

        main_hall.add_connection("south", "start")
        main_hall.add_connection("east", "library")
        main_hall.add_connection("west", "armory")
        main_hall.add_connection("north", "throne")
        main_hall.add_connection("down", "dungeon")

        library.add_connection("west", "hall")
        library.add_connection("north", "kitchen")

        armory.add_connection("east", "hall")

        kitchen.add_connection("south", "library")

        dungeon.add_connection("up", "hall")

        throne_room.add_connection("south", "hall")
        throne_room.add_connection("north", "boss")

        boss_chamber.add_connection("south", "throne")

        # Add items
        sword = Item("Sword", "A shining blade with ancient runes etched along its length.", 15)
        armory.add_item(sword)

        shield = Item("Shield", "A sturdy shield emblazoned with a dragon crest.", 10)
        armory.add_item(shield)

        spellbook = Item("Spellbook", "A tome containing powerful incantations of protection.", 12)
        library.add_item(spellbook)

        potion = Item("Potion", "A vial of glowing blue liquid that emanates magical energy.", 8)
        kitchen.add_item(potion)

        amulet = Item("Amulet", "A silver amulet with a ruby center that pulses with inner light.", 20)
        throne_room.add_item(amulet)

        dagger = Item("Dagger", "A small but deadly blade with an ornate hilt.", 5)
        dungeon.add_item(dagger)

        # Create boss
        self.create_boss(
            "Ancient Dragon", 
            "A massive dragon with scales as black as night. Its eyes glow with malevolence.",
            200,  # Health
            70    # Power (will be reduced by player's items)
        )

    def start(self) -> None:
        print("Welcome to the D&D Text Adventure!")
        player_name = input("What is your name, brave adventurer? ")
        self.player = Player(player_name)

        print(f"\nWelcome, {self.player.name}!")
        print("You've heard rumors of an ancient castle that contains powerful artifacts...")
        print("But beware, a terrible dragon has made its lair in the deepest chamber.")
        print("You must find six magical items to have any hope of defeating it.")
        print("\nCommands: go [direction], look, inventory, take [item], drop [item], quit")

        self.initialize_game()
        self.game_loop()

    def game_loop(self) -> None:
        while not self.game_over:
            current_room = self.rooms[self.player.current_room_id]
            current_room.display()

            command = input("\nWhat would you like to do? ").lower().strip()
            self.process_command(command)

    def process_command(self, command: str) -> None:
        parts = command.split()

        if not parts:
            print("Please enter a command.")
            return

        action = parts[0]

        if action == "quit":
            self.game_over = True
            print("Thanks for playing!")
            return

        if action == "look":
            return  # Room will be displayed again in the next loop iteration

        if action == "inventory":
            self.player.display_inventory()
            return

        if action == "go" and len(parts) > 1:
            direction = parts[1]
            self.move_player(direction)
            return

        if action == "take" and len(parts) > 1:
            item_name = " ".join(parts[1:])
            self.take_item(item_name)
            return

        if action == "drop" and len(parts) > 1:
            item_name = " ".join(parts[1:])
            self.drop_item(item_name)
            return

        print("I don't understand that command.")

    def move_player(self, direction: str) -> None:
        current_room = self.rooms[self.player.current_room_id]
        new_room_id = current_room.get_connection(direction)

        if not new_room_id:
            print(f"You can't go {direction} from here.")
            return

        self.player.current_room_id = new_room_id

        # Check if player entered boss room
        if new_room_id == "boss":
            self.check_boss_encounter()

    def take_item(self, item_name: str) -> None:
        current_room = self.rooms[self.player.current_room_id]
        item = current_room.remove_item(item_name)

        if not item:
            print(f"There is no {item_name} here.")
            return

        self.player.add_to_inventory(item)

    def drop_item(self, item_name: str) -> None:
        item = self.player.remove_from_inventory(item_name)

        if not item:
            print(f"You don't have {item_name} in your inventory.")
            return

        current_room = self.rooms[self.player.current_room_id]
        current_room.add_item(item)
        print(f"You dropped {item.name}.")

    def check_boss_encounter(self) -> None:
        if len(self.player.inventory) < self.required_items:
            print("\nAs you enter the chamber, the ancient dragon rises before you!")
            print("You realize you are ill-equipped to face such a powerful foe.")
            print("The dragon's fiery breath engulfs you before you can react.")
            print("\nGAME OVER - You need to find more magical items before facing the boss.")
            self.game_over = True
            return

        print("\nYou enter the chamber, and the ancient dragon rises before you!")
        print("But with your magical items, you are prepared for this battle.")
        self.boss_battle()

    def boss_battle(self) -> None:
        boss = self.boss
        print(f"\n=== BOSS BATTLE: {boss['name']} ===")
        print(boss['description'])

        player_power = self.player.get_total_power()
        effective_boss_power = max(10, boss['power'] - player_power)

        print(f"\nYour Power: {player_power}")
        print(f"{boss['name']}'s Power: {effective_boss_power}")

        input("\nPress Enter to begin the battle...")

        boss_health = boss['health']
        player_health = self.player.health

        round_num = 1
        while boss_health > 0 and player_health > 0:
            print(f"\n--- Round {round_num} ---")

            # Player attacks
            player_damage = random.randint(player_power // 2, player_power)
            boss_health -= player_damage
            print(f"You attack the {boss['name']} for {player_damage} damage!")

            if boss_health <= 0:
                break

            # Boss attacks
            boss_damage = random.randint(effective_boss_power // 3, effective_boss_power)
            player_health -= boss_damage
            print(f"The {boss['name']} attacks you for {boss_damage} damage!")

            print(f"\nYour Health: {player_health}")
            print(f"{boss['name']}'s Health: {boss_health}")

            time.sleep(1)
            round_num += 1

        if player_health <= 0:
            print(f"\nThe {boss['name']} has defeated you!")
            print("GAME OVER")
        else:
            print(f"\nYou have defeated the {boss['name']}!")
            print("Congratulations! You have completed the adventure!")

        self.game_over = True


if __name__ == "__main__":
    game = Game()
    game.start()