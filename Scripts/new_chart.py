
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import PySimpleGUI as sg


arquivo = pd.read_excel('dados.xlsx')

def graficoPizza():
    Entregue = arquivo.loc[arquivo['Status']=='Concluído']
    Pendente = arquivo.loc[arquivo['Status']=='Pendente']
    plt.title('Status dos pedidos')
    plt.pie([len(Entregue),len(Pendente)], labels=['Concluído','Pendente'], autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

def graficoBarrasPedidos():
    data = arquivo['Data de entrega']
    data = pd.to_datetime(data)

    jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(len(data)):
        if data[i].month == 1:
            jan += 1
        elif data[i].month == 2:
            fev += 1
        elif data[i].month == 3:
            mar += 1
        elif data[i].month == 4:
            abr += 1
        elif data[i].month == 5:
            mai += 1
        elif data[i].month == 6:
            jun += 1
        elif data[i].month == 7:
            jul += 1
        elif data[i].month == 8:
            ago += 1
        elif data[i].month == 9:
            set += 1
        elif data[i].month == 10:
            out += 1
        elif data[i].month == 11:
            nov += 1
        elif data[i].month == 12:
            dez += 1

    meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
    valores = [jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez]
    plt.title('Quantidade de pedidos por mês')
    plt.bar(meses, valores)
    plt.show()

def graficoTipoBolo():
    bolosA = arquivo['Bolo de aniversário']
    bolosA = bolosA.sum()

    bolosC = arquivo['Bolo de casamento']
    bolosC = bolosC.sum()

    plt.title('Quantidade de bolos por tipo')
    plt.pie([bolosA, bolosC], labels=['Bolo de aniversário','Bolo de casamento'], autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

def graficoTipoSalgados():
    salgadosM = arquivo['Salgado mini']
    salgadosM = salgadosM.sum()

    salgadoN = arquivo['Salgado normal']
    salgadoN = salgadoN.sum()

    plt.title('Quantidade de salgados por tipo')
    plt.pie([salgadosM, salgadoN], labels=['Salgado mini','Salgado normal'], autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

def lucrototal():
    lucro = arquivo['Valor final']
    lucro = lucro.sum()
    return lucro


###############################
############ GUI ###############
###############################

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
            [sg.Output(graficoPizza(), size=(100,20))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        janela = sg.Window("Gráfico Pizza", layout=layout, finalize=True)
        while True:
            event, values = janela.read()
            if event == 'Voltar':
                janela.close()
                break
            graficoPizza()
        
    def grafico_barras():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Gráfico de Barras: pedidos mensais", font=("Helvetica", 15))],
            # Inserir o gráfico aqui
            [sg.Output(graficoBarrasPedidos(), size=(100,20))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        janela = sg.Window("Gráfico de Barras", layout=layout, finalize=True)
        while True:
            event, values = janela.read()
            if event == 'Voltar':
                janela.close()
                break
            graficoBarrasPedidos()

    def grafico_tipo_bolos():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Gráfico Pizza: Tipo de bolo", font=("Helvetica", 15))],
            # Inserir o gráfico aqui
            [sg.Output(graficoTipoBolo(), size=(100,20))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        janela = sg.Window("Gráfico Pizza", layout=layout, finalize=True)
        while True:
            event, values = janela.read()
            if event == 'Voltar':
                janela.close()
                break
            graficoTipoBolo()

    def grafico_tipo_salgados():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Gráfico Pizza: Tipo de salgado", font=("Helvetica", 15))],
            # Inserir o gráfico aqui
            [sg.Output(graficoTipoSalgados(), size=(100,20))],
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