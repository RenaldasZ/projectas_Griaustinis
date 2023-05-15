

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    health = Column(Integer)
    level = Column(Integer)
    inventory = relationship("InventoryItem", back_populates="player")

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 1

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def add_to_inventory(self, item_name):
        item = InventoryItem(name=item_name, player=self)
        self.inventory.append(item)

    def remove_from_inventory(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                break
        else:
            print(f"{item_name} is not in the inventory.")

    def display_inventory(self):
        inventory_str = "\n".join(item.name for item in self.inventory) if self.inventory else "Inventory is empty"
        return inventory_str


class InventoryItem(Base):
    __tablename__ = 'inventory_items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", back_populates="inventory")


# Create the database engine
engine = create_engine('sqlite:///players.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Creating a Player instance
character = Player("Griaustinis")


# # Adding the player to the session
session.add(character)
session.commit()

print("\nCharacter statistics:")
print("-- character Name:", character.name)
print("-- character Health:", character.health)
print("-- character Level:", character.level, "\n")

character.add_to_inventory("Wooden Sword")
character.add_to_inventory("Wooden Shield")
character.add_to_inventory("Lether Armor")
# Committing the changes to the database
session.commit()

print("Inventory:")
print(character.display_inventory())

# Close the session
session.close()
