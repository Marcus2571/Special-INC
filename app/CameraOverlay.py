import PySimpleGUI as sg
from Languages import Language

layout = [
    [sg.Text("Select a language:"), sg.Combo(Language, size=(20, 1), enable_events=True, key='COMBO')],
    [sg.Push(), sg.Button('Close')],
]

window = sg.Window('Title', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Close':
        break
    elif event in ('COMBO'):
        text = values['COMBO']
        print(repr(values['COMBO']))

window.close()







