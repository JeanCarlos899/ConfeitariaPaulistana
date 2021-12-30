from PySimpleGUI.PySimpleGUI import Canvas
import pandas as pd
import matplotlib.pyplot as plt

arquivo = pd.read_excel('dados.xlsx')

class NewChart:
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

