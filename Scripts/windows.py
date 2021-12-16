import PySimpleGUI as sg
import pandas as pd
from Scripts.print_table import print_table

class Windows:
    def janela_principal():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Menu principal", justification="center", font=("Helvetica", 15))],
            [sg.Button("Nova encomenda", size=(100,2))],
            [sg.Button("Listar encomendas", size=(100,2))],
            [sg.Button("Dar baixa em encomenda", size=(100,2))], 
            [sg.Button("Sair", size=(100,2))],
        ]
        return sg.Window("Confeitaria Paulistana", layout=layout, finalize=True)

    def janela_nova_encomenda():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Nova encomenda", justification="center", font=("Helvetica", 15))],
            [sg.Checkbox("Bolo de aniversário", key="bolo_aniversario")],
            [sg.Checkbox("Bolo de casamento", key="bolo_casamento")],
            [sg.Button("Confirmar", size=(100,2))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Nova encomenda", layout=layout, finalize=True)

    def janela_listar_encomendas():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Lista de encomendas", font=("Helvetica", 15))],
            [sg.Text(print_table(), font=("Courier New", 12))], #Fonte monoespaçada para ficar alinhado
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True)

    def janela_dados_cliente():
        sg.theme('Dark Blue 3')
        layout = [
            #input para nome do cliente, data de entrega e peso do bolo
            [sg.Text("Nome do cliente:")],
            [sg.InputText(key="nome_cliente", size=(115,2))],
            [sg.Text("Data de entrega:")],
            [sg.InputText(key="data_entrega", size=(115,2))],
            [sg.Text("Peso do bolo (aproximado): ")],
            [sg.InputText(key="peso", size=(115,2))],
            [sg.Button("Confirmar", size=(100,2))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Informações", layout=layout, finalize=True)

    def janela_baixa_encomenda():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Informe o número da encomenda: "), sg.InputText(key="numero_encomenda")],
            [sg.Button("Voltar", size=(100,2))],
            [sg.Button("Listar encomendas", size=(100,2))],
            [sg.Button("Confirmar", size=(100,2))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Dar baixa em encomenda", layout=layout, finalize=True)