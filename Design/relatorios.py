import PySimpleGUI as sg
from Scripts.reports import Relatorios

class FrontRelatorio:
    def menu_relatorios():
        sg.theme('Default1')
        layout = [
            [sg.Frame("Opções de gráficos", 
                [
                    [
                        sg.Button(image_filename="Design/Images/pedidos_entregues.png", button_color=("#E8E5EA", "#E8E5EA"), key="-PEDIDOS_ENTREGUES-",image_size=(150, 100), pad=(10, 10)),
                        sg.Button(image_filename="Design/Images/pedidos_nao_entregues.png", button_color=("#E8E5EA", "#E8E5EA"), key="-PEDIDOS_NAO_ENTREGUES-",image_size=(150, 100), pad=(10, 10))
                    ],
                    [
                        sg.Button(image_filename="Design/Images/pedidos_pendentes.png", button_color=("#E8E5EA", "#E8E5EA"), key="PEDIDOS_PENDENTES",image_size=(150, 100), pad=(10, 10)),
                        sg.Button(image_filename="Design/Images/todos_pedidos.png", button_color=("#E8E5EA", "#E8E5EA"), key="-TODOS_PEDIDOS-",image_size=(150, 100), pad=(10, 10))
                    ],
                    [sg.Button("Voltar", size=(100, 2), button_color=("White", "#FF8C01"), key="-VOLTAR-")]
                ]
            )],
        ]
        return sg.Window("Relatórios", layout=layout, finalize=True, size=(370, 330))


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

 


