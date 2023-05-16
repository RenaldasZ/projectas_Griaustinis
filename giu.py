import PySimpleGUI as sg

layout = [[sg.Image("small_warrior.png"), sg.Text("ilga istorija")],
          [sg.Text("health"), sg.Text("power"), sg.Text("level"), sg.Button("Start")],
          [sg.Output(s=(30, 10), key="-output-")],

]

window = sg.Window("Griaustinis", layout, size=(850, 620))


while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Close":
        break

window.close()