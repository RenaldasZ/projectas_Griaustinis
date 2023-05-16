import PySimpleGUI as sg

layout1 = [[sg.Image("small_warrior.png"), sg.Text("ilga istorija")],
          [sg.Text("health"), sg.Text("power"), sg.Text("level"), sg.Button("Start",size=(20,3), key="-new game-")]
        
]
layout2 = [[sg.Button("Left",size=(16,0), key="Left"), sg.Button("Right",size=(16,0), key="Right"), sg.Button("Foward",size=(16,0), key="Foward"),sg.Button("Back",size=(16,0), key="Back")],
          [sg.Output(s=(30, 10), key="-output-")]
]
layout = [
    [sg.Column(layout1, key='-COL1-')],
    [sg.VSeperator()],
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
