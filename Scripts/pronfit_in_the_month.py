import PySimpleGUI as sg
import datetime
from Scripts.xlsx_to_list import Xlsx_to_list

class Gasto:
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

class Lucromensal:
    def lucro():
        sg.theme('DefaultNoMoreNagging')
        layout = [
            [sg.Frame('Informe os gastos no atual mês',
                [
                    [sg.Text('Controle de Gastos')],
                    [sg.Text('', size=(100, 1), font=("Helvetica", 25), key='-OUTPUT-')],
                    [sg.Text('Quanto você gastou nesse mês com funcionários?',size=(100,1), font=("Helvetica", 15))],
                    [sg.InputText(size=(100, 1), key='-INPUT_FUNCIONARIOS-', default_text='0')],
                    [sg.Text('Quanto você gastou nesse mês com mercadorias?',size=(100,1), font=("Helvetica", 15))],
                    [sg.InputText(size=(100, 1), key='-INPUT_MERCADORIAS-', default_text='0')],
                    [sg.Text('Quanto você gastou nesse mês com impostos?',size=(100,1), font=("Helvetica", 15))],
                    [sg.InputText(size=(100, 1), key='-INPUT_IMPOSTOS-', default_text='0')],
                    [sg.Text('Quanto você gastou nesse mês com outros custos?',size=(100,1), font=("Helvetica", 15))],
                    [sg.InputText(size=(100, 1), key='-INPUT_OUTROS-', default_text='0')],
                    [sg.Button('Enviar', key='-ENVIAR-', size=(30,1), button_color=("White", "#FF8C01")), sg.Button('Sair', key='-EXIT-', size=(30,1), button_color=("White", "#FF8C01"))],
                ],
            )],
        ]
        return sg.Window('Controle de Gastos', layout, size=(500, 400), finalize=True)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == '-EXIT-':
                break
            if event == '-ENVIAR-':
                try:
                    funcionarios = float(values['-INPUT_FUNCIONARIOS-'])
                    mercadorias = float(values['-INPUT_MERCADORIAS-'])
                    impostos = float(values['-INPUT_IMPOSTOS-'])
                    outros = float(values['-INPUT_OUTROS-'])
                    total = funcionarios - mercadorias - impostos - outros + Gasto.descobrirGanhoMes()
                    window['-OUTPUT-'].update(total)
                    window['-OUTPUT-'].update(f'O lucro mensal será {total} reais')
                except ValueError:
                    window['-OUTPUT-'].update('Por favor, digite apenas números.')
            if event == '-EXIT-':
                break
        window.close()