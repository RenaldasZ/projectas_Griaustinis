

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = 'Player'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    power = Column(Integer, nullable=False)


    # def take_damage(self, damage):
    #     self.health -= damage

    # def heal(self, amount):
    #     self.health += amount

class Enemy(Base):
    __tablename__ = 'Enemy'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False)
    power = Column(Integer, nullable=False)

# Create the database engine
engine = create_engine('sqlite:///thunder.db')
Base.metadata.create_all(engine)

