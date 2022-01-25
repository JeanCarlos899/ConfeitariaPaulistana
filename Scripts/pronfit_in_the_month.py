import datetime
from Scripts.return_list import ReturnList

class Gasto:
    def descobrirMes():
        mes = datetime.datetime.now().month
        return mes
        
    def descobrirGanhoMes():
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

