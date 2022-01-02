import pandas as pd
import matplotlib.pyplot as plt
from Scripts.xlsx_to_list import Xlsx_to_list
class NewChart:
    def graficoPizza():
        arquivo = pd.read_excel('dados.xlsx')

        Entregue = arquivo.loc[arquivo['Status']=='Concluído']
        Pendente = arquivo.loc[arquivo['Status']=='Pendente']
        plt.title('Status dos pedidos')
        plt.pie([len(Entregue),len(Pendente)], labels=['Concluído','Pendente'], autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()

    def graficoBarrasPedidos():
        datas = Xlsx_to_list("C").toListStr()

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
        arquivo = pd.read_excel('dados.xlsx')

        bolosA = arquivo['Bolo de aniversário']
        bolosA = bolosA.sum()

        bolosC = arquivo['Bolo de casamento']
        bolosC = bolosC.sum()

        plt.title('Quantidade de bolos por tipo')
        plt.pie([bolosA, bolosC], labels=['Bolo de aniversário','Bolo de casamento'], autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()

    def graficoTipoSalgados():
        arquivo = pd.read_excel('dados.xlsx')

        salgadosM = arquivo['Salgado mini']
        salgadosM = salgadosM.sum()

        salgadoN = arquivo['Salgado normal']
        salgadoN = salgadoN.sum()

        plt.title('Quantidade de salgados por tipo')
        plt.pie([salgadosM, salgadoN], labels=['Salgado mini','Salgado normal'], autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()

    def graficoganho():
        datas = Xlsx_to_list("C").toListStr()
        status = Xlsx_to_list("K").toListStr()
        valor = Xlsx_to_list("I").toListStr()

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
        arquivo = pd.read_excel('dados.xlsx')
        valorA = 0
        ValorC = 0
        status = Xlsx_to_list("K").toListStr()

        valor = arquivo['Valor final']

        for x in range(len(valor)):
            if status[x] == 'Concluído':
                # somar valor de bolos de aniversário
                if arquivo['Bolo de aniversário'][x] != 0:
                    valorA += float(valor[x])
                # somar valor de bolos de casamento
                if arquivo['Bolo de casamento'][x] != 0:
                    ValorC += float(valor[x])

        plt.title('Lucro por tipo de festa')
        plt.pie([valorA, ValorC], labels=['Festa de aniversário','festa de casamento'], autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()





