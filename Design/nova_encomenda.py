import PySimpleGUI as sg
   
class NovaEncomenda:
    def nova_encomenda(titulo):
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
        return sg.Window(titulo, layout=layout, finalize=True, size=(800, 520), background_color="#e0e0e0")



