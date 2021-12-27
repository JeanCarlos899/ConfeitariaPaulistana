import PySimpleGUI as sg 
try:
    from Scripts.xlsx_to_list import Xlsx_to_list
except ImportError:
    pass
 
class ListarEncomendas:
    def get_dados_pedido(x):
        bolo_aniversario = Xlsx_to_list("E").toListStr()
        bolo_casamento = Xlsx_to_list("F").toListStr()
        salgado_mini = Xlsx_to_list("G").toListStr()
        salgado_normal = Xlsx_to_list("H").toListStr()
        valor_final = Xlsx_to_list("I").toListStr()
        mensagem = Xlsx_to_list("J").toListStr()
        status = Xlsx_to_list("K").toListStr()

        lista = []
        
        for valor in range(len(bolo_aniversario)):
            if x == 1:
                lista.append(
                    [
                        str(bolo_aniversario[valor]), 
                        str(bolo_casamento[valor]), 
                        str(salgado_mini[valor]), 
                        str(salgado_normal[valor]), 
                        str(valor_final[valor]), 
                        str(status[valor])
                    ]
                )
            else:
                lista.append(str(mensagem[valor]))
        return lista

    def valores_tabela(tipo):
        try:
            lista = []

            id = Xlsx_to_list("A").toListStr()
            nome = Xlsx_to_list("B").toListStr()
            data_entrega = Xlsx_to_list("C").toListStr()
            hora_entrega = Xlsx_to_list("D").toListStr()
            status = Xlsx_to_list("K").toListStr()

            cont = 1

            for valor in range(len(id)):
                if status[valor] == tipo:
                    lista.append([str(cont), str(id[valor]), nome[valor], data_entrega[valor], hora_entrega[valor]])
                    cont += 1
            return lista
        except:
            return ['', '', '', '', '']

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
                                num_rows=20, key='index_encomenda')
                    ],
                    [sg.Button('Voltar', size=(46, 2)), sg.Button('Mais informações', size=(46, 2))]
                    
                ], size=(800, 400)
            )]
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True, size=(800, 490))

    def mais_informacoes(cliente_selecionado, index_da_lista):
        sg.theme('Dark Blue 3')
        
        #informações do cliente e horários
        data_values = [cliente_selecionado]
        data_headings = ['Nº', 'ID', 'Nome Cliente', 'Data entrega', 'Hora entrega']
        data_cols_width = [5, 5, 35, 20, 18]

        #informações da encomenda
        data_values_encomenda = [ListarEncomendas.get_dados_pedido(1)[index_da_lista]]
        data_headings_encomenda = ['Bolo aniverário', 'Bolo casamento', 'Salgado mini', 'Salgado normal', 'Valor final', 'Status']
        data_cols_width_encomenda = [14, 14, 14, 14, 14, 14]
        mensagem = str(ListarEncomendas.get_dados_pedido(0)[index_da_lista]) 
        
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
                    [sg.Button('Voltar', size=(100, 2))]
                ], size=(800, 500)
            )]
        ]
        return sg.Window("Mais informações", layout=layout, finalize=True, size=(800, 500)) 

if __name__ == "__main__":
    janela = ListarEncomendas.listar_encomendas("Pendente")

    while True:
        janela, evento, valor = sg.read_all_windows()
        if evento == sg.WIN_CLOSED:
            break