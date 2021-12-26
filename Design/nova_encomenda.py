import PySimpleGUI as sg
   
class NovaEncomenda:
    def nova_encomenda():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Frame('Dados do cliente e entrega (obrigatório)',
                [
                    [sg.Text("Nome do cliente:")],
                    [sg.InputText(key="nome_cliente", size=(115,2))],
                    [sg.Text("Data de entrega dd/mm/aaaa:")],
                    [sg.InputText(key="data_entrega", size=(115,2))],
                    [sg.Text("Hora de entrega:")],
                    [sg.InputText(key="horario_entrega", size=(115,2), default_text="00:00")],
                ], size=(800, 180)
            )],
            [
                sg.Frame('Dados do pedido (obrigatório)',
                    [
                        [sg.Frame('Bolos', 
                            [
                                [sg.Text("Bolo de aniversário:"), sg.Text("   ", font=(None, 1)), sg.InputText(key="bolo_aniversario", size=(100,1), default_text=0)],
                                [sg.Text("Bolo de casamento:"), sg.Text("", font=(None, 1)), sg.InputText(key="bolo_casamento", size=(100,1), default_text=0)],
                            ], size=(480, 80))
                        ],

                        [sg.Frame('Salgadinhos', 
                            [
                                [
                                    sg.Text("Mini salgadinho:"), 
                                    sg.Text("                     ", font=(None, 1)), sg.InputText(key="qtd_mini", size=(100,1), default_text=0)
                                ],
                                [
                                    sg.Text("Salgadinho normal:"), 
                                    sg.Text("    ", font=(None, 1)), sg.InputText(key="qtd_normal", size=(100,1), default_text=0)
                                ],
                            ], size=(480, 80))
                        ],
                    ], size=(500, 200)
                ),

                sg.Frame("Informações adicionais (opcional)",
                    [
                        [sg.Multiline(key="info_complementares", size=(100, 11))]
                    ], size=(400, 200)
                )
            ],
            
            [sg.Text("", font=("Helvetica", 1))],
            [sg.Button("Confirmar", size=(100,2))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Nova encomenda", layout=layout, finalize=True, size=(800, 520))

if __name__ == "__main__":
    janela = NovaEncomenda.nova_encomenda()

    while True:
        janela, evento, valor = sg.read_all_windows()
        if evento == sg.WIN_CLOSED:
            break