import pygame
import PySimpleGUI as sg
from game_config import Player, Enemy, engine
from sqlalchemy.orm import sessionmaker

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# Load the background music
pygame.mixer.music.load("background_music.mp3")

# Play the background music on loop
pygame.mixer.music.play(loops=-1)
# Load the sound effect
sound_effect = pygame.mixer.Sound("attack.mp3")
sound_effect1 = pygame.mixer.Sound("dragon.mp3")
sound_effect2 = pygame.mixer.Sound("start.mp3")
sound_effect3 = pygame.mixer.Sound("flee.mp3")


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
    [sg.Image("images/small_warrior.png"), 
     sg.Text("""Once upon a time, in a distant kingdom, a courageous Warrior
    named 'Thunder girl aka Griaustinis' received a distressing message. 
    The beautiful prince, R. Cicinas, had been captured by a fearsome dragon
    and imprisoned in its lair atop a mountain.
    Your quest is to find the dragon and save the prince.""", font=("Gabriola", 18), justification="center")],
    [sg.Text("Thunder Girl", size=(20, 0), font=("Segoe Print", 16))],
    [sg.Text(f"Level\n{player.level}", key="-level-"), sg.Text(f"Health\n{player.health}", key="-health-"), sg.Text(f"Power\n{player.power}", key="-power-"), sg.Text(f"Gold\n{player.gold}", key="-gold-"), sg.Text(f"Score\n{player.score}", key="-score-"),
     sg.Button("Start",size=(16,0),border_width=(5), key="-new game-")]
]

layout2 = [[sg.Button("Swamp",size=(16,0), key="Swamp"), sg.Button("Cave", size=(16,0), key="Cave"), sg.Button("Forest",size=(16,0), key="Forest"), sg.Button("Mountain",size=(16,0), key="Mountain"),sg.Button("Village",size=(16,0), key="Village")],
          [sg.Output(s=(30, 10), key="-output-"), sg.Button("Attack!!!", size=(16,0), button_color=('white', 'firebrick4'),border_width=(5), key="Attack"), sg.Button("Flee",size=(16,0), key="Flee"),sg.Image(default_pic, key="-location-")]
]
layout = [
    [sg.Column(layout1, key='-COL1-')],
    [sg.Column(layout2, key='-COL2-', visible=False)]
]

window = sg.Window("Griaustinis", layout, size=(1050, 820), element_justification="center")

def attack(player:Player, enemy:Enemy, session=session):
    if player.health > 0 and enemy.health > 0:
        # Player's turn
        enemy.health -= player.power
        if enemy.health <= 0:
            player.money(enemy.power // 10)
            # player.money(20) <-- gold reward after enemy die
            print("You defeated the Enemy! Please choose another location")                
        else:
            # Enemy's turn
            player.health -= enemy.power
            if player.health <= 0:
                print("Game over. You were defeated by Enemy.")
            else:
                print("Your health:", player.health) 
                print("Enemy's health:", enemy.health)         
                player.hit_score(2)
                # player.money(2) <-- gold reward after every hit
        session.commit()
    return player
        
def update_player_stats(player, window):
    window["-level-"].update(f"Level\n{player.level}")
    window["-health-"].update(f"Health\n{player.health}")
    window["-power-"].update(f"Power\n{player.power}")
    window["-gold-"].update(f"Gold\n{player.gold}")
    window["-score-"].update(f"Score\n{player.score}")

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

player.health = 100
rat.health = 50
goblin.health = 70
ork.health = 90
dragon.health = 200

while True:
    event, values = window.read()

    if event == "-new game-":
        window["-COL2-"].update(visible=True)
        print("Welcome to your village, where your journey begins. Please choose where you would like to continue your journey.")
        
    if event == sg.WINDOW_CLOSED or event == "Close":
        break

    if event in enemy_location.keys():
        location = event
        print(location_messages[location])
        window["-location-"].update(filename=enemy_pics[location])

    if event == "Attack":
        if location and location in enemy_location.keys():
            player = attack(player, enemy_location[location])
            update_player_stats(player, window)

        else:
            print("There are no enemies here. Please choose a location.")

    if event == "Village":
        if location != event:
            if player.gold >= 10:
                player.gold -= 10
                player.heal()
            rat.health = 50
            goblin.health = 70
            ork.health = 90
            dragon.health = 200
            window["-location-"].update(filename="images/small_village.png")
            location = event
            session.commit()
            update_player_stats(player, window)
        else:
            print("You don't have enough gold to to regenerare health..")

    if event == sg.WINDOW_CLOSED or event == "Quit":
        break
    
    elif event =="Attack":
        # Play the sound effect
        sound_effect.play()
        
    elif event =="Mountain":
        # Play the sound effect
        sound_effect1.play()
        
    elif event =="-new game-":
        # Play the sound effect
        sound_effect2.play()
        
    elif event =="Flee":
        # Play the sound effect
        sound_effect3.play()
        
window.close()
 # Stop the background music when the game ends
pygame.mixer.music.stop()

# Quit pygame
pygame.quit()


