import PySimpleGUI as sg
from Scripts.data_list import DataList

class BaixaEncomenda:
    def baixa_encomenda():
        sg.theme('Dark Blue 3')

        data_values = DataList.get_dados_pedido_resumido("Pendente")
        data_headings = ['Nº', 'ID', 'Nome Cliente', 'Data entrega', 'Hora entrega']
        data_cols_width = [5, 5, 35, 20, 18]

        layout = [ 
            [sg.Frame('Finalizar encomenda',
                [
                    [sg.Table(
                                values=data_values, 
                                headings=data_headings,
                                max_col_width=65,
                                col_widths=data_cols_width,
                                auto_size_columns=False,
                                justification='left',
                                enable_events=True,
                                num_rows=10, key='-TABLE_LISTAR_ENCOMENDA-')
                    ],
                    [sg.Frame('Instruções de uso e peso dos bolos (Kg)',
                            [
                                [sg.Text("Selecione uma encomenda acima, insira a quantidade de Kg total do(s) bolo(s) de aniversário e casamento, depois clique em finalizar encomenda.", size=(45, 3))],
                                [sg.Text('')],
                                [sg.Text('Bolo Aniversário:', size=(15, 1)), sg.InputText(size=(10, 1), key='bolo_aniversario')],
                                [sg.Text('Bolo Casamento:', size=(15, 1)), sg.InputText(size=(10, 1), key='bolo_casamento')]
                            ], size=(377, 190)
                        ),
                    sg.Frame('Valor final',
                            [
                                [sg.Output(size=(60, 10), key='-VALOR_FINAL-')]
                            ], size=(400, 190)
                        )
                    ],
                    [sg.Text('', font=(None, 1))],
                    [sg.Button('Finalizar encomenda', size=(46, 2)), sg.Button('Voltar', size=(46, 2))],

                ], size=(800, 490)
            )]
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True, size=(800, 490))