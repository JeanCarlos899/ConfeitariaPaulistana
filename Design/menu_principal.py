import PySimpleGUI as sg

class MenuPrincipal:
    def menu_principal():
        sg.theme('Default1')

        layout = [
            [sg.Frame('', 
                [
                    [
                        sg.Button(image_filename="Design/Images/nova_encomenda.png", image_size=(65, 65), key="Nova encomenda", border_width=3, pad=(2,2), button_color=("#E8E5EA", "#E8E5EA")),
                        sg.Button(image_filename="Design/Images/listar_encomenda.png", image_size=(65, 65), key="Listar encomendas", border_width=3, pad=(2,2),button_color=("#E8E5EA", "#E8E5EA")),
                        sg.Button(image_filename="Design/Images/baixa_encomenda.png", image_size=(65, 65), key="Dar baixa em encomenda", border_width=3, pad=(2,2), button_color=("#E8E5EA", "#E8E5EA")),
                        sg.Button(image_filename="Design/Images/relatorios.png", image_size=(65, 65), key="relatorios", border_width=3, pad=(2,2), button_color=("#E8E5EA", "#E8E5EA")),
                        sg.Button(image_filename="Design/Images/graficos.png", image_size=(65, 65), key="graficos", border_width=3, pad=(2,2), button_color=("#E8E5EA", "#E8E5EA")),
                        sg.Button(image_filename="Design/Images/editar_encomenda.png", image_size=(65, 65), key="editar_encomenda", border_width=3, pad=(2,2), button_color=("#E8E5EA", "#E8E5EA")),
                        sg.Button(image_filename="Design/Images/deletar_encomenda.png", image_size=(65, 65), key="deletar_encomenda", border_width=3, pad=(2,2), button_color=("#E8E5EA", "#E8E5EA")),
                        sg.Button(image_filename="Design/Images/sair.png", image_size=(65, 65), key="Sair",border_width=3, pad=(2,2), button_color=("#E8E5EA", "#E8E5EA"))
                    ],
                    
                    [
                        sg.Text("Nova\nencomenda", font=(None, 8), background_color="#EEAD2D", justification="center", size=(11, 2), pad=(2, 0)),
                        sg.Text("Listar\nEncomendas", font=(None, 8), background_color="#EEAD2D", justification="center", size=(11, 2), pad=(2, 0)),
                        sg.Text("Finalizar\nEncomenda", font=(None, 8), background_color="#EEAD2D", justification="center", size=(11, 2), pad=(2, 0)),
                        sg.Text("Relatórios\nde vendas", font=(None, 8), background_color="#EEAD2D", justification="center", size=(11, 2), pad=(2, 0)),
                        sg.Text("Gráficos\nde vendas", font=(None, 8), background_color="#EEAD2D", justification="center", size=(11, 2), pad=(2, 0)),
                        sg.Text("Editar\nencomenda", font=(None, 8), background_color="#EEAD2D", justification="center", size=(11, 2), pad=(2, 0)),
                        sg.Text("Deletar\nencomenda", font=(None, 8), background_color="#EEAD2D", justification="center", size=(11, 2), pad=(2, 0)),
                        sg.Text("Sair", font=(None, 8), background_color="#EEAD2D", justification="center", size=(11, 2), pad=(2, 0))
                    ]
                ], border_width=2, background_color="#EEAD2D", size=(1366, 115), pad=(0,0), element_justification="left")
            ],
        
            [sg.Image(filename="Design/Images/logo.png", size=(1366, 500), key="logo")],

            [
                sg.Text("Um produto desenvolvido por JD technology® e licenciado para Confeitaria Paulistana.\nTelefone para suporte: 0800-000-1234\nsuporte@jdtechnology.com.br", 
                font=(None, 10), justification="center", size=(1366, 3), pad=(2, 0))
            ]
        ]

        return sg.Window("Confeitaria Paulistana", layout=layout, finalize=True, resizable=True, size=(1366,768), margins=(0,0))