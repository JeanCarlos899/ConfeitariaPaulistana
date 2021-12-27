from reportlab.pdfgen import canvas
import pandas as pd
import matplotlib.pyplot as plt
import datetime

arquivo = pd.read_excel('dados.xlsx')

def historico_todos_pedidos():
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


def historico_pedidos_concluido():
    file_name = input('Digite o nome do arquivo: ')
    pdf = canvas.Canvas(file_name + '.pdf')
    pdf.drawString(100,750,'Histórico de pedidos concluídos')
    pdf.setFont('Helvetica', 12)
    pdf.drawString(10,700,'ID')
    pdf.drawString(50,700,'Nome cliente')
    pdf.drawString(150,700,'Data de entrega')
    pdf.drawString(250,700,'B. Aniversário')
    pdf.drawString(340,700,'B. Casamento')
    pdf.drawString(430,700,'S. Mini')
    pdf.drawString(475,700,'S. Normal')
    pdf.drawString(550,700,'Preço')


    pdf.setFont('Helvetica', 10)
    for i in range(len(arquivo)):
        if arquivo['Status'][i] == 'Concluído':
            pdf.drawString(10,650-i*20,str(arquivo['ID'][i]))
            pdf.drawString(50,650-i*20,str(arquivo['Nome cliente'][i]))
            pdf.drawString(150,650-i*20,str(arquivo['Data de entrega'][i]))
            pdf.drawString(270,650-i*20,str(arquivo['Bolo de aniversário'][i]))
            pdf.drawString(360,650-i*20,str(arquivo['Bolo de casamento'][i]))
            pdf.drawString(440,650-i*20,str(arquivo['Salgado mini'][i]))
            pdf.drawString(485,650-i*20,str(arquivo['Salgado normal'][i]))
            pdf.drawString(555,650-i*20,str(arquivo['Valor final'][i]))

    pdf.save()

def historico_pedidos_naoentregues():
    file_name = input('Digite o nome do arquivo: ')
    pdf = canvas.Canvas(file_name + '.pdf')
    pdf.drawString(100,750,'Pedidos que não foram entregues')
    pdf.setFont('Helvetica', 12)

    pdf.drawString(10,700,'ID')
    pdf.drawString(50,700,'Nome cliente')
    pdf.drawString(150,700,'Data de entrega')
    pdf.drawString(250,700,'B. Aniversário')
    pdf.drawString(340,700,'B. Casamento')
    pdf.drawString(430,700,'S. Mini')
    pdf.drawString(475,700,'S. Normal')

    pdf.setFont('Helvetica', 10)
    for i in range(len(arquivo)):
        if arquivo['Status'][i] == 'Pendente':
            pdf.drawString(10,650-i*20,str(arquivo['ID'][i]))
            pdf.drawString(50,650-i*20,str(arquivo['Nome cliente'][i]))
            pdf.drawString(150,650-i*20,str(arquivo['Data de entrega'][i]))
            pdf.drawString(270,650-i*20,str(arquivo['Bolo de aniversário'][i]))
            pdf.drawString(360,650-i*20,str(arquivo['Bolo de casamento'][i]))
            pdf.drawString(440,650-i*20,str(arquivo['Salgado mini'][i]))
            pdf.drawString(485,650-i*20,str(arquivo['Salgado normal'][i]))
            
    pdf.save()

def pedidos_pendentes():

    data = datetime.datetime.now()
    datapedido = arquivo['Data de entrega']
    datapedido = pd.to_datetime(datapedido)

    file_name = input('Digite o nome do arquivo: ')
    pdf = canvas.Canvas(file_name + '.pdf')

    pdf.drawString(100,750,'Pedidos pendentes')
    pdf.setFont('Helvetica', 12)
    pdf.drawString(10,700,'ID')
    pdf.drawString(50,700,'Nome cliente')
    pdf.drawString(150,700,'Data de entrega')
    pdf.drawString(250,700,'B. Aniversário')
    pdf.drawString(340,700,'B. Casamento')
    pdf.drawString(430,700,'S. Mini')
    pdf.drawString(475,700,'S. Normal')

    pdf.setFont('Helvetica', 10)
    for i in range(len(arquivo)):
        if arquivo['Status'][i] == 'Pendente':
            if data.date() > datapedido[i]:
                pdf.drawString(10,650-i*20,str(arquivo['ID'][i]))
                pdf.drawString(50,650-i*20,str(arquivo['Nome cliente'][i]))
                pdf.drawString(150,650-i*20,str(arquivo['Data de entrega'][i]))
                pdf.drawString(270,650-i*20,str(arquivo['Bolo de aniversário'][i]))
                pdf.drawString(360,650-i*20,str(arquivo['Bolo de casamento'][i]))
                pdf.drawString(440,650-i*20,str(arquivo['Salgado mini'][i]))
                pdf.drawString(485,650-i*20,str(arquivo['Salgado normal'][i]))
            
    pdf.save()

historico_todos_pedidos()