from typing import Optional
import PySimpleGUI as sg
from Design.listar_encomendas import PrintTable

class BaixaEncomenda:
    def baixa_encomenda():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text(PrintTable.imprimir_tabela("Pendente"), font=("Courier New", 10))],
            [sg.Text("Informe o ID da encomenda: ", )],
            [sg.InputText(key="id", size=(115,2), default_text=0)],

            [sg.Text("Informe o(s) Kg do(s) bolo(s) de aniversário: *caso tenha mais de um bolo, informe o valor total*")],
            [sg.InputText(key="kg_bolo_aniversario", size=(115,2), default_text=0)],

            [sg.Text("Informe o(s) Kg do(s) bolo(s) de casamento: *caso tenha mais de um bolo, informe o valor total*")],
            [sg.InputText(key="kg_bolo_casamento", size=(115,2), default_text=0)],

            [sg.Button("Confirmar", size=(100,2))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Dar baixa em encomenda", layout=layout, finalize=True)
        
    def popup_baixa(valor_final):
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text(f"O valor final da encomenda é: R$ {valor_final}", font=("Helvetica", 15))],
            [sg.Button("Ok", size=(50,2))],
        ]
        return sg.Window("Confirmar baixa", layout=layout, finalize=True)

