# from openpyxl import load_workbook
import PySimpleGUI as sg


import PySimpleGUI as sg
   
class ListarEncomendas:
    def listar_encomendas():
        sg.theme('Dark Blue 3')

        data_values = [['1', 'Jean Carlos', '20/20/2020', '10:45'], ['2', 'Carlos', '20/20/0220', '10:20']]
        data_headings = ['ID', 'Nome Cliente', 'Data entrega', 'Hora entrega']
        data_cols_width = [5, 40, 20, 18]

        layout = [ 
            [sg.Frame('Filtros',
                [
                    [
                        sg.Text("De:"), 
                        sg.Combo(['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']),
                        sg.Text("Até:"), 
                        sg.Combo(['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']),
                        sg.Text("Ano:"),
                        sg.Combo(["2022", "2021", "2020"], default_value="2021"),
                        sg.Radio("Pendentes", "status", default=True, key="pendentes"),
                        sg.Radio("Entregues", "status", key="entregues"),
                        sg.Button("Filtrar", size=(50, 1))
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
                    [sg.Button('Voltar', size=(46, 2)), sg.Button('Mais informções', size=(46, 2))]
                    
                ], size=(800, 400)
            )]
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True, size=(800, 490))

if __name__ == "__main__":
    janela = ListarEncomendas.listar_encomendas()

    while True:
        janela, evento, valor = sg.read_all_windows()
        if evento == sg.WIN_CLOSED:
            break


