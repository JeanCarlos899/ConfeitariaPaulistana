import PySimpleGUI as sg

class MenuPrincipal:
    def menu_principal():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Menu principal", justification="center", font=("Helvetica", 15))],
            [sg.Button("Nova encomenda", size=(100,2))],
            [sg.Button("Listar encomendas", size=(100,2))],
            [sg.Button("Dar baixa em encomenda", size=(100,2))], 
            [sg.Button("Sair", size=(100,2))],
        ]
        return sg.Window("Confeitaria Paulistana", layout=layout, finalize=True)