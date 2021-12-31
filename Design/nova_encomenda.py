import PySimpleGUI as sg
   
class NovaEncomenda:
    def nova_encomenda(titulo):
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
        return sg.Window(titulo, layout=layout, finalize=True, size=(800, 520))