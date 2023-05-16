

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Player(Base):
    __tablename__ = 'Player'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    inventory = relationship('Inventory', backref='player')

class Inventory(Base):
    __tablename__ = 'Inventory'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey('Player.id'))
    item_id = Column(Integer, ForeignKey('Item.id'))

class Enemy(Base):
    __tablename__ = 'Enemy'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False)

class Item(Base):
    __tablename__ = 'Item'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    power = Column(Integer, nullable=False)
    durability = Column(Integer, nullable=False)

# Create the database engine
engine = create_engine('sqlite:///thunder.db')
Base.metadata.create_all(engine)

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

# # Game logic
# def attack(player, enemy):
#     weapon_power = session.query(Item.power).join(Inventory, Item.id == Inventory.item_id).filter(Inventory.player_id == player.id).first()
#     if weapon_power is not None:
#         weapon_power = weapon_power[0]  # Access the power attribute if the query result is not None
#     else:
#         weapon_power = 0  # Assign a default value if weapon_power is None

#     enemy.health -= weapon_power
#     player.health -= enemy.health

#     if enemy.health <= 0:
#         print(f'{player.name} defeated {enemy.name}!')
#     elif player.health <= 0:
#         print(f'{enemy.name} defeated {player.name}!')
#     else:
#         print(f'{player.name} and {enemy.name} are still in battle!')

# # Create a session
# Session = sessionmaker(bind=engine)
# session = Session()

# # Retrieve the player 'Thunder' and the enemies from the database
# thunder = session.query(Player).filter_by(name='Thunder').first()
# enemies = session.query(Enemy).all()

# # Perform a battle with each enemy
# for enemy in enemies:
#     attack(thunder, enemy)

# Close the session
session.close()


