from sqlalchemy.orm import sessionmaker
from game_config import Player, Enemy, engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# # Add items to the Item table
# item1 = Item(name='Sword', power=10, durability=100)
# item2 = Item(name='Shield', power=5, durability=200)
# item3 = Item(name='Potion', power=0, durability=1)

# session.add_all([item1, item2, item3])
# session.commit()

# # Create a player named 'Thunder Girl'
player = Player(name='Thunder Girl', health=100, level=1, power=10)
session.add(player)
session.commit()

# # Add related items to Thunder's inventory
# inventory_item1 = Inventory(name='Sword', player=thunder)
# inventory_item2 = Inventory(name='Shield', player=thunder)

# session.add_all([inventory_item1, inventory_item2])
# session.commit()

# # Add enemies to the Enemy table
enemy = Enemy(name='Rat', health=50, power=5)
session.add_all([enemy])
session.commit()

# # Add enemies to the Enemy table
enemy = Enemy(name='Goblin', health=70, power=7)
session.add_all([enemy])
session.commit()

session.close()