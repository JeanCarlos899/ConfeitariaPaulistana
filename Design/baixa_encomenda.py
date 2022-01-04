import PySimpleGUI as sg
from Scripts.data_list import DataList

class BaixaEncomenda:
    def baixa_encomenda():
        sg.theme('Dark Blue 3')

        data_values = DataList("Pendente").get_dados_pedido_resumido()
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
                                num_rows=10, key='-TABLE_LISTAR_ENCOMENDA-',
                                background_color="#aaacb3",
                                text_color="black",
                                header_background_color="#FF8C01")
                    ],
                    [sg.Frame('Instruções de uso e peso dos bolos (Kg)',
                            [
                                [sg.Text("Selecione uma encomenda acima, insira a quantidade de Kg total do(s) bolo(s) de aniversário e casamento, depois clique em finalizar encomenda.", size=(45, 3), background_color="#e0e0e0", text_color="black")],
                                [sg.Text('', background_color="#e0e0e0")],
                                [sg.Text('Bolo Aniversário:', size=(15, 1), background_color="#e0e0e0", text_color="black"), sg.InputText(size=(10, 1), key='-BOLO_ANIVERSARIO-', default_text=0)],
                                [sg.Text('Bolo Casamento:', size=(15, 1), background_color="#e0e0e0", text_color="black"), sg.InputText(size=(10, 1), key='-BOLO_CASAMENTO-', default_text=0)]
                            ], size=(377, 190), background_color="#e0e0e0", title_color="black"
                        ),
                    sg.Frame('Valor final',
                            [
                                [sg.Output(size=(60, 10), key='-VALOR_FINAL-')]
                            ], size=(400, 190), background_color="#e0e0e0", title_color="black"
                        )
                    ],
                    [sg.Text('', font=(None, 1), background_color="#e0e0e0")],
                    [sg.Button('Finalizar encomenda', button_color=("White", "#FF8C01"), size=(30, 2), key="-FINALIZAR_ENCOMENDA-"), sg.Button("Atualizar lista", button_color=("White", "#FF8C01"), size=(30, 2), key="-ATUALIZAR_LISTA-"), sg.Button('Voltar', size=(30, 2), key="-VOLTAR-", button_color=("White", "#FF8C01"))],

                ], size=(800, 490), background_color="#e0e0e0", title_color="black"
            )]
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True, size=(800, 490), background_color="#e0e0e0")