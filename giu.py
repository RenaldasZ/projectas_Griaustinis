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
default_pic = "small_village.png"
layout1 = [
    [sg.Image("small_warrior.png"), 
     sg.Text("""Once upon a time, in a distant kingdom, a courageous Warrior
    named 'Thunder girl aka Griaustinis' received a distressing message. 
    The beautiful prince, R. Cicinas, had been captured by a fearsome dragon
    and imprisoned in its lair atop a mountain.
    Your quest is to find the dragon and save the prince.""", font=("Gabriola", 18), justification="center")],
    [sg.Text("Thunder Girl", key="-thunder-", size=(20, 0), font=("Segoe Print", 16))],
    [sg.Text(f"Level\n{player.level}"), sg.Text(f"Health\n{player.health}"), sg.Text(f"Power\n{player.power}"), sg.Text(f"Gold\n{player.gold}"), sg.Text(f"Score\n{player.score}"), sg.Button("Start",size=(16,0),border_width=(5), key="-new game-")]
]

layout2 = [[sg.Button("Swamp",size=(16,0), key="Swamp"), sg.Button("Cave",size=(16,0), key="Cave"), sg.Button("Forest",size=(16,0), key="Forest"), sg.Button("Mountain",size=(16,0), key="Mountain"),sg.Button("Village",size=(16,0), key="Village")],
          [sg.Output(s=(30, 10), key="-output-"), sg.Button("Attack!!!",size=(16,0), button_color=('white', 'firebrick4'),border_width=(5), key="Attack"), sg.Button("Flee",size=(16,0), key="Flee"),sg.Image(default_pic, key="-location-")]
]
layout = [
    [sg.Column(layout1, key='-COL1-')],
    [sg.Column(layout2, key='-COL2-', visible=False)]
]

window = sg.Window("Griaustinis", layout, size=(1050, 520))

def attack(player:Player, enemy:Enemy, session=session):
    while player.health > 0 and enemy.health > 0:
        # Player's turn
        enemy.health -= player.power
        if enemy.health <= 0:
            print("You defeated the Rat!")
            break
        print("Enemy's health:", enemy.health)         
        # Enemy's turn
        player.health -= enemy.power
        if player.health <= 0:
            print("Game over. You were defeated by Rat.")
            break
        print("Your health:", player.health)          
        player.hit_score(2)
        player.money(1)
        session.commit()
    return player

        
location = None
enemy_location = {
    "Swamp": rat, 
    "Cave": goblin,
    "Forest": ork,
    "Mountain": dragon,
}
location_messages = {
    "Swamp": "Atvykote į pelkę ir sutikote Žiurkių Baroną. Pasirinkite savo taktiką", 
    "Cave": "Atvykote į olą ir sutikote Gobiliną. Pasirinkite savo taktiką",
    "Forest": "Atvykote į mišką ir sutikote Ork'ą. Pasirinkite savo taktiką",
    "Mountain": "Atvykote į kalną ir sutikote Drakoną. Pasirinkite savo taktiką",
}

enemy_pics = {
    "Swamp": "small_rat.png", 
    "Cave": "small_goblin.png",
    "Forest": "small_orc.png",
    "Mountain": "small_dragon.png",
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
        print("Sveiki atvykę")
        
    if event == sg.WINDOW_CLOSED or event == "Close":
        break
    if event in enemy_location.keys():
        location = event
        print(location_messages[location])
        window["-location-"].update(filename=enemy_pics[location])
    if event == "Attack":
        if location:
            player = attack(player, enemy_location[location])
        else:
            print("Čia priešų nėra, pasirinkite vietą")
    if event == "Village":
        rat.health = 50
        goblin.health = 70
        ork.health = 90
        dragon.health = 200
        window["-location-"].update(filename="small_village.png")
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break
    elif event == "Start Game":
        # Start the game logic here
        pass
    elif event == "-VOLUME-":
        volume = values

        # Set the background music volume
        pygame.mixer.music.set_volume(volume)

window.close()
 # Stop the background music when the game ends
pygame.mixer.music.stop()

# Quit pygame
pygame.quit()


