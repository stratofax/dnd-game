# The Prompt Log

A log of prompts used to develop the game.


The following prompt is a great way to start a chat session, if your AI has access to the code.

> Please review the README and the Python (.py) files in this repo to undestand the context of the project. Also ask me any questions you may have about the project.

At the end of chat, simply ask:

 Please update the README to reflect the changes we made during this chat session.



## 2025-03-08 

### 18:10

Great questions! Based on what you read in the main.py file, can you think of any ways to update the README file to make it more informative?

I think that's a good start, but I'd like to make the game more modular, literally by breaking it up into separate python modules. The most obvious way is to separate the intialize_game code so it can call a separate level01.py file and load in the rooms and items from that file. Ultimately I'd like the game to be able to load different levels, where a "level" is a collection of rooms and items, with a new boss in each level. Can you implement this modification to the main.py code?

It looks like it runs! Let's update the README to reflect your changes

### 20:24

Please review the README and the Python (.py) files in this repo to undestand the context of the project. Please ask me any questions you may have about the project.

I emoved the the two legacy files. Regarding images, I wanted to try using ASCII art. I suspect you may be a superb ASCII artist. I suggest we add an ASCII art representation of each Room object in a level -- this requires modifying the Room class. Then, when the player goes to a room (wih, say, a `go north` command) the ASCII art appears below the room description.

Let's work on all three enhancements. 

1. I really like the use of emojis in the ASCII art (we might need to come up with a new name, but UNICODE ART doesn't have the same ring to it as ASCII ART).  
2. I noticed some other alignment issues in some of the other images as well. 
3. Dynamic elements are a great idea! Especially if you're using emojis -- maybe we could represent each Item with a unique emoji, and then add it to the Emoji/ASCII art (I'm going to call it Emo Art for now) if it's present in a room. 

Do you want to try to make these improvements? I'd also suggest creating a method or routine that prints out all the Rooms in a level so we can review the descriptions and Emo Art for each room, with also a listing of any Items in the room when the level loads.

Adding the emojis in frame of the Emo Art disrupts the alignment. Let's try this with the Emo Art: please add some related emojis BELOW the bottom border of each Emo Art image. For example, place book and library related emojis below the bottom border of the Library Emo Art image. Then, add the Item emoji to the end of this dedicated row of emojis (for the Library, add the Spellbook emoji). Then when the player takes the item, you can display the original, un-altered Emo Art for that room

Before we run the game, can we center the emoji row below the Emo Art frame? Can you calculate the width of the longest line in each piece of Emo Art and then center the emojis below the frame? I think you need half the length of the longest line minus half the length of the emoji line, added as spaces to the emoji line on the left, might do the trick.

Let's test! 

Sorry, I quit the game. There seem to be a lot of linter errors@current_problems 

Please update the README to reflect the work we've done during this chat session. Also add a new To Do section to the README:

## To Do

- Add a `help` command
- Save and load games
- Add Emo Art to Level02