

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Intermediate table for the many-to-many relationship between Player and InventoryItem
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

    def money(self, amount):
        self.gold += amount
        

    def add_health_potion(self, health_potion):     # add health potion
        self.inventory.append(health_potion)

    def add_power_potion(self, power_potion):       # add power potion
        self.inventory.append(power_potion)

    def use_hp_potion(self, health_potion):         # use health potion
        health_potion.use_hp(self)

    def use_pw_potion(self, power_potion):          # use power potion
        power_potion.use_pw(self)


    def potion_health(self, health):
        self.health += health
    
    def potion_power(self, power):
        self.power += power


class InventoryItem(Base):
    __tablename__ = 'InventoryItem'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    players = relationship("Player", secondary=player_inventory, back_populates="inventory")

    def use(self, player):
        if self.name == "Health Potion":
            player.potion_health(50)
            print(player.health)
        if self.name == "Super Power Potion":
            player.potion_power(50)
            print(player.power)
        return player


class HealthPotion(InventoryItem):
    def __init__(self):
        self.name = "Health Potion"


class PowerPotion(InventoryItem):
    def __init__(self):
        self.name = "Super Power Potion"


class Enemy(Base):
    __tablename__ = 'Enemy'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False)
    power = Column(Integer, nullable=False)


# Create the database engine
engine = create_engine('sqlite:///thunder.db')
Base.metadata.create_all(engine)

