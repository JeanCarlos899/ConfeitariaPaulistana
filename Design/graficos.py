import PySimpleGUI as sg
from Scripts.new_chart import NewChart

class Graficos:
    def menu_graficos():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Selecione o gráfico", font=("Helvetica", 15))],
            [sg.Button("Gráfico Pizza: status dos pedidos", size=(100,2))],
            [sg.Button("Gráfico Pizza: Tipo de bolo", size=(100,2))],
            [sg.Button("Gráfico Pizza: Tipo de salgado", size=(100,2))],
            [sg.Button("Gráfico de Barras: pedidos mensais", size=(100,2))],
            [sg.Button("Sair")]
        ]
        return sg.Window("Gráficos", layout=layout, finalize=True)

    def janela_graficos():
        janela = Graficos.menu_graficos()
        while True:
            event, values = janela.read()
            if event in (None, 'Sair'):
                break
            if event == 'Gráfico Pizza: status dos pedidos':
                NewChart.graficoPizza()
            if event == 'Gráfico Pizza: Tipo de bolo':
                NewChart.graficoTipoBolo()
            if event == 'Gráfico Pizza: Tipo de salgado':
                NewChart.graficoTipoSalgados()
            if event == 'Gráfico de Barras: pedidos mensais':
                NewChart.graficoBarrasPedidos()
            if event == 'Sair':
                janela.close()
                break


tela = Graficos.janela_graficos()