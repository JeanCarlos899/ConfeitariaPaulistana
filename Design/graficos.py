import PySimpleGUI as sg
from Scripts.new_chart import NewChart

class Graficos:
    def menu_graficos():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Selecione o gráfico", font=("Helvetica", 15))],
            [sg.Button("Gráfico Pizza: status dos pedidos", key='-STATUS_PEDIDO-' ,size=(100,2))],
            [sg.Button("Gráfico Pizza: Tipo de bolo", key='-TIPO_BOLO-' ,size=(100,2))],
            [sg.Button("Gráfico Pizza: Tipo de salgado", key='-TIPO_SALGADO-', size=(100,2))],
            [sg.Button("Gráfico de Barras: pedidos mensais", key='-MENSAIS-', size=(100,2))],
            [sg.Button("Sair", key='-SAIR-', size=(100,2))]
        ]
        return sg.Window("Gráficos", layout=layout, finalize=True)

