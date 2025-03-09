import os
import random
import time
from typing import Dict, List, Optional, Tuple

from game_classes import Item, Room, Player
from level_manager import load_level

class Game:
    def __init__(self):
        self.rooms = {}
        self.player = None
        self.boss = None
        self.game_over = False
        self.required_items = 6  # Default, will be overridden by level data
        self.current_level = 1
        self.starting_room_id = "start"  # Default, will be overridden by level data

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
        # Load the first level
        level_data = load_level(self, self.current_level)
        
        if not level_data:
            print("Error loading level. Exiting game.")
            self.game_over = True
            return
            
        print(f"\nLevel {self.current_level}: {level_data['name']}")
        print(level_data['description'])
        print(f"You must find {self.required_items} magical items to defeat the boss.")

    def start(self) -> None:
        print("Welcome to the D&D Text Adventure!")
        player_name = input("What is your name, brave adventurer? ")
        self.player = Player(player_name)

        print(f"\nWelcome, {self.player.name}!")
        print("\nCommands: go [direction], look, inventory, take [item], drop [item], quit")

        self.initialize_game()
        
        if not self.game_over:
            # Set player's starting room from level data
            self.player.current_room_id = self.starting_room_id
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
            print(f"\nAs you enter the chamber, the {self.boss['name']} rises before you!")
            print("You realize you are ill-equipped to face such a powerful foe.")
            print(f"The {self.boss['name']}'s attack engulfs you before you can react.")
            print(f"\nGAME OVER - You need to find more magical items before facing the boss.")
            self.game_over = True
            return

        print(f"\nYou enter the chamber, and the {self.boss['name']} rises before you!")
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
            self.advance_to_next_level()

        self.game_over = True
        
    def advance_to_next_level(self) -> None:
        # This method would handle advancing to the next level
        # For now, we'll just show a victory message
        print("Congratulations! You have completed the adventure!")
        print("\nTo be continued in the next level...")
        
        # In a more complete implementation, you would:
        # 1. Increment self.current_level
        # 2. Reset player's position but keep inventory
        # 3. Load the next level
        # 4. Set game_over to False to continue playing


if __name__ == "__main__":
    game = Game()
    game.start()