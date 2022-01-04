import PySimpleGUI as sg
from Scripts.pronfit_in_the_month import Gasto

class Lucromensal:

    def lucro():
        sg.theme('DefaultNoMoreNagging')
        layout = [
            [sg.Frame('Informe os gastos no atual mês',
                [
                    [sg.Text('Controle de Gastos')],
                    [sg.Text('', size=(100, 1), font=("Helvetica", 18), key='-OUTPUT-')],
                    [sg.Text('Quanto você gastou nesse mês com funcionários?',size=(100,1), font=("Helvetica", 15))],
                    [sg.InputText(size=(100, 1), key='-INPUT_FUNCIONARIOS-', default_text='0')],
                    [sg.Text('Quanto você gastou nesse mês com mercadorias?',size=(100,1), font=("Helvetica", 15))],
                    [sg.InputText(size=(100, 1), key='-INPUT_MERCADORIAS-', default_text='0')],
                    [sg.Text('Quanto você gastou nesse mês com impostos?',size=(100,1), font=("Helvetica", 15))],
                    [sg.InputText(size=(100, 1), key='-INPUT_IMPOSTOS-', default_text='0')],
                    [sg.Text('Quanto você gastou nesse mês com outros custos?',size=(100,1), font=("Helvetica", 15))],
                    [sg.InputText(size=(100, 1), key='-INPUT_OUTROS-', default_text='0')],
                    [sg.Button('Enviar', key='-ENVIAR-', size=(28,1), button_color=("White", "#FF8C01")), sg.Button('Sair', key='-EXIT-', size=(28,1), button_color=("White", "#FF8C01"))],
                ], size=(500, 400)
            )],
        ]
        return sg.Window('Controle de Gastos', layout, size=(500, 400), finalize=True)



