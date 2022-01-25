import PySimpleGUI as sg
from Scripts.sqlite import SQLite
   
class EditarEncomenda:
    def listar_encomendas(tipo):
        sg.theme("DefaultNoMoreNagging")

        data_values = SQLite('dados.db').selected_select(
            'dados', 
            [
                'id', 
                'nome_cliente', 
                'data_entrega', 
                'hora_entrega', 
            ], f'status = "{tipo}"'
        )
        data_headings = ['Nº', 'ID', 'Nome Cliente', 'Data entrega', 'Hora entrega']
        data_cols_width = [5, 5, 35, 20, 18]

        layout = [ 
            [sg.Frame('Filtros',
                [
                    [
                        sg.Radio("Pendentes", "status", default=True, key="-STATUS_PENDENTE-", text_color="black", background_color="#e0e0e0"),
                        sg.Radio("Entregues", "status", key="-STATUS_CONCLUIDO-", text_color="black", background_color="#e0e0e0"),
                        sg.Button("Filtrar", size=(20, 1), key="-FILTRAR-", button_color=("White", "#FF8C01")),
                        sg.Text("*Selecione uma modalidade de filtro e clique em filtrar", text_color="black", background_color="#e0e0e0")
                    ],
                ], size=(800, 60), background_color="#e0e0e0"
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
                                num_rows=20, 
                                key='-INDEX_ENCOMENDA-', 
                                background_color="#aaacb3",
                                text_color="black",
                                header_background_color="#FF8C01")
                    ],
                    [
                        sg.Button('Voltar', size=(46, 2), key="-VOLTAR-", button_color=("White", "#FF8C01")), sg.Button('Editar encomenda', size=(46, 2), key="-EDITAR-", button_color=("White", "#FF8C01"))]
                    
                ], size=(800, 400), background_color="#e0e0e0"
            )]
        ]
        return sg.Window("Selecione uma encomenda para editar", layout=layout, finalize=True, size=(800, 490), background_color="#e0e0e0")

    def edit_info():
        sg.theme('DefaultNoMoreNagging')
        layout = [
            [sg.Frame('Dados do cliente e entrega (obrigatório)',
                [
                    [sg.Text("Nome do cliente:", background_color="#e0e0e0")],
                    [sg.InputText(key="-NOME_CLIENTE-", size=(115,2))],
                    [sg.Text("Data de entrega dd/mm/aaaa:", background_color="#e0e0e0")],
                    [sg.InputText(key="-DATA_ENTREGA-", size=(115,2))],
                    [sg.Text("Hora de entrega:", background_color="#e0e0e0")],
                    [sg.InputText(key="-HORA_ENTREGA-", size=(115,2), default_text="00:00")],
                ], size=(800, 180), background_color="#e0e0e0"
            )],
            [
                sg.Frame('Dados do pedido (obrigatório)',
                    [
                        [sg.Frame('Bolos', 
                            [
                                [sg.Text("Bolo de aniversário:", background_color="#e0e0e0"), sg.Text("   ", background_color="#e0e0e0", font=(None, 1)), sg.InputText(key="-BOLO_ANIVERSARIO-", size=(100,1), default_text=0)],
                                [sg.Text("Bolo de casamento:",background_color="#e0e0e0"), sg.Text("", background_color="#e0e0e0", font=(None, 1)), sg.InputText(key="-BOLO_CASAMENTO-", size=(100,1), default_text=0)],
                            ], size=(480, 80), background_color="#e0e0e0")
                        ],

                        [sg.Frame('Salgadinhos', 
                            [
                                [
                                    sg.Text("Mini salgadinho:", background_color="#e0e0e0"), 
                                    sg.Text("                     ", background_color="#e0e0e0", font=(None, 1)), sg.InputText(key="-QTD_MINI-", size=(100,1), default_text=0)
                                ],
                                [
                                    sg.Text("Salgadinho normal:", background_color="#e0e0e0"), 
                                    sg.Text("    ", background_color="#e0e0e0", font=(None, 1)), sg.InputText(key="-QTD_NORMAL-", size=(100,1), default_text=0)
                                ],
                            ], size=(480, 80), background_color="#e0e0e0")
                        ],
                    ], size=(500, 200), background_color="#e0e0e0"
                ),

                sg.Frame("Informações adicionais (opcional)",
                    [
                        [sg.Multiline(key="-INFO_COMPLEMENTARES-", size=(100, 11), background_color="#e0e0e0")]
                    ], size=(400, 200), background_color="#e0e0e0"
                )
            ],
            
            [sg.Text("", font=("Helvetica", 1))],
            [sg.Button("Confirmar", size=(100,2), key="-CONFIRMAR-", button_color=("White", "#FF8C01"))],
            [sg.Button("Voltar", key="-VOLTAR-",size=(100,2), button_color=("White", "#FF8C01"))],
        ]
        return sg.Window("Editar encomenda", layout=layout, finalize=True, size=(800, 520), background_color="#e0e0e0")



