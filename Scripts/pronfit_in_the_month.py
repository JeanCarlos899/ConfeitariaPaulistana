import datetime
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window
from Scripts.xlsx_to_list import Xlsx_to_list
from Design.lucro_mes import Lucromensal

class Gasto:
    def __init__(self, funcionarios, mercadorias, impostos, outros):
        self.funcionarios = funcionarios
        self.mercadorias = mercadorias
        self.impostos = impostos
        self.outros = outros
        
    def descobrirMes():
        mes = datetime.datetime.now().month
        return mes
    def descobrirGanhoMes():
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

        mes = Gasto.descobrirMes()
        if mes == 1:
            return jan
        elif mes == 2:
            return fev
        elif mes == 3:
            return mar
        elif mes == 4:
            return abr
        elif mes == 5:
            return mai
        elif mes == 6:
            return jun
        elif mes == 7:
            return jul
        elif mes == 8:
            return ago
        elif mes == 9:
            return set
        elif mes == 10:
            return out
        elif mes == 11:
            return nov
        elif mes == 12:
            return dez

