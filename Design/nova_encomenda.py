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
                    [sg.Text("Hora de entrega: exemplo(10:53):")],
                    [sg.InputText(key="hora_entrega", size=(115,2))],
                ]
            )],
            [sg.Frame('Dados do pedido (obrigatório)',
                [
                    [sg.Frame('Bolos', 
                        [
                            [sg.Text("Bolo de aniversário:"), sg.InputText(key="bolo_aniversario")],
                            [sg.Text("Bolo de casamento:"), sg.InputText(key="bolo_casamento")],
                        ]    
                    )],

                    [sg.Frame('Salgadinhos', 
                        [
                            [sg.Text("Mini salgadinho:"), sg.InputText(key="qtd_mini")],
                            [sg.Text("Salgadinho normal:"), sg.InputText(key="qtd_normal")],
                        ]    
                    )],
                ]
            )],

            [sg.Text("Informações complementares do pedido:")],
            [sg.InputText(key="info_pedido", size=(115, 10))],

            [sg.Text("", font=("Helvetica", 1))],
            [sg.Button("Confirmar", size=(100,2))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Nova encomenda", layout=layout, finalize=True)

if __name__ == "__main__":
    janela = NovaEncomenda.nova_encomenda()

    while True:
        janela, evento, valor = sg.read_all_windows()
        if evento == sg.WIN_CLOSED:
            break