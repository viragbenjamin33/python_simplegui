import PySimpleGUI as sg

layout = [[sg.Text("Hello from Beni!")], [sg.Button("OK")]]

window = sg.Window("Hello World", layout,margins=(70, 50))

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
