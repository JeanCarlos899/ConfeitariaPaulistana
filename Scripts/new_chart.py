import matplotlib.pyplot as plt
from Scripts.return_list import ReturnList

class NewChart:

    def graficoPizza():
        Entregue = ReturnList('status').__call__().count('Concluído')
        Pendente = ReturnList('status').__call__().count('Pendente')
        plt.title('Status dos pedidos')
        plt.pie([Entregue, Pendente], labels=['Concluído','Pendente'], autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()

    def graficoBarrasPedidos():
        datas = ReturnList('data_entrega').__call__()

        jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        for data in datas:
            mes = str(str(data).split('/')[1])
            if mes == '01':
                jan += 1
            if mes == '02':
                fev += 1
            if mes == '03':
                mar += 1
            if mes == '04':
                abr += 1
            if mes == '05':
                mai += 1
            if mes == '06':
                jun += 1
            if mes == '07':
                jul += 1
            if mes == '08':
                ago += 1
            if mes == '09':
                set += 1
            if mes == '10':
                out += 1
            if mes == '11':
                nov += 1
            if mes == '12':
                dez += 1

        meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
        valores = [jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez]
        plt.title('Quantidade de pedidos por mês')
        plt.bar(meses, valores)
        plt.plot(meses, valores, color='red')
        plt.show()

    def graficoTipoBolo():
        bolosA = sum(
            ReturnList('bolo_aniversario').__call__()
            )

        bolosC = sum(
            ReturnList('bolo_casamento').__call__()
            )

        plt.title('Quantidade de bolos por tipo')
        plt.pie([bolosA, bolosC], labels=['Bolo de aniversário','Bolo de casamento'], autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()

    def graficoTipoSalgados():
        salgadosM = sum(
            ReturnList('salgado_mini').__call__()
            )

        salgadoN = sum(
            ReturnList('salgado_normal').__call__()
            )

        plt.title('Quantidade de salgados por tipo')
        plt.pie([salgadosM, salgadoN], labels=['Salgado mini','Salgado normal'], autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()

    def graficoganho():
        datas = ReturnList('data_entrega').__call__()
        status = ReturnList('status').__call__()
        valor = ReturnList('valor_final').__call__()

        jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        for x in range(len(datas)):
            if status[x] == 'Concluído':
                mes = str(str(datas[x]).split('/')[1])
                if mes == '01':
                    jan += float(valor[x])
                elif mes == '02':
                    fev += float(valor[x])
                elif mes == '03':
                    mar += float(valor[x])
                elif mes == '04':
                    abr += float(valor[x])
                elif mes == '05':
                    mai += float(valor[x])
                elif mes == '06':
                    jun += float(valor[x])
                elif mes == '07':
                    jul += float(valor[x])
                elif mes == '08':
                    ago += float(valor[x])
                elif mes == '09':
                    set += float(valor[x])
                elif mes == '10':
                    out += float(valor[x])
                elif mes == '11':
                    nov += float(valor[x])
                elif mes == '12':
                    dez += float(valor[x])
        
        meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
        valores = [jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez]
        plt.title('Lucro por mês')
        plt.bar(meses, valores)
        plt.plot(meses, valores, color='red')
        plt.yticks(valores, valores)
        plt.show()

    def lucroporfesta():
        valorA = 0
        ValorC = 0
        status = ReturnList('status').__call__()

        valor = ReturnList('valor_final').__call__()

        for x in range(len(valor)):
            if status[x] == 'Concluído':
                if ReturnList('bolo_aniversario').__call__()[x] != 0:
                    valorA += float(valor[x])
                    
                if ReturnList('bolo_casamento').__call__()[x] != 0:
                    ValorC += float(valor[x])

        plt.title('Lucro por tipo de festa')
        plt.pie([valorA, ValorC], labels=['Festa de aniversário','festa de casamento'], autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()