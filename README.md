# projectas_Griaustinis

The "Griaustinis" project is a fun game where the player has to defeat enemies hidden in certain locations. By defeating the mighty dragon, the main character Thunder Girl saves the handsome prince Rytis Cicinas.

# Installation Requirements

To install the game, you need to run the game_config.py and player_enemy_config files and create a default database. Make sure you have access to the pygame, PySimpleGUI, and sqlalchemy libraries before running the game.


# Gameplay

The control of the main player in the game is very simple. The game starts in the village, and by selecting a location with the mouse, we encounter enemies. If we want to fight them, we click the "Attack" button. If our strength is not enough, we can return to the village location. At any time, we can access the inventory and purchase or use a health potion.


# File Descriptions

game_config.py: This file is responsible for creating the database for the game. It should include the structure and logic of the database, allowing for the creation of necessary tables and records. This may involve defining the structure and relationships of players, enemies, inventory items, and other required data.

player_enemy_config.py: This file complements the existing database with predefined records of enemies, players, and inventory items. It should implement functionality for adding enemies, players, or inventory items to the database, updating their information, and so on.

front_end.py: This file is the main part of the game's logic and user interface. It should encompass all game rules, execution of actions, management of enemies and players, event handling, and control of user interface elements such as buttons, images, text fields, and more.

images folder: This folder contain all the images used in the game. This include images of the player, enemies, locations, or other image files relevant to the game.

sounds folder: This folder contain the game sounds. It include background music, sound effects, or other audio files used during gameplay.

All these files together form the core structure and functionality of the game. To run the game, you should execute the front_end.py file, which ensures the execution of the game logic and control of the user interface.

# Autors:
Blenderis85,
EricWebDev,
RenaldasZ,
TapuTap.

