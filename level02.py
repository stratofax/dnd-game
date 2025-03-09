from typing import Dict, List, Optional, Tuple
from game_classes import Item, Room

def initialize_level(game) -> None:
    """
    Initialize the second level of the game - The Enchanted Forest
    
    Args:
        game: The Game instance to initialize with rooms, items, and boss
    """
    # Create rooms
    entry = Room(
        "Forest Edge", 
        "You stand at the edge of an ancient, enchanted forest. Massive trees with glowing leaves tower above you.",
        "forest_edge.jpg"
    )
    game.add_room("start", entry)

    clearing = Room(
        "Forest Clearing", 
        "A peaceful clearing bathed in dappled sunlight. Colorful flowers dot the ground.",
        "clearing.jpg"
    )
    game.add_room("clearing", clearing)

    pond = Room(
        "Mystic Pond", 
        "A small pond with crystal-clear water that seems to shimmer with magical energy.",
        "pond.jpg"
    )
    game.add_room("pond", pond)

    hollow = Room(
        "Tree Hollow", 
        "The inside of a massive hollow tree. Strange symbols are carved into the wood.",
        "hollow.jpg"
    )
    game.add_room("hollow", hollow)

    grove = Room(
        "Sacred Grove", 
        "A circle of ancient standing stones. The air here feels charged with primal magic.",
        "grove.jpg"
    )
    game.add_room("grove", grove)

    cave = Room(
        "Crystal Cave", 
        "A cave whose walls are lined with glowing crystals of various colors.",
        "cave.jpg"
    )
    game.add_room("cave", cave)

    altar = Room(
        "Forest Altar", 
        "A stone altar covered in moss and vines. It radiates ancient power.",
        "altar.jpg"
    )
    game.add_room("altar", altar)

    boss_chamber = Room(
        "Heart of the Forest", 
        "The very center of the forest where the oldest tree stands. Its branches reach toward the sky like grasping fingers.",
        "heart_forest.jpg"
    )
    game.add_room("boss", boss_chamber)

    # Connect rooms
    entry.add_connection("north", "clearing")

    clearing.add_connection("south", "start")
    clearing.add_connection("east", "pond")
    clearing.add_connection("west", "hollow")
    clearing.add_connection("north", "grove")

    pond.add_connection("west", "clearing")

    hollow.add_connection("east", "clearing")
    hollow.add_connection("down", "cave")

    grove.add_connection("south", "clearing")
    grove.add_connection("north", "altar")

    cave.add_connection("up", "hollow")

    altar.add_connection("south", "grove")
    altar.add_connection("north", "boss")

    boss_chamber.add_connection("south", "altar")

    # Add items
    staff = Item("Staff", "A wooden staff carved with symbols of nature. It hums with power.", 18)
    hollow.add_item(staff)

    bow = Item("Bow", "A bow made from a branch of the oldest tree in the forest. Its arrows never miss.", 14)
    grove.add_item(bow)

    crystal = Item("Crystal", "A pulsing crystal that seems to absorb and redirect magical energy.", 12)
    cave.add_item(crystal)

    cloak = Item("Cloak", "A cloak woven from leaves that never wither. It provides protection from magical attacks.", 10)
    pond.add_item(cloak)

    crown = Item("Crown", "A crown of intertwined branches and flowers. It enhances the wearer's connection to nature.", 16)
    altar.add_item(crown)

    berries = Item("Berries", "Glowing berries that restore vitality when consumed.", 5)
    clearing.add_item(berries)

    # Level metadata
    level_data = {
        "name": "The Enchanted Forest",
        "description": "An ancient forest filled with magical energy and creatures. At its heart lies a powerful entity that guards the forest's secrets.",
        "required_items": 5,  # Slightly easier than level 1
        "starting_room": "start",
        "boss": {
            "name": "Ancient Treant",
            "description": "A massive tree-like creature with glowing eyes and limbs that can crush stone.",
            "health": 180,
            "power": 60
        }
    }
    
    return level_data
