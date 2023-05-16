from sqlalchemy.orm import sessionmaker
from game_config import Player, Inventory, Enemy, Item, engine

# Game logic
def attack(player, enemy):
    weapon_power = session.query(Item.power).join(Inventory, Item.id == Inventory.item_id).filter(Inventory.player_id == player.id).first()
    if weapon_power is not None:
        weapon_power = weapon_power[0]  # Access the power attribute if the query result is not None
    else:
        weapon_power = 0  # Assign a default value if weapon_power is None

    enemy.health -= weapon_power
    player.health -= enemy.health

    if enemy.health <= 0:
        print(f'{player.name} defeated {enemy.name}!')
    elif player.health <= 0:
        print(f'{enemy.name} defeated {player.name}!')
    else:
        print(f'{player.name} and {enemy.name} are still in battle!')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Retrieve the player 'Thunder' and the enemies from the database
thunder = session.query(Player).filter_by(name='Thunder').first()
enemies = session.query(Enemy).all()

# Perform a battle with each enemy
for enemy in enemies:
    attack(thunder, enemy)

session.close()