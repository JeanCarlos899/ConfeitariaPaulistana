from PySimpleGUI.PySimpleGUI import Canvas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import PySimpleGUI as sg
from reportlab.pdfgen import canvas


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



def historico_pedidos():
    file_name = input('Digite o nome do arquivo: ')
    pdf = canvas.Canvas(file_name + '.pdf')
    pdf.drawString(100,750,'Histórico de pedidos')

    pdf.setFont('Helvetica', 12)
    pdf.drawString(10,700,'ID')
    pdf.drawString(50,700,'Nome cliente')
    pdf.drawString(150,700,'Data de entrega')
    pdf.drawString(250,700,'B. Aniversário')
    pdf.drawString(350,700,'B. Casamento')
    pdf.drawString(440,700,'S. Mini')
    pdf.drawString(500,700,'S. Normal')


    pdf.setFont('Helvetica', 10)
    for i in range(len(arquivo)):
        pdf.drawString(10,650-i*20,str(arquivo['ID'][i]))
        pdf.drawString(50,650-i*20,str(arquivo['Nome cliente'][i]))
        pdf.drawString(150,650-i*20,str(arquivo['Data de entrega'][i]))
        pdf.drawString(270,650-i*20,str(arquivo['Bolo de aniversário'][i]))
        pdf.drawString(370,650-i*20,str(arquivo['Bolo de casamento'][i]))
        pdf.drawString(450,650-i*20,str(arquivo['Salgado mini'][i]))
        pdf.drawString(510,650-i*20,str(arquivo['Salgado normal'][i]))

    pdf.save()


historico_pedidos()