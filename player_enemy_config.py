from sqlalchemy.orm import sessionmaker
from game_config import Player, Enemy, InventoryItem, engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a player named 'Thunder Girl'
player = Player(name='Thunder Girl', health=100, level=1, power=10, gold=10, score=0)

# # Add the health potion to the player's inventory
# potion = HealthPotion()
# player.add_health_potion(potion)

# # Add the  power potion to the player's inventory
# potion = PowerPotion()
# player.add_power_potion(potion)

## Add items to the InventoryItem table
# health_potion = InventoryItem(name='Health Potion', quantity=0)
# power_potion = InventoryItem(name='Power Potion', quantity=0)

# Add enemy to the Enemy table
enemy1 = Enemy(name='Rat', health=50, power=10)
enemy2 = Enemy(name='Goblin', health=110, power=12)
enemy3 = Enemy(name='Orc', health=200, power=15)
enemy4 = Enemy(name='Dragon', health=500, power=25)

session.add_all([player, enemy1, enemy2, enemy3, enemy4])


session.commit()
session.close()