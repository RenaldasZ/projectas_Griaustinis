from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Player(Base):
    __tablename__ = 'Player'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    inventory_id = Column(Integer, ForeignKey('Inventory.id'))
    inventory = relationship("Inventory", foreign_keys=[inventory_id])


class Equipment(Base):
    __tablename__ = 'Equipment'
    id = Column(Integer, primary_key=True)


class Inventory(Base):
    __tablename__ = 'Inventory'
    id = Column(Integer, primary_key=True)
    sword = Column(String, nullable=False)
    shield = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey('Player.id'))
    player = relationship("Player", foreign_keys=[player_id])


class Enemy(Base):
    __tablename__ = 'Enemy'
    id = Column(Integer, primary_key=True)
    rat = Column(Integer, nullable=False)

# Create the database engine
engine = create_engine('sqlite:///thunder.db')
Base.metadata.create_all(engine)

# Sample data
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Creating a player
player1 = Player(name='John', health=100, level=1)
session.add(player1)

# Creating inventory for the player
inventory1 = Inventory(sword='Iron Sword', shield='Wooden Shield')
player1.inventory = inventory1
session.add(inventory1)

# Creating an enemy
enemy1 = Enemy(rat=10)
session.add(enemy1)

# Commit the changes
session.commit()
