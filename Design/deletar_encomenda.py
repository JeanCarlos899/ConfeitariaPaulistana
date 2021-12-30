import PySimpleGUI as sg 
from Scripts.data_list import DataList
 
class DeletarEncomenda:

    def deletar_encomenda(tipo):
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
                    [sg.Button('Voltar', size=(46, 2), key="-VOLTAR-"), sg.Button('Deletar encomenda', size=(46, 2), key="-DELETAR_ENCOMENDA-")]
                    
                ], size=(800, 400)
            )]
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True, size=(800, 490))