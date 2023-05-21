

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import PySimpleGUI as sg

Base = declarative_base()

# Intermediate table for the many-to-many relationship between Players and InventoryItem
player_inventory = Table('player_inventory', Base.metadata,
                         Column('player_id', Integer, ForeignKey('Player.id'), primary_key=True),
                         Column('inventory_item_id', Integer, ForeignKey('InventoryItem.id'), primary_key=True)
                         )


class Player(Base):
    __tablename__ = 'Player'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    power = Column(Integer, nullable=False)
    gold = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)

    inventory = relationship("InventoryItem", secondary=player_inventory, back_populates="players")

    def __str__(self):
        return {Player.name}

    def hit_score(self, amount):
        self.score += amount
        if self.score % 10 == 0:
            self.lvl_up()
            self.heal()
            self.strength()
            
    def heal(self, health=35):
        self.health += health

    def strength(self):
        self.power += 2

    def lvl_up(self):
        self.level += 1
        sg.popup("Congratulations!", self.name, "You achieved", "level", self.level , "Power +2")

    def money(self, amount):
        self.gold += amount
        

    def add_health_potion(self, health_potion):     # add health potion to players inventory
        self.inventory.append(health_potion)

    def add_power_potion(self, power_potion):       # add power potion to players inventory
        self.inventory.append(power_potion)


    def potion_health(self, health):                # use health potion from players inventory
        self.health += health
    
    def potion_power(self, power):                  # use power potion from players inventory
        self.power += power


class InventoryItem(Base):
    __tablename__ = 'InventoryItem'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    players = relationship("Player", secondary=player_inventory, back_populates="inventory")

    def use(self, player):
        if self.name == "Health Potion":
            player.potion_health(80)
            print("Your health after potion:", player.health)
        if self.name == "Power Potion":
            player.potion_power(10)
            print("Your power after potion:", player.power)
        # Decrement the quantity of the potion by 1
        self.quantity -= 1
        # If the quantity reaches 0, remove the potion from the player's inventory
        if self.quantity <= 0:
            player.inventory.remove(self)
        return player


class HealthPotion(InventoryItem):
    def __init__(self):
        self.name = "Health Potion"
        self.quantity = 0


class PowerPotion(InventoryItem):
    def __init__(self):
        self.name = "Power Potion"
        self.quantity = 0


class Enemy(Base):
    __tablename__ = 'Enemy'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False)
    power = Column(Integer, nullable=False)

    def drop_potion(self, player, potion_type, quantity):
        if potion_type == "Health Potion":
            health_potion = HealthPotion()
            health_potion.quantity = 2
            player.add_health_potion(health_potion)
            print(f"{self.name} dropped {quantity} Health Potion(s).")

        if potion_type == "Power Potion":
            power_potion = PowerPotion()
            power_potion.quantity = 2
            player.add_power_potion(power_potion)
            print(f"{self.name} dropped {quantity} Power Potion(s).")


# Create the database engine
engine = create_engine('sqlite:///thunder.db')
Base.metadata.create_all(engine)

