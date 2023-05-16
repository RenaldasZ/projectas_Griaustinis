from sqlalchemy.orm import sessionmaker
from random import randint
from game_config import Player, Enemy, engine

Session = sessionmaker(bind=engine)
session = Session()

# Get the player and enemy from the database
player = session.query(Player).first()
enemy = session.query(Enemy).first()

print("Player: {} | Health: {} | Level: {}".format(player.name, player.health, player.level))
print("Enemy: Orc | Power: {}".format(enemy.id))

while player.health > 0 and enemy.id > 0:
    # Player attacks the enemy
    enemy.health -= randint(1, 10)
    if enemy.health < 0:
        enemy.Orc = 0
    print("Player attacks the enemy! Enemy Orc Power: {}".format(enemy.health))

    # Enemy attacks the player
    player.health -= randint(1, 10)
    if player.health < 0:
        player.health = 0
    print("Enemy attacks the player! Player Health: {}".format(player.health))

if player.health == 0:
    print("Game Over! You were defeated.")
else:
    print("CongOrculations! You defeated the enemy.")

# Update the player and enemy in the database
session.commit()
