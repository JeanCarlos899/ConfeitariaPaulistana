import PySimpleGUI as sg
from Scripts.data_list import DataList
   
class EditarEncomenda:
    def listar_encomendas(tipo):
        sg.theme('Dark Blue 3')

        data_values = DataList(tipo).get_dados_pedido_resumido()
        data_headings = ['Nº', 'ID', 'Nome Cliente', 'Data entrega', 'Hora entrega']
        data_cols_width = [5, 5, 35, 20, 18]

        layout = [ 
            [sg.Frame('Filtros',
                [
                    [
                        sg.Radio("Pendentes", "status", default=True, key="-STATUS_PENDENTE-"),
                        sg.Radio("Entregues", "status", key="-STATUS_CONCLUIDO-"),
                        sg.Button("Filtrar", size=(20, 1), key="-FILTRAR-"),
                        sg.Text("*Selecione uma modalidade de filtro e clique em filtrar")
                    ],
                ], size=(800, 60)
            )],  
            [sg.Frame('',
                [
                    [sg.Table(
                                values=data_values, 
                                headings=data_headings,
                                max_col_width=65,
                                col_widths=data_cols_width,
                                auto_size_columns=False,
                                justification='left',
                                enable_events=True,
                                num_rows=20, key='-INDEX_ENCOMENDA-')
                    ],
                    [sg.Button('Voltar', size=(46, 2), key="-VOLTAR-"), sg.Button('Editar encomenda', size=(46, 2), key="-EDITAR-")]
                    
                ], size=(800, 400)
            )]
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True, size=(800, 490))

    def editar_encomenda():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Frame('Dados do cliente e entrega (obrigatório)',
                [
                    [sg.Text("Nome do cliente:")],
                    [sg.InputText(key="-NOME_CLIENTE-", size=(115,2))],
                    [sg.Text("Data de entrega dd/mm/aaaa:")],
                    [sg.InputText(key="-DATA_ENTREGA-", size=(115,2))],
                    [sg.Text("Hora de entrega:")],
                    [sg.InputText(key="-HORA_ENTREGA-", size=(115,2), default_text="00:00")],
                ], size=(800, 180)
            )],
            [
                sg.Frame('Dados do pedido (obrigatório)',
                    [
                        [sg.Frame('Bolos', 
                            [
                                [sg.Text("Bolo de aniversário:"), sg.Text("   ", font=(None, 1)), sg.InputText(key="-BOLO_ANIVERSARIO-", size=(100,1), default_text=0)],
                                [sg.Text("Bolo de casamento:"), sg.Text("", font=(None, 1)), sg.InputText(key="-BOLO_CASAMENTO-", size=(100,1), default_text=0)],
                            ], size=(480, 80))
                        ],

                        [sg.Frame('Salgadinhos', 
                            [
                                [
                                    sg.Text("Mini salgadinho:"), 
                                    sg.Text("                     ", font=(None, 1)), sg.InputText(key="-QTD_MINI-", size=(100,1), default_text=0)
                                ],
                                [
                                    sg.Text("Salgadinho normal:"), 
                                    sg.Text("    ", font=(None, 1)), sg.InputText(key="-QTD_NORMAL-", size=(100,1), default_text=0)
                                ],
                            ], size=(480, 80))
                        ],
                    ], size=(500, 200)
                ),

                sg.Frame("Informações adicionais (opcional)",
                    [
                        [sg.Multiline(key="-INFO_COMPLEMENTARES-", size=(100, 11))]
                    ], size=(400, 200)
                )
            ],
            
            [sg.Text("", font=("Helvetica", 1))],
            [sg.Button("Confirmar", size=(100,2), key="-CONFIRMAR-")],
            [sg.Button("Voltar", key="-VOLTAR-",size=(100,2))],
        ]
        return sg.Window("Editar encomenda", layout=layout, finalize=True, size=(800, 520))