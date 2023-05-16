import PySimpleGUI as sg

sg.theme('Dark2')

layout1 = [[sg.Image("small_warrior.png"), sg.Text("Once upon a time, in a distant kingdom, a courageous knight named\n 'Griaustinis' received a distressing message. The beautiful princess, Lady Arabella, had been\n captured by a fearsome dragon and imprisoned in its lair atop a mountain.Your quest is to find the dragon\n and save the princess.", font=("Edwardian Script ITC", 21))],
          [sg.Text("Thunder", key="-thunder-", size=(20, 0), font=("Algerian", 25))],
          [sg.Text("health"), sg.Text("power"), sg.Text("level"), sg.Button("Start",size=(16,0),border_width=(10), key="-new game-")],       
]

layout2 = [[sg.Button("Left",size=(16,0), key="Left"), sg.Button("Right",size=(16,0), key="Right"), sg.Button("Foward",size=(16,0), key="Foward"),sg.Button("Back",size=(16,0), key="Back")],
          [sg.Output(s=(30, 10), key="-output-"), sg.Button("Attack!!!",size=(16,0), button_color=('white', 'firebrick4'),border_width=(10), key="Atack"), sg.Button("Flee",size=(16,0), key="Flee")]
]
layout = [
    [sg.Column(layout1, key='-COL1-')],
    [sg.Column(layout2, key='-COL2-', visible=False)]
]

window = sg.Window("Griaustinis", layout, size=(850, 620))

while True:
    event, values = window.read()
    if event == "-new game-":
        window["-COL2-"].update(visible=True)
    if event == sg.WINDOW_CLOSED or event == "Close":
        break

window.close()

