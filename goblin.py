
from game_config import Player, Enemy, engine
from sqlalchemy.orm import sessionmaker

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Retrieve the player from the database
player = session.query(Player).filter_by(name='Thunder Girl').first()

# Retrieve the enemy from the database
enemy = session.query(Enemy).filter_by(id=2).first()

# Game initialization
player_health = player.health
player_power = player.power

enemy_health = enemy.health
enemy_power = enemy.power

# Game loop
while player_health > 0 and enemy_health > 0:
    # Player's turn
    enemy_health -= player_power
    if enemy_health <= 0:
        print("You defeated the Goblin!")
        break
    print("Enemy's health:", enemy_health)
    
    # Enemy's turn
    player_health -= enemy_power
    if player_health <= 0:
        print("Game over. You were defeated by Goblin.")
        break
    print("Your health:", player_health)
    
    # Update player's health in the database
    player.health = player_health
    player.hit_score(3)
    player.money(2)
    session.commit()
    
    # Wait for player input before next round
    input("Press Enter to continue...")

# Close the session
session.close()


