from reportlab.pdfgen import canvas
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import PySimpleGUI as sg

arquivo = pd.read_excel('dados.xlsx')

class Relatorios:
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

######################################################################
######################################################################

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
            [sg.Button('OK',key='Ok', size=(100, 1), font=('Helvetica', 15))]
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
            
            elif event == 'Ok' or event == 'OkErro':
                FrontRelatorio.fecharpopups()
                janela.close()
  


FrontRelatorio.janela_Relatorios()