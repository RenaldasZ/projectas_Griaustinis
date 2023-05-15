import PySimpleGUI as sg
from sqlalchemy.orm import sessionmaker
from game import engine, Player

Session = sessionmaker(bind=engine)
session = Session()

# Create layout for the window
layout = [
    [sg.Text("1. Create a player")],
    [sg.Text("2. Take damage")],
    [sg.Text("3. Heal")],
    [sg.Text("4. Add to inventory")],
    [sg.Text("5. Remove from inventory")],
    [sg.Text("6. Display inventory")],
    [sg.Text("0. Exit")],
    [sg.Text("Enter your choice: "), sg.InputText(key="-CHOICE-")],
    [sg.Button("Submit"), sg.Button("Exit")]
]

# Create the window
window = sg.Window("Game Menu", layout)

# Loop for the menu
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    choice = values["-CHOICE-"]

    if choice == "1":
        name = sg.popup_get_text("Enter the player's name:")
        player = Player(name)
        session.add(player)
        session.commit()
        sg.popup(f"Player created. {name}")

    elif choice == "2":
        player_id = int(sg.popup_get_text("Enter the player's ID:"))
        damage = int(sg.popup_get_text("Enter the damage amount:"))
        player = session.query(Player).get(player_id)
        if player:
            player.take_damage(damage)
            session.commit()
            sg.popup("Damage taken.")
        else:
            sg.popup("Player not found.")

    elif choice == "3":
        player_id = int(sg.popup_get_text("Enter the player's ID:"))
        amount = int(sg.popup_get_text("Enter the healing amount:"))
        player = session.query(Player).get(player_id)
        if player:
            player.heal(amount)
            session.commit()
            sg.popup("Player healed.")
        else:
            sg.popup("Player not found.")

    elif choice == "4":
        player_id = int(sg.popup_get_text("Enter the player's ID:"))
        item_name = sg.popup_get_text("Enter the item name:")
        player = session.query(Player).get(player_id)
        if player:
            player.add_to_inventory(item_name)
            session.commit()
            sg.popup(f"{item_name} Item added to inventory.")
        else:
            sg.popup("Player not found.")

    elif choice == "5":
        player_id = int(sg.popup_get_text("Enter the player's ID:"))
        item_name = sg.popup_get_text("Enter the item name:")
        player = session.query(Player).get(player_id)
        if player:
            player.remove_from_inventory(item_name)
            session.commit()
            sg.popup("Item removed from inventory.")
        else:
            sg.popup("Player not found.")

    elif choice == "6":
        player_id = int(sg.popup_get_text("Enter the player's ID:"))
        player = session.query(Player).get(player_id)
        if player:
            inventory_str = player.display_inventory()
            sg.popup(inventory_str)
        else:
            sg.popup("Player not found.")

    elif choice == "0":
        break

    else:
        sg.popup("Invalid choice. Please try again.")

# Close the session
session.close()
window.close()
