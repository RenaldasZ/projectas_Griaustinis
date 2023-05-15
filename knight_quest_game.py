

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from game import Player, engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def start_game():
    print("\nTo play the game, enter your name!\n")
    player_name = input("Enter your knight's name: ")
    player = Player(player_name)

    try:
        session.add(player)
        session.commit()
        print(f"\nWelcome to Knight Quest, {player.name}!")
        print("""
        Once upon a time, in a distant kingdom, a courageous knight named Griaustinis received a distressing message. 
        The beautiful princess, Lady Arabella, had been captured by a fearsome dragon and imprisoned in its lair atop a mountain.
        Your quest is to find the dragon and save the princess.\n
        """)
        return player
    except IntegrityError:
        session.rollback()
        print("A knight with that name already exists. Please choose a different name.")
        return None

def game_loop(player):
    while True:
        print("What would you like to do?")
        print("1. Explore and hunt monsters")
        print("2. View Inventory")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            explore(player)
        elif choice == "2":
            view_inventory(player)
        elif choice == "3":
            print("Goodbye! Thanks for playing Knight Quest.")
            break
        else:
            print("Invalid choice. Please try again.")

def explore(player):
    print(f"\n{player.name} is exploring...\n")

    # Implement your exploration logic here

    print(f"""
    {player.name} entered the dark forest surrounding the mountain, 
        cautiously navigating through its dense vegetation. As he ventured deeper, he encountered a fork in the path.
    """)

    print(f"""
    {player.name} chose to take the path on the right, leading him to a hidden cave. Inside the cave, he found a SWORD !!!!!
    """)

    print("""
    What would you like to do next?
    """)


    player.add_to_inventory("Sword")
    session.commit()
    inventory = player.display_inventory()
    print(inventory)


def view_inventory(player):
    print(f"{player.name}'s Inventory:")
    inventory = player.display_inventory()
    print(inventory)

player = start_game()
if player:
    game_loop(player)

# Close the session
session.close()

