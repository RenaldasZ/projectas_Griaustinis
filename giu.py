import PySimpleGUI as sg

sg.theme('Dark2')

layout1 = [
    [sg.Image("small_warrior.png"), 
     sg.Text("""Once upon a time, in a distant kingdom, a courageous Warrior
    named 'Thunder girl aka Griaustinis' received a distressing message. 
    The beautiful prince, R. Cicinas, had been captured by a fearsome dragon
    and imprisoned in its lair atop a mountain.
    Your quest is to find the dragon and save the prince.""", font=("Gabriola", 18), justification="center")],
    [sg.Text("Thunder Girl", key="-thunder-", size=(20, 0), font=("Segoe Print", 16))],
    [sg.Text("health"), sg.Text("power"), sg.Text("level"), sg.Button("Start",size=(16,0),border_width=(5), key="-new game-")]
]

layout2 = [[sg.Button("Swamp",size=(16,0), key="Swamp"), sg.Button("Cave",size=(16,0), key="Cave"), sg.Button("Forest",size=(16,0), key="Forest"), sg.Button("Mountain",size=(16,0), key="Mountain"),sg.Button("Village",size=(16,0), key="Village")],
          [sg.Output(s=(30, 10), key="-output-"), sg.Button("Attack!!!",size=(16,0), button_color=('white', 'firebrick4'),border_width=(5), key="Atack"), sg.Button("Flee",size=(16,0), key="Flee")]
]
layout = [
    [sg.Column(layout1, key='-COL1-')],
    [sg.Column(layout2, key='-COL2-', visible=False)]
]

window = sg.Window("Griaustinis", layout, size=(1050, 820))

while True:
    event, values = window.read()
    if event == "-new game-":
        window["-COL2-"].update(visible=True)
        print("Sveiki atvyk3")
        
    if event == sg.WINDOW_CLOSED or event == "Close":
        break
    
window.close()

