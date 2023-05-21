import pygame
import PySimpleGUI as sg
from sqlalchemy.orm import sessionmaker
from game_config import Player, Enemy, engine
from views import attack, open_inventory, update_player_stats

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()
# Load the background music
pygame.mixer.music.load("sounds/background_music.mp3")
# Play the background music on loop
pygame.mixer.music.play(loops=-1)
# Set the initial volume (range: 0.0 to 1.0)
initial_volume = 0.1
pygame.mixer.music.set_volume(initial_volume)

# Retrieve the player and enemy from the database
player = session.query(Player).filter_by(name='Thunder Girl').first()
rat = session.get(Enemy, 1)
goblin = session.get(Enemy, 2)
ork = session.get(Enemy, 3)
dragon = session.get(Enemy, 4)

sg.theme('Dark2')
default_pic = "images/small_village.png"

layout1 = [
    [
        sg.Image("images/small_warrior.png"), 
        sg.Text(
            """Once upon a time, in a distant kingdom, a courageous Warrior
            named 'Thunder girl aka Griaustinis' received a distressing message. 
            The beautiful prince, R. Cicinas, had been captured by a fearsome dragon
            and imprisoned in its lair atop a mountain.
            Your quest is to find the dragon and save the prince.""",
            font=("Gabriola", 18),
            justification="center"
        ),
        sg.Image("images/small_dragon.png")
    ],
    [sg.Text("Thunder Girl", size=(20, 0), font=("Segoe Print", 16))],
    [
        sg.Text(f"Level\n{player.level}", key="-level-"),
        sg.Text(f"Health\n{player.health}", key="-health-"),
        sg.Text(f"Power\n{player.power}", key="-power-"),
        sg.Text(f"Gold\n{player.gold}", key="-gold-"),
        sg.Text(f"Score\n{player.score}", key="-score-")
    ],
    [sg.Button("Play", size=(14, 0), border_width=4, key="-start game-")]
]


layout2 = [[sg.Button("Swamp",size=(16,0), key="Swamp"), 
            sg.Button("Cave", size=(16,0), key="Cave"), 
            sg.Button("Forest",size=(16,0), key="Forest"), 
            sg.Button("Mountain",size=(16,0), key="Mountain"),
            sg.Button("Village",size=(16,0), key="Village")],
          [sg.Output(s=(30, 10), key="-output-"), 
           sg.Button("Attack!!!", size=(16,0), button_color=('white', 'firebrick4'),border_width=(5), key="Attack"), 
           sg.Button("Inventory",size=(16,0), key="-inventory-"),
           sg.Image(default_pic, key="-location-")]
]

layout = [
    [sg.Column(layout1, key='-COL1-', justification="center")],
    [sg.Column(layout2, key='-COL2-', justification="center", visible=False)]
]

window = sg.Window("Thunder girl aka Griaustinis", layout, size=(1050, 820))

location = None
enemy_location = {
    "Swamp": rat, 
    "Cave": goblin,
    "Forest": ork,
    "Mountain": dragon,
}

location_messages = {
    "Swamp": "You have arrived at the swamp and encountered the Rat Baron. Choose your strategy: Attack or Flee", 
    "Cave": "You have arrived at the cave and encountered the Goblin. Choose your strategy: Attack or Flee",
    "Forest": "You have arrived at the forest and encountered the Orc. Choose your strategy: Attack or Flee",
    "Mountain": "You have arrived at the mountain and encountered the Dragon.Choose your strategy: Attack or Flee",
}

enemy_pics = {
    "Swamp": "images/small_rat.png", 
    "Cave": "images/small_goblin.png",
    "Forest": "images/small_orc.png",
    "Mountain": "images/small_dragon.png",
}

location_sounds = {
    "Attack": "sounds/attack.mp3", 
    "Mountain": "sounds/dragon.mp3",
    "-start game-": "sounds/start.mp3",
    "Swamp": "sounds/rat.mp3",
    "Cave": "sounds/goblin.mp3",
    "Forest": "sounds/ork.mp3",
    "Village": "sounds/village.mp3",
    "-inventory-": "sounds/inventory.mp3",
    "-use-": "sounds/potion.mp3",
}


#creating instance
player.health = 100
rat.health = 50
goblin.health = 110
ork.health = 200
dragon.health = 500

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Close":
        session.commit()
        break

    if event == "-start game-":
        window["-COL2-"].update(visible=True)
        print("Welcome to your village, where your journey begins. Please choose where you would like to continue your journey.")
        pygame.mixer.Sound(location_sounds["-start game-"]).play()

    if event in enemy_location.keys():
        location = event
        print(location_messages[location])
        pygame.mixer.Sound(location_sounds[location]).play()
        window["-location-"].update(filename=enemy_pics[location])
        window["Swamp"].update(disabled=True)
        window["Cave"].update(disabled=True)
        window["Forest"].update(disabled=True)
        window["Mountain"].update(disabled=True)
        window["Attack"].update(disabled=False)

    if event == "Attack":
        if location and location in enemy_location.keys():
            player = attack(player, enemy_location[location])
            update_player_stats(player, window)
            pygame.mixer.Sound(location_sounds[event]).play()
            session.commit()
        else:
            print("There are no enemies here. Please choose a different location.")

    if event == "Village":
        if location != event:
            if player.gold >= 10:
                player.gold -= 10
                player.heal()
            rat.health = 50
            goblin.health = 110
            ork.health = 200
            dragon.health = 500
            window["-location-"].update(filename="images/small_village.png")
            location = event
            update_player_stats(player, window)
            window["Swamp"].update(disabled=False)
            window["Cave"].update(disabled=False)
            window["Forest"].update(disabled=False)
            window["Mountain"].update(disabled=False)
            window["Attack"].update(disabled=True)
            session.commit()
            pygame.mixer.Sound(location_sounds[event]).play()
        else:
            print("You don't have enough gold to regenerate health.. Go back to adventure!")

    if event == sg.WINDOW_CLOSED or event == "Quit":
        break

    if event == '-inventory-':
        pygame.mixer.Sound(location_sounds[event]).play()
        open_inventory(player, window)
        
window.close()

pygame.mixer.music.stop()
pygame.quit()


