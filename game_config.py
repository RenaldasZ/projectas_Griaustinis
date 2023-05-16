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
    power = Column(Integer, nullable=False)

# class Inventory(Base):
#     __tablename__ = 'Inventory'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     player_id = Column(Integer, ForeignKey('Player.id'))
#     item_id = Column(Integer, ForeignKey('Item.id'))

class Enemy(Base):
    __tablename__ = 'Enemy'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False)

# class Item(Base):
#     __tablename__ = 'Item'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     power = Column(Integer, nullable=False)
#     durability = Column(Integer, nullable=False)

# Create the database engine
engine = create_engine('sqlite:///thunder.db')
Base.metadata.create_all(engine)

