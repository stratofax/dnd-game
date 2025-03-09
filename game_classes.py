from typing import Dict, List, Optional, Tuple


class Item:
    # Dictionary mapping item types to emojis
    ITEM_EMOJIS = {
        "sword": "⚔️",
        "shield": "🛡️",
        "spellbook": "📚",
        "potion": "🧪",
        "amulet": "📿",
        "dagger": "🗡️",
        "staff": "🏑",
        "bow": "🏹",
        "crystal": "💎",
        "cloak": "👘",
        "crown": "👑",
        "berries": "🫐",
        "default": "❓"  # Default emoji for unknown items
    }

    # Room theme emojis to display below room art
    ROOM_THEME_EMOJIS = {
        "castle_entrance": "🏰 🚪 🏰",
        "main_hall": "🏛️ 🪔 🏛️",
        "library": "📚 📖 📕 📗 📘",
        "armory": "⚔️ 🛡️ 🗡️ 🏹",
        "kitchen": "🍲 🔥 🍖 🍷",
        "dungeon": "⛓️ 🔒 ⛓️ 🔒",
        "throne_room": "👑 💎 👑 💎",
        "boss_chamber": "🐉 ⚡️ 🔥 ⚡️"
    }

    def __init__(self, name: str, description: str, power: int = 0):
        self.name = name
        self.description = description
        self.power = power  # Power value for combat

    def __str__(self) -> str:
        return self.name

    @property
    def emoji(self) -> str:
        """Get the emoji representation of this item."""
        item_name = self.name.lower()
        default = self.ITEM_EMOJIS["default"]
        return self.ITEM_EMOJIS.get(item_name, default)


class Room:
    def __init__(
        self, name: str, description: str, 
        ascii_art: Optional[str] = None, 
        theme: Optional[str] = None
    ):
        self.name = name
        self.description = description
        self._base_ascii_art = ascii_art or self._get_default_ascii_art()
        self.items = []
        self.connections = {}  # direction -> room_id
        self._item_positions = {}  # Coordinates for item placement in ASCII art
        self.theme = theme or self._derive_theme_from_name()

    def _derive_theme_from_name(self) -> str:
        """Derive a theme key from the room name for emoji selection."""
        name_lower = self.name.lower()
        for key in Item.ROOM_THEME_EMOJIS:
            if key.replace('_', ' ') in name_lower:
                return key
        # Default to the room name with spaces replaced by underscores
        return (
            name_lower.replace(' ', '_')
        )

    def _get_default_ascii_art(self) -> str:
        return """
    ╔═══════════════╗
    ║               ║
    ║  Empty Room   ║
    ║               ║
    ╚═══════════════╝
        """

    def add_item(
        self, item: Item, 
        position: Optional[Tuple[int, int]] = None
    ) -> None:
        """Add an item to the room with optional position for ASCII art display."""
        self.items.append(item)
        if position:
            self._item_positions[item.name.lower()] = position

    def remove_item(self, item_name: str) -> Optional[Item]:
        for i, item in enumerate(self.items):
            if item.name.lower() == item_name.lower():
                if item.name.lower() in self._item_positions:
                    del self._item_positions[item.name.lower()]
                return self.items.pop(i)
        return None

    def add_connection(self, direction: str, room_id: str) -> None:
        self.connections[direction.lower()] = room_id

    def get_connection(self, direction: str) -> Optional[str]:
        return (
            self.connections.get(direction.lower())
        )

    def _get_max_line_length(self) -> int:
        """Get the length of the longest line in the ASCII art."""
        lines = self._base_ascii_art.split('\n')
        return max(len(line) for line in lines if line.strip())

    def _get_theme_emojis(self) -> str:
        """Get themed emojis for this room plus any item emojis."""
        # Get the base theme emojis
        theme_emojis = Item.ROOM_THEME_EMOJIS.get(self.theme, "")
        
        # Add item emojis
        item_emojis = " ".join([item.emoji for item in self.items])
        
        if theme_emojis and item_emojis:
            return f"{theme_emojis} | {item_emojis}"
        elif item_emojis:
            return item_emojis
        else:
            return theme_emojis

    def _center_emojis(self, emoji_line: str) -> str:
        """Center the emoji line under the ASCII art."""
        if not emoji_line:
            return ""
        
        max_line_length = self._get_max_line_length()
        emoji_length = len(emoji_line)
        
        # Calculate padding to center the emoji line
        padding = max(0, (max_line_length - emoji_length) // 2)
        
        return " " * padding + emoji_line

    def display(self) -> None:
        print(f"\n=== {self.name} ===")
        print(self.description)
        print("\n" + self._base_ascii_art)
        
        # Display themed emojis and item emojis below the ASCII art
        theme_emojis = self._get_theme_emojis()
        if theme_emojis:
            centered_emojis = self._center_emojis(theme_emojis)
            print(centered_emojis)

        if self.items:
            print("\nYou see:")
            for item in self.items:
                print(f"- {item.emoji} {item.name}: {item.description}")

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
        print(f"Added {item.emoji} {item.name} to your inventory.")

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
            print(
                f"- {item.emoji} {item.name}: {item.description} "
                f"(Power: {item.power})"
            )
        print(f"Total Power: {self.get_total_power()}")
        print(f"Health: {self.health}")


def preview_level(game) -> None:
    """Display a preview of all rooms in the level with their items."""
    print("\n=== LEVEL PREVIEW ===")
    print(f"Level {game.current_level}")
    print("-" * 50)

    # Find the boss room to display its name
    boss_room = game.rooms.get("boss")
    if boss_room:
        print(f"Final Boss: {boss_room.name}")
        print("-" * 50)

    for room_id, room in game.rooms.items():
        print(f"\n=== {room.name} [{room_id}] ===")
        print(room.description)
        print("\n" + room._base_ascii_art)
        
        # Display themed emojis and item emojis below the ASCII art
        theme_emojis = room._get_theme_emojis()
        if theme_emojis:
            centered_emojis = room._center_emojis(theme_emojis)
            print(centered_emojis)
        
        if room.items:
            print("\nItems in this room:")
            for item in room.items:
                print(f"- {item.emoji} {item.name} (Power: {item.power})")
                print(f"  Description: {item.description}")
        
        print("\nConnections:")
        for direction, connected_room_id in room.connections.items():
            connected_room = game.rooms.get(connected_room_id)
            if connected_room:
                print(f"- {direction.capitalize()} ➡️ {connected_room.name}")
        
        print("-" * 50)
