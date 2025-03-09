from typing import Dict, List, Optional, Tuple
from game_classes import Item, Room

def initialize_level(game) -> None:
    """
    Initialize the first level of the game - The Ancient Castle
    
    Args:
        game: The Game instance to initialize with rooms, items, and boss
    """
    # Create rooms
    entry = Room(
        "Castle Entrance", 
        "You stand before an ancient castle. The massive wooden doors are partially open, revealing darkness within.",
        "castle_entrance.jpg"
    )
    game.add_room("start", entry)

    main_hall = Room(
        "Main Hall", 
        "A vast hall with a high ceiling. Dusty chandeliers hang above, and tapestries line the walls.",
        "main_hall.jpg"
    )
    game.add_room("hall", main_hall)

    library = Room(
        "Library", 
        "Shelves upon shelves of ancient tomes. The air is thick with dust and the smell of old parchment.",
        "library.jpg"
    )
    game.add_room("library", library)

    armory = Room(
        "Armory", 
        "Weapons of various kinds line the walls. Most are rusted beyond use, but a few might still serve.",
        "armory.jpg"
    )
    game.add_room("armory", armory)

    kitchen = Room(
        "Kitchen", 
        "A large stone hearth dominates one wall. Pots and pans hang from hooks, and a large table sits in the center.",
        "kitchen.jpg"
    )
    game.add_room("kitchen", kitchen)

    dungeon = Room(
        "Dungeon", 
        "A damp, dark place with cells lining the walls. Water drips from the ceiling, and the air is cold.",
        "dungeon.jpg"
    )
    game.add_room("dungeon", dungeon)

    throne_room = Room(
        "Throne Room", 
        "A grand room with a throne on a raised dais. This is where the lord of the castle would sit in judgment.",
        "throne_room.jpg"
    )
    game.add_room("throne", throne_room)

    boss_chamber = Room(
        "Boss Chamber", 
        "A circular chamber with strange runes carved into the floor. The air crackles with dark energy.",
        "boss_chamber.jpg"
    )
    game.add_room("boss", boss_chamber)

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

    # Level metadata
    level_data = {
        "name": "The Ancient Castle",
        "description": "An ancient castle that contains powerful artifacts, but beware, a terrible dragon has made its lair in the deepest chamber.",
        "required_items": 6,
        "starting_room": "start",
        "boss": {
            "name": "Ancient Dragon",
            "description": "A massive dragon with scales as black as night. Its eyes glow with malevolence.",
            "health": 200,
            "power": 70
        }
    }
    
    return level_data
