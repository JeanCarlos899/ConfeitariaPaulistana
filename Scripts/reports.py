from reportlab.pdfgen import canvas
import datetime
from Scripts.return_list import ReturnList

class Relatorios:
    def historico_todos_pedidos():

        file_name = f'Histórico de todos os pedidos({datetime.datetime.now().strftime("%d-%m-%Y")})'
        pdf = canvas.Canvas(file_name + '.pdf')
        pdf.setPageSize((750,1000))

        pdf.drawString(315,950,'Histórico de todos os pedidos')
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
        for i in range(len(ReturnList('id').__call__())):
            pdf.drawString(10,850-i*20,str(ReturnList('id').__call__()[i]))
            pdf.drawString(50,850-i*20,str(ReturnList('nome_cliente').__call__()[i]))
            pdf.drawString(150,850-i*20,str(ReturnList('data_entrega').__call__()[i]))
            pdf.drawString(290,850-i*20,str(ReturnList('bolo_aniversario').__call__()[i]))
            pdf.drawString(360,850-i*20,str(ReturnList('bolo_casamento').__call__()[i]))
            pdf.drawString(460,850-i*20,str(ReturnList('salgado_mini').__call__()[i]))
            pdf.drawString(495,850-i*20,str(ReturnList('salgado_normal').__call__()[i]))
            pdf.drawString(560,850-i*20,str(ReturnList('valor_final').__call__()[i]))
            pdf.drawString(640,850-i*20,str(ReturnList('status').__call__()[i]))
        
        pdf.save()

    def historico_pedidos_concluido():
        file_name = f'Pedidos Concluídos({datetime.datetime.now().strftime("%d-%m-%Y")})'
        pdf = canvas.Canvas(file_name + '.pdf')
        pdf.setPageSize((750,1000))

        pdf.drawString(315,950,'Histórico de pedidos concluídos')
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
        for i in range(len(ReturnList('id').__call__())):
            if ReturnList('status').__call__()[i] == 'Concluído':
                pdf.drawString(10,850-i*20,str(ReturnList('id').__call__()[i]))
                pdf.drawString(50,850-i*20,str(ReturnList('nome_cliente').__call__()[i]))
                pdf.drawString(150,850-i*20,str(ReturnList('data_entrega').__call__()[i]))
                pdf.drawString(290,850-i*20,str(ReturnList('bolo_aniversario').__call__()[i]))
                pdf.drawString(360,850-i*20,str(ReturnList('bolo_casamento').__call__()[i]))
                pdf.drawString(460,850-i*20,str(ReturnList('salgado_mini').__call__()[i]))
                pdf.drawString(495,850-i*20,str(ReturnList('salgado_normal').__call__()[i]))
                pdf.drawString(560,850-i*20,str(ReturnList('valor_final').__call__()[i]))
                pdf.drawString(640,850-i*20,str(ReturnList('status').__call__()[i]))

        pdf.save()

    def historico_pedidos_naoentregues():
        
        file_name = f'Pedidos não entregues({datetime.datetime.now().strftime("%d-%m-%Y")})'
        pdf = canvas.Canvas(file_name + '.pdf')
        pdf.setPageSize((750,1000))

        pdf.drawString(315,950,'Histórico de pedidos não entregues')
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
        for i in range(len(ReturnList('id').__call__())):
            if ReturnList('status').__call__()[i] == 'Pendente':
                pdf.drawString(10,850-i*20,str(ReturnList('id').__call__()[i]))
                pdf.drawString(50,850-i*20,str(ReturnList('nome_cliente').__call__()[i]))
                pdf.drawString(150,850-i*20,str(ReturnList('data_entrega').__call__()[i]))
                pdf.drawString(290,850-i*20,str(ReturnList('bolo_aniversario').__call__()[i]))
                pdf.drawString(360,850-i*20,str(ReturnList('bolo_casamento').__call__()[i]))
                pdf.drawString(460,850-i*20,str(ReturnList('salgado_mini').__call__()[i]))
                pdf.drawString(495,850-i*20,str(ReturnList('salgado_normal').__call__()[i]))
                pdf.drawString(640,850-i*20,str(ReturnList('status').__call__()[i]))

        pdf.save()

    def pedidos_pendentes():
        file_name = f'Pedidos Pendentes({datetime.datetime.now().strftime("%d-%m-%Y")})'
        pdf = canvas.Canvas(file_name + '.pdf')
        pdf.setPageSize((750,1000))

        pdf.drawString(315,950,'Pedidos pendentes')
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
        for i in range(len(ReturnList('id').__call__())):
            if ReturnList('status').__call__()[i] == 'Pendente':
                pdf.drawString(10,850-i*20,str(ReturnList('id').__call__()[i]))
                pdf.drawString(50,850-i*20,str(ReturnList('nome_cliente').__call__()[i]))
                pdf.drawString(150,850-i*20,str(ReturnList('data_entrega').__call__()[i]))
                pdf.drawString(290,850-i*20,str(ReturnList('bolo_aniversario').__call__()[i]))
                pdf.drawString(360,850-i*20,str(ReturnList('bolo_casamento').__call__()[i]))
                pdf.drawString(460,850-i*20,str(ReturnList('salgado_mini').__call__()[i]))
                pdf.drawString(495,850-i*20,str(ReturnList('salgado_normal').__call__()[i]))
                pdf.drawString(640,850-i*20,str(ReturnList('status').__call__()[i]))

        pdf.save()