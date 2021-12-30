import PySimpleGUI as sg
from Scripts.reports import Relatorios

class FrontRelatorio:
    def menu_relatorios():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text('Relatórios', size=(15, 1), font=('Helvetica', 25))],
            [sg.Text('Selecione o relatório desejado:', size=(30, 1), font=('Helvetica', 15))],
            [sg.Button('Pedidos entregues',key='-PEDIDOS_ENTREGUES-', size=(100, 1), font=('Helvetica', 15))],
            [sg.Button('Pedidos não entregues', key='-PEDIDOS_NAO_ENTREGUES-', size=(100, 1), font=('Helvetica', 15))],
            [sg.Button('Pedidos pendentes', key='-PEDIDOS_PENDENTES-', size=(100, 1), font=('Helvetica', 15))],
            [sg.Button('Todos os pedidos', key='-TODOS_PEDIDOS-', size=(100, 1), font=('Helvetica', 15))],
            [sg.Button('Voltar', key='-VOLTAR-', size=(100, 1), font=('Helvetica', 15))]
        ]
        return sg.Window("Relatórios", layout=layout, finalize=True)

    def popupConfirmacao():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text('Tabela gerada com sucesso', size=(100, 1), font=('Helvetica', 15))],
            [sg.Button('Ok', key='-OK-', size=(100, 1), font=('Helvetica', 15))]
        ]
        return sg.Window("confirmacao", layout=layout, finalize=True)

    def popupErro():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text('Erro ao gerar a tabela',key="OkErro", size=(1000, 1), font=('Helvetica', 15))],
            [sg.Button('Ok', key='-OK_ERRO-', size=(100, 1), font=('Helvetica', 15))]
        ]
        return sg.Window("erro", layout=layout, finalize=True)

 


