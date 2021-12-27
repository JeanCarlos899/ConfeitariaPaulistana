from reportlab.pdfgen import canvas
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import PySimpleGUI as sg

arquivo = pd.read_excel('dados.xlsx')

def historico_todos_pedidos():

    file_name = f'Histórico de todos os pedidos({datetime.datetime.now().strftime("%d-%m-%Y")})'
    pdf = canvas.Canvas(file_name + '.pdf')
    pdf.setPageSize((750,1000))

    pdf.drawString(100,950,'Histórico de todos os pedidos')
    pdf.setFont('Helvetica', 12)
    pdf.drawString(10,900,'ID')
    pdf.drawString(50,900,'Nome cliente')
    pdf.drawString(150,900,'Data de entrega')
    pdf.drawString(250,900,'B. Aniversário')
    pdf.drawString(340,900,'B. Casamento')
    pdf.drawString(430,900,'S. Mini')
    pdf.drawString(485,900,'S. Normal')
    pdf.drawString(550,900,'Valor final')
    pdf.drawString(630,900,'Status')

    pdf.setFont('Helvetica', 10)
    for i in range(len(arquivo)):
        pdf.drawString(10,850-i*20,str(arquivo['ID'][i]))
        pdf.drawString(50,850-i*20,str(arquivo['Nome cliente'][i]))
        pdf.drawString(150,850-i*20,str(arquivo['Data de entrega'][i]))
        pdf.drawString(290,850-i*20,str(arquivo['Bolo de aniversário'][i]))
        pdf.drawString(360,850-i*20,str(arquivo['Bolo de casamento'][i]))
        pdf.drawString(460,850-i*20,str(arquivo['Salgado mini'][i]))
        pdf.drawString(495,850-i*20,str(arquivo['Salgado normal'][i]))
        pdf.drawString(560,850-i*20,str(arquivo['Valor final'][i]))
        pdf.drawString(640,850-i*20,str(arquivo['Status'][i]))
    
    pdf.save()


def historico_pedidos_concluido():
    file_name = f'Pedidos Concluídos({datetime.datetime.now().strftime("%d-%m-%Y")})'
    pdf = canvas.Canvas(file_name + '.pdf')
    pdf.setPageSize((750,1000))

    pdf.drawString(100,950,'Histórico de pedidos concluídos')
    pdf.setFont('Helvetica', 12)
    pdf.drawString(10,900,'ID')
    pdf.drawString(50,900,'Nome cliente')
    pdf.drawString(150,900,'Data de entrega')
    pdf.drawString(250,900,'B. Aniversário')
    pdf.drawString(340,900,'B. Casamento')
    pdf.drawString(430,900,'S. Mini')
    pdf.drawString(485,900,'S. Normal')
    pdf.drawString(560,900,'Valor final')
    pdf.drawString(630,900,'Status')


    pdf.setFont('Helvetica', 10)
    for i in range(len(arquivo)):
        if arquivo['Status'][i] == 'Concluído':
            pdf.drawString(10,850-i*20,str(arquivo['ID'][i]))
            pdf.drawString(50,850-i*20,str(arquivo['Nome cliente'][i]))
            pdf.drawString(150,850-i*20,str(arquivo['Data de entrega'][i]))
            pdf.drawString(270,850-i*20,str(arquivo['Bolo de aniversário'][i]))
            pdf.drawString(370,850-i*20,str(arquivo['Bolo de casamento'][i]))
            pdf.drawString(440,850-i*20,str(arquivo['Salgado mini'][i]))
            pdf.drawString(495,850-i*20,str(arquivo['Salgado normal'][i]))
            pdf.drawString(570,850-i*20,str(arquivo['Valor final'][i]))
            pdf.drawString(630,850-i*20,str(arquivo['Status'][i]))

    pdf.save()

def historico_pedidos_naoentregues():
    file_name = f'Pedidos não entregues({datetime.datetime.now().strftime("%d-%m-%Y")})'
    pdf = canvas.Canvas(file_name + '.pdf')
    pdf.setPageSize((750,1000))

    pdf.drawString(100,950,'Histórico de pedidos não entregues')
    pdf.setFont('Helvetica', 12)
    pdf.drawString(10,900,'ID')
    pdf.drawString(50,900,'Nome cliente')
    pdf.drawString(150,900,'Data de entrega')
    pdf.drawString(250,900,'B. Aniversário')
    pdf.drawString(340,900,'B. Casamento')
    pdf.drawString(430,900,'S. Mini')
    pdf.drawString(485, 900,'S. Normal')
    pdf.drawString(560,900,'Status')

    pdf.setFont('Helvetica', 10)
    for i in range(len(arquivo)):
        if arquivo['Status'][i] == 'Pendente':
            pdf.drawString(10,850-i*20,str(arquivo['ID'][i]))
            pdf.drawString(50,850-i*20,str(arquivo['Nome cliente'][i]))
            pdf.drawString(150,850-i*20,str(arquivo['Data de entrega'][i]))
            pdf.drawString(270,850-i*20,str(arquivo['Bolo de aniversário'][i]))
            pdf.drawString(370,850-i*20,str(arquivo['Bolo de casamento'][i]))
            pdf.drawString(440,850-i*20,str(arquivo['Salgado mini'][i]))
            pdf.drawString(495,850-i*20,str(arquivo['Salgado normal'][i]))
            pdf.drawString(570,850-i*20,str(arquivo['Status'][i]))
        
    pdf.save()

def pedidos_pendentes():

    data = datetime.datetime.now()
    datapedido = arquivo['Data de entrega']
    datapedido = pd.to_datetime(datapedido)

    file_name = f'Pedidos Pendentes({datetime.datetime.now().strftime("%d-%m-%Y")})'
    pdf = canvas.Canvas(file_name + '.pdf')
    pdf.setPageSize((750,1000))

    pdf.drawString(100,950,'Pedidos pendentes')
    pdf.setFont('Helvetica', 12)
    pdf.drawString(10,900,'ID')
    pdf.drawString(50,900,'Nome cliente')
    pdf.drawString(150,900,'Data de entrega')
    pdf.drawString(250,900,'B. Aniversário')
    pdf.drawString(340,900,'B. Casamento')
    pdf.drawString(430,900,'S. Mini')
    pdf.drawString(485,900,'S. Normal')
    pdf.drawString(560,900,'Status')

    pdf.setFont('Helvetica', 10)
    for i in range(len(arquivo)):
        if arquivo['Status'][i] == 'Pendente':
            if data > datapedido[i]:
                pdf.drawString(10,850-i*20,str(arquivo['ID'][i]))
                pdf.drawString(50,850-i*20,str(arquivo['Nome cliente'][i]))
                pdf.drawString(150,850-i*20,str(arquivo['Data de entrega'][i]))
                pdf.drawString(270,850-i*20,str(arquivo['Bolo de aniversário'][i]))
                pdf.drawString(370,850-i*20,str(arquivo['Bolo de casamento'][i]))
                pdf.drawString(440,850-i*20,str(arquivo['Salgado mini'][i]))
                pdf.drawString(495,850-i*20,str(arquivo['Salgado normal'][i]))
                pdf.drawString(560,850-i*20,str(arquivo['Status'][i]))

            
    pdf.save()


historico_pedidos_naoentregues()
