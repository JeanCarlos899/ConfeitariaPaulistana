import PySimpleGUI as sg 
try:
    from Scripts.xlsx_to_list import Xlsx_to_list
except ImportError:
    pass
 
class ListarEncomendas:
    def valores_tabela(tipo):
        try:
            lista = []

            id = Xlsx_to_list("A").toListNum()
            nome = Xlsx_to_list("B").toListStr()
            data_entrega = Xlsx_to_list("C").toListStr()
            hora_entrega = Xlsx_to_list("D").toListStr()
            status = Xlsx_to_list("K").toListStr()

            cont = 1

            for valor in range(len(id)):
                if status[valor] == tipo:
                    lista.append([cont, id[valor], nome[valor], data_entrega[valor], hora_entrega[valor]])
                    cont += 1
            return lista
        except:
            return ['', '', '', '']

    def listar_encomendas(tipo):
        sg.theme('Dark Blue 3')

        data_values = ListarEncomendas.valores_tabela(tipo)
        data_headings = ['Nº', 'ID', 'Nome Cliente', 'Data entrega', 'Hora entrega']
        data_cols_width = [5, 5, 35, 20, 18]

        layout = [ 
            [sg.Frame('Filtros',
                [
                    [
                        sg.Radio("Pendentes", "status", default=True, key="status_pendente"),
                        sg.Radio("Entregues", "status", key="status_concluido"),
                        sg.Button("Filtrar", size=(20, 1)),
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
                                num_rows=20, key='_filestable_')
                    ],
                    [sg.Button('Voltar', size=(46, 2)), sg.Button('Mais informações', size=(46, 2))]
                    
                ], size=(800, 400)
            )]
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True, size=(800, 490))

if __name__ == "__main__":
    janela = ListarEncomendas.listar_encomendas("Pendente")

    while True:
        janela, evento, valor = sg.read_all_windows()
        if evento == sg.WIN_CLOSED:
            break