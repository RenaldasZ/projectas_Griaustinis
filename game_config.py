

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
    gold = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)


    def hit_score(self, amount):
        self.score += amount
        if self.score % 10 == 0:
            self.lvl_up()
            self.heal()
            self.strenght()

    def heal(self):
        self.health += 50

    def strenght(self):
        self.power += 2

    def lvl_up(self):
        self.level += 1

    def money(self, amount):
        self.gold += amount

class Enemy(Base):
    __tablename__ = 'Enemy'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, nullable=False)
    power = Column(Integer, nullable=False)

# Create the database engine
engine = create_engine('sqlite:///thunder.db')
Base.metadata.create_all(engine)

