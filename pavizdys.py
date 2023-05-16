import PySimpleGUI as sg
import json

#import back_end as be
import time


layout1 = [
    [
        sg.Button(
            "Start new game",
            size=(16, 0),
            key="-new game-",
            border_width=(10),
            button_color="#ff1155",
        ),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Button(
            "Highscores",
            size=(16, 0),
            border_width=(10),
            button_color="#ff1155",
            key="-hs-",
        ),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Button("Load game", size=(16, 0), border_width=(10), button_color="#ff1155"),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Button(
            "Difficulty", size=(16, 0), border_width=(10), button_color="#ff1155"
        ),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Output(s=(19, 20), key="-output-"),
    ],
    [
        sg.Button(
            "Exit",
            size=(16, 0),
            key="-EXIT-",
            border_width=(10),
            button_color="#ff1155",
        ),
        sg.Text("", size=(5, 0)),
    ],
]
layout2 = [
    [
        sg.Button(
            button_text=" ",
            size=(16, 8),
            button_color=("white"),
            key=(row, col),
            disabled=False,
            image_filename="",
        )
        for row in range(4)
    ]
    for col in range(4)
]
layout = [[sg.Col(layout1, p=0), sg.Col(layout2, p=0, visible=False, key="-COL2-")]]
# Sukuriamas langas
window = sg.Window("Tile Memory Game", layout, size=(850, 620))
# Atvaizduojame ir bendraujame su langu, naudodami įvykių kilpą
previous_event = None
score = 0
highscores = []
while True:
    event, values = window.read()
    # Žiūrime, ar vartotojas nori išeiti, ar langas buvo uždarytas

    # Išvedame pranešimą į langą
    if event == "-new game-":
        window["-COL2-"].update(visible=True)
        current_time = time.time()
    if event in be.cards:
        window.read(timeout=100)
        window[event].update(image_filename="white.png")
        if previous_event:
            window[previous_event].update(image_filename="white.png")

            if be.cards[event] == be.cards[previous_event] and event != previous_event:
                score += 1
                window[previous_event].update(disabled=True)
                window[event].update(disabled=True)
                window[event].update(image_filename=be.cards[event])
                window[previous_event].update(image_filename=be.cards[event])
                previous_event = None
            else:
                window[event].update(image_filename=be.cards[event])
                window.read(timeout=555)
                window[event].update(image_filename="white.png")
                previous_event = None

        else:
            previous_event = event
            window[event].update(image_filename=be.cards[event])

    if score == 8:
        finish_time = time.time()
        total_time = finish_time - current_time
        laikas = f"{total_time:.2f}"
        scorer_name = sg.popup_get_text(f"Sveikiname, jus įveikėte delionę, jūsų laikas: {laikas} sec \nĮveskite savo vardą:")
        score = 0
        # json code
        highscoress = {}
        with open("highscores.json", "r") as json_file:
                highscoress = json.load(json_file)

        highscoress[laikas] = scorer_name
        with open("highscores.json", "w") as json_file:
            json.dump(highscoress, json_file)
        #highscores.append(laikas)
    if event == "-hs-":
        # for a in highscores:
        #     print(a)
        # json code
        # sitas isclearina langa
        window["-output-"].update('')
        # try naudojamas kai nera irasu, kad neuzsikrashintu programa
        # cia nuskaitomas json failas ir isrusiuojami atsakymai
        try:
            with open("highscores.json", "r") as json_file:
                highscoress = json.load(json_file)
            sorted_highscores = {}
            for index in sorted(highscoress):
                sorted_highscores[index]=highscoress[index]
            be.sort_highscores(sorted_highscores)
        except Exception as e:
            pass
    if event == sg.WINDOW_CLOSED or event == "-EXIT-":
        break

window.close()