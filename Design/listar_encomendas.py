import PySimpleGUI as sg 
from Scripts.print_table import print_table
 
class ListarEncomendas:
    def listar_encomendas():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Lista de encomendas", font=("Helvetica", 15))],
            [sg.Text(print_table(), font=("Courier New", 12))], #Fonte monoespaçada para ficar alinhado
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True)