import PySimpleGUI as sg 
from Scripts.data_list import DataList
 
class ListarEncomendas:

    def listar_encomendas(tipo):
        sg.theme("DefaultNoMoreNagging")
        
        data_values = DataList(tipo).get_dados_pedido_resumido()
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
                ], size=(800, 60), background_color="#e0e0e0", title_color="black", 
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
                                text_color="black")
                    ],
                    [sg.Button('Voltar', size=(46, 2), key="-VOLTAR-", button_color=("White", "#FF8C01")), sg.Button('Mais informações', button_color=("White", "#FF8C01"), size=(46, 2), key="-MAIS_INFORMACOES-")]
                    
                ], size=(800, 400), background_color="#e0e0e0"
            )]
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True, size=(800, 490), background_color="#e0e0e0")

    def mais_informacoes(tipo, cliente_selecionado, index_da_lista):
        sg.theme('Dark Blue 3')
        
        #informações do cliente e horários
        data_values = [cliente_selecionado]
        data_headings = ['Nº', 'ID', 'Nome Cliente', 'Data entrega', 'Hora entrega']
        data_cols_width = [5, 5, 35, 20, 18]

        #informações da encomenda
        data_values_encomenda = [DataList(tipo).get_dados_pedido(False)[index_da_lista]]
        data_headings_encomenda = ['Bolo aniverário', 'Bolo casamento', 'Salgado mini', 'Salgado normal', 'Valor final', 'Status']
        data_cols_width_encomenda = [14, 14, 14, 14, 14, 14]
        mensagem = str(DataList(tipo).get_dados_pedido(True)[index_da_lista]) 
        
        layout = [
            [sg.Frame('Informações completas do pedido',
                [
                    [sg.Table(
                                values=data_values, 
                                headings=data_headings,
                                max_col_width=65,
                                col_widths=data_cols_width,
                                auto_size_columns=False,
                                justification='left',
                                enable_events=False,
                                num_rows=5),
                    ],
                    [sg.Table(
                                values=data_values_encomenda,
                                headings=data_headings_encomenda,
                                max_col_width=65,
                                col_widths=data_cols_width_encomenda,
                                auto_size_columns=False,
                                justification='left',
                                enable_events=False,
                                num_rows=5),
                    ],
                    [sg.Frame('Mensagem adicional',
                        [
                            [sg.Multiline(size=(800, 12), default_text=mensagem, disabled=True)],
                        ], size=(800, 200)
                    )],
                    [sg.Button('Voltar', size=(100, 2), key="-VOLTAR-")]
                ], size=(800, 500)
            )]
        ]
        return sg.Window("Mais informações", layout=layout, finalize=True, size=(800, 500)) 