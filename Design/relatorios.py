import PySimpleGUI as sg
from Scripts.reports import Relatorios

class FrontRelatorio:
    def menu_relatorios():
        layout = [
            [sg.Text('Relatórios', size=(15, 1), font=('Helvetica', 25))],
            [sg.Text('Selecione o relatório desejado:', size=(30, 1), font=('Helvetica', 15))],
            [sg.Button('Pedidos entregues', size=(100, 1), font=('Helvetica', 15))],
            [sg.Button('Pedidos não entregues', size=(100, 1), font=('Helvetica', 15))],
            [sg.Button('Pedidos pendentes', size=(100, 1), font=('Helvetica', 15))],
            [sg.Button('Todos os pedidos', size=(100, 1), font=('Helvetica', 15))],
            [sg.Button('Voltar', size=(100, 1), font=('Helvetica', 15))]

        ]
        return sg.Window("Relatórios", layout=layout, finalize=True)

    def popupConfirmacao():

        layout = [
            [sg.Text('Tabela gerada com sucesso', size=(30, 1), font=('Helvetica', 15))],
        ]
        return sg.Window("Sucesso", layout=layout, finalize=True)

    def popupErro():
        layout = [
            [sg.Text('Erro ao gerar a tabela',key="OkErro", size=(30, 1), font=('Helvetica', 15))],
        ]
        return sg.Window("Erro", layout=layout, finalize=True)

    def fecharpopups():
        FrontRelatorio.popupConfirmacao().close()
        FrontRelatorio.popupErro().close()

    def janela_Relatorios():
        janela = FrontRelatorio.menu_relatorios()
        while True:
            event, values = janela.read()
            if event in (None, 'Voltar'):
                break
            elif event == 'Pedidos entregues':
                Relatorios.historico_pedidos_concluido()
                FrontRelatorio.popupConfirmacao()

            elif event == 'Pedidos não entregues':
                Relatorios.historico_pedidos_naoentregues()
                FrontRelatorio.popupConfirmacao()

            elif event == 'Pedidos pendentes':
                Relatorios.pedidos_pendentes()
                FrontRelatorio.popupConfirmacao()

            elif event == 'Todos os pedidos':
                Relatorios.historico_todos_pedidos()
                FrontRelatorio.popupConfirmacao()

            elif event == 'Voltar':
                janela.close()

FrontRelatorio.janela_Relatorios()