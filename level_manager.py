import importlib
from typing import Dict, Any, Optional

def load_level(game, level_number: int) -> Dict[str, Any]:
    """
    Load a specific level into the game.
    
    Args:
        game: The Game instance to load the level into
        level_number: The level number to load
        
    Returns:
        Dict containing level metadata
    """
    # Clear any existing game state
    game.rooms = {}
    game.boss = None
    
    # Import the level module dynamically
    try:
        level_module = importlib.import_module(f"level{level_number:02d}")
    except ImportError:
        print(f"Error: Level {level_number} does not exist!")
        return None
    
    # Initialize the level
    level_data = level_module.initialize_level(game)
    
    # Set up the boss from level data
    if "boss" in level_data:
        boss_data = level_data["boss"]
        game.create_boss(
            boss_data["name"],
            boss_data["description"],
            boss_data["health"],
            boss_data["power"]
        )
    
    # Set required items from level data
    if "required_items" in level_data:
        game.required_items = level_data["required_items"]
    
    # Set starting room from level data
    if "starting_room" in level_data:
        game.starting_room_id = level_data["starting_room"]
    else:
        game.starting_room_id = "start"  # Default
    
    return level_data
