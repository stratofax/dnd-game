# The DnD Game

A Dungeons and Dragons text adventure game where the player navigates through various levels, collects magical items, and ultimately confronts powerful bosses. In each level, the player must find and collect magical items to have enough power to defeat that level's boss.

## Game Overview

- **Setting**: Multiple environments including an ancient castle and an enchanted forest
- **Goal**: Collect the required magical items in each level and defeat the boss
- **Challenge**: If you confront a boss without enough items, you will be defeated

## Quick Start

Download the code as a ZIP file from GitHub and extract it to a directory on your computer, or clone this repo.

This game doesn't require anything besides a working version of Python 3.9 or higher -- no additional packages are required.

To start the game, open a command prompt in this `dnd-game` directory and run:

```
python main.py
```

Depending on your system, you may need to use `python3` (typically, for Macs) instead of `python`.

Follow the on-screen prompts to enter your name and begin your quest. Good luck, adventurer!

## Game Mechanics

### Navigation

Players can move between rooms using directional commands:

- `go north`
- `go south`
- `go east`
- `go west`
- `go up`
- `go down`

### Items

Each level contains various magical items with different power values. You must collect enough items to face the boss.

#### Level 1: The Ancient Castle

- **Sword** (Power: 15) - Found in the Armory
- **Shield** (Power: 10) - Found in the Armory
- **Spellbook** (Power: 12) - Found in the Library
- **Potion** (Power: 8) - Found in the Kitchen
- **Amulet** (Power: 20) - Found in the Throne Room
- **Dagger** (Power: 5) - Found in the Dungeon

#### Level 2: The Enchanted Forest

- **Staff** (Power: 18) - Found in the Tree Hollow
- **Bow** (Power: 14) - Found in the Sacred Grove
- **Crystal** (Power: 12) - Found in the Crystal Cave
- **Cloak** (Power: 10) - Found in the Mystic Pond
- **Crown** (Power: 16) - Found in the Forest Altar
- **Berries** (Power: 5) - Found in the Forest Clearing

### Commands
- `look` - Examine your current location
- `inventory` - Check your collected items and total power
- `take [item]` - Pick up an item in the current room
- `drop [item]` - Drop an item from your inventory
- `quit` - Exit the game

### Combat

When facing a boss:
- Your total power is determined by the combined power of all items in your inventory
- Combat proceeds in rounds with both you and the boss attacking each other
- Damage is calculated randomly based on power values
- The boss's effective power is reduced by your total power

## Game Structure

The game has been designed with a modular structure to support multiple levels:

- **main.py**: Contains the main Game class and game loop
- **game_classes.py**: Contains the Item, Room, and Player classes
- **level_manager.py**: Handles loading different levels dynamically
- **level01.py, level02.py, etc.**: Individual level definitions

## Emo Art System

The game features a unique "Emo Art" visualization system that combines ASCII art with emojis:

- **Room Visualization**: Each room displays ASCII art that represents its characteristics
- **Dynamic Item Display**: Items appear as emojis below the ASCII art
- **Room Themes**: Each room has themed emojis that enhance its visual representation
- **Centered Layout**: Emojis are automatically centered beneath the ASCII art for better aesthetics
- **Item Tracking**: When items are collected, they disappear from the room display

Example of Emo Art for the Castle Entrance:

```
         /\                                 /\
        /  \    _____________________      /  \
       /    \  /                     \    /    \
      /      \/                       \  /      \
     /   _    \           []           \/        \
    /   |_|    \          []           /\         \
   /__________[]_\________[]__________/  \_________\
        |  |       Ancient Castle           |   |
        |[]|         Entrance               |[]]|
        |__|                                |___|
        
                       🏰 🚪 🏰
```

### Adding New Levels

To create a new level:
1. Create a new file named `levelXX.py` (where XX is the level number, e.g., `level03.py`)
2. Implement the `initialize_level(game)` function that creates rooms, items, and returns level metadata
3. The level will automatically be available in the game


## To Do

- Add a `help` command
- Save and load games
- Add Emo Art to Level02