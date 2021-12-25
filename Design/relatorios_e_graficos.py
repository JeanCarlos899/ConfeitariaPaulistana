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
        ]
        return sg.Window("Gráficos", layout=layout, finalize=True)


    # se o botão Gráfico Pizza: status dos pedidos for clicado:
    def grafico_pizza():
        # criar uma janela e imprimir o gráfico
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Gráfico Pizza: status dos pedidos", font=("Helvetica", 15))],
            # Inserir o gráfico aqui
            [sg.Output(NewChart.graficoPizza(), size=(100,20))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        janela = sg.Window("Gráfico Pizza", layout=layout, finalize=True)
        while True:
            event, values = janela.read()
            if event == 'Voltar':
                janela.close()
                break
            NewChart.graficoPizza()
        
    def grafico_barras():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Gráfico de Barras: pedidos mensais", font=("Helvetica", 15))],
            # Inserir o gráfico aqui
            [sg.Output(NewChart.graficoBarrasPedidos, size=(100,20))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        janela = sg.Window("Gráfico de Barras", layout=layout, finalize=True)
        while True:
            event, values = janela.read()
            if event == 'Voltar':
                janela.close()
                break
            NewChart.graficoBarrasPedidos()

    def grafico_tipo_bolos():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Gráfico Pizza: Tipo de bolo", font=("Helvetica", 15))],
            # Inserir o gráfico aqui
            [sg.Output(NewChart.graficoTipoBolo(), size=(100,20))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        janela = sg.Window("Gráfico Pizza", layout=layout, finalize=True)
        while True:
            event, values = janela.read()
            if event == 'Voltar':
                janela.close()
                break
            NewChart.graficoTipoBolo()

    def grafico_tipo_salgados():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Gráfico Pizza: Tipo de salgado", font=("Helvetica", 15))],
            # Inserir o gráfico aqui
            [sg.Output(NewChart.graficoTipoSalgados(), size=(100,20))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        janela = sg.Window("Gráfico Pizza", layout=layout, finalize=True)

janela = Graficos.menu_graficos()
while True:
    event, values = janela.read()
    if event == 'Gráfico Pizza: status dos pedidos':
        janela.close()
        Graficos.grafico_pizza()
    elif event == 'Gráfico Pizza: Tipo de bolo':
        janela.close()
        Graficos.grafico_tipo_bolos()
    elif event == 'Gráfico Pizza: Tipo de salgado':
        janela.close()
        Graficos.grafico_tipo_salgados()
    elif event == 'Gráfico de Barras: pedidos mensais':
        janela.close()
        Graficos.grafico_barras()