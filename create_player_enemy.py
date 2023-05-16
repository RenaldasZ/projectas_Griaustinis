from sqlalchemy.orm import sessionmaker
from game_config import Player, Inventory, Enemy, Item, engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add items to the Item table
item1 = Item(name='Sword', power=10, durability=100)
item2 = Item(name='Shield', power=5, durability=200)
item3 = Item(name='Potion', power=0, durability=1)

session.add_all([item1, item2, item3])
session.commit()

# Create a player named 'Thunder'
thunder = Player(name='Thunder', health=100, level=1)
session.add(thunder)
session.commit()

# Add related items to Thunder's inventory
inventory_item1 = Inventory(name='Sword', player=thunder)
inventory_item2 = Inventory(name='Shield', player=thunder)

session.add_all([inventory_item1, inventory_item2])
session.commit()

# Add enemies to the Enemy table
enemy1 = Enemy(name='Goblin', health=50)
enemy2 = Enemy(name='Orc', health=80)

session.add_all([enemy1, enemy2])
session.commit()