import PySimpleGUI as sg 
from Scripts.print_table import print_table
 
class ListarEncomendas:
    def menu_encomendas():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Selecione a listagem", justification="center", font=("Helvetica", 15))],
            [sg.Button("Encomendas em aberto", size=(100,2))],
            [sg.Button("Encomendas fechadas", size=(100,2))],
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True)

    def listar_encomendas():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Lista de encomendas", font=("Helvetica", 15))],
            [sg.Text(print_table(), font=("Courier New", 12))], #Fonte monoespaçada para ficar alinhado
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True)