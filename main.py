import re
import webbrowser
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('What anime would you like to watch?')],
    [sg.InputText()],
    [sg.Button('Search')],
]

window = sg.Window('AutoAnime', layout)

while True:
    event, values = window.read()
    data = values[0]
    if event == sg.WIN_CLOSED:  # if user closes
        break
    if event == 'Search':
        data = re.sub(r"[^\w\s]", '', data)
        data = re.sub(r"\s+", '+', data)
        webbrowser.open('https://www11.9anime.to/search?keyword=' + data)

window.close()
