from sqlalchemy.orm import sessionmaker
from game_config import Player, Enemy, engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a player named 'Thunder Girl'
player = Player(name='Thunder Girl', health=100, level=1, power=10, gold=10, score=0)
session.add(player)
session.commit()

# Add enemies to the Enemy table
enemy = Enemy(name='Rat', health=50, power=5)
session.add_all([enemy])
session.commit()

# Add enemies to the Enemy table
enemy = Enemy(name='Goblin', health=70, power=7)
session.add_all([enemy])
session.commit()

# Add enemies to the Enemy table
enemy = Enemy(name='Orc', health=90, power=10)
session.add_all([enemy])
session.commit()

# Add enemies to the Enemy table
enemy = Enemy(name='Dragon', health=200, power=20)
session.add_all([enemy])
session.commit()

session.close()