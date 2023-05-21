from game_config import Player, Enemy, HealthPotion, PowerPotion, InventoryItem, sg, engine
from sqlalchemy.orm import sessionmaker

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Retrieve the player and enemy from the database
player = session.query(Player).filter_by(name='Thunder Girl').first()
rat = session.get(Enemy, 1)
goblin = session.get(Enemy, 2)
ork = session.get(Enemy, 3)
dragon = session.get(Enemy, 4)

def attack(player:Player, enemy:Enemy, session=session):
    if player.health > 0 and enemy.health > 0:
        # Player's turn
        enemy.health -= player.power
        if enemy.health <= 0:
            player.money(enemy.power) # gold reward after kill = enemy power
            print("You defeated the Enemy! Please go back to village take a rest and choose another location.") 
            if enemy.name == "Rat":
                enemy.drop_potion(player, "Health Potion", 1)  # Drops 3 Health Potions
                sg.popup("You defeated the Rat and recived Health potion.")
            if enemy.name == "Goblin":
                sg.popup("You defeated the Goblin")
            if enemy.name == "Orc":
                sg.popup("You defeated the Orc and recived Power potion!")
                enemy.drop_potion(player, "Power Potion", 1)  # Drops 2 Power Potions
            if enemy.name == "Dragon":
                sg.popup("You killed Dragon and saved Rytis Cicinas. Congratulations brave warrior! Now you can continue playing or start again.")         
        else:
            # Enemy's turn
            player.health -= enemy.power
            if player.health <= 0:
                sg.popup("Game over. You were defeated by Enemy. Go back to village.")
            else:
                print("Enemy hit you:", enemy.power, "\nYour health:", player.health) 
                print("Enemy's health:", enemy.health) 
                player.hit_score(1)        
    return player

def open_inventory(player: Player, main_window):
    layout = [[sg.Text('Inventory')]]
    for item in player.inventory:
        layout.append([sg.Text(item.name), sg.Button("use", key=item)])
    layout.append([sg.Button('Close')])

    window = sg.Window('Inventory', layout, size=(400, 300))
    
    while True:
        event, values = window.read()
        if isinstance(event, InventoryItem):
            # Assuming 'player' is an instance of the 'Player' class
            item_to_use = player.inventory[0]  # Assuming the item to use is at index 0 of the player's inventory
            player = item_to_use.use(player)  # Use the item and update the player's attributes
            # player = event.use(player)
            session.commit()
            update_player_stats(player, main_window)
            window.close()  # Close the current window
            open_inventory(player, main_window)  # Open a new inventory window

        if event == sg.WINDOW_CLOSED or event == 'Close':
            break
    window.close()

def update_player_stats(player, window):
    window["-level-"].update(f"Level\n{player.level}")
    window["-health-"].update(f"Health\n{player.health}")
    window["-power-"].update(f"Power\n{player.power}")
    window["-gold-"].update(f"Gold\n{player.gold}")
    window["-score-"].update(f"Score\n{player.score}")


