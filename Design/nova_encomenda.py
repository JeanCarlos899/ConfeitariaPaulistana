import PySimpleGUI as sg
   
class NovaEncomenda:
    def nova_encomenda():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Nova encomenda", justification="center", font=("Helvetica", 15))],

            [sg.Text("Nome do cliente:")],
            [sg.InputText(key="nome_cliente", size=(115,2))],
            [sg.Text("Data de entrega:")],
            [sg.InputText(key="data_entrega", size=(115,2))],
            [sg.Text("", font=("Helvetica", 1))],
            
            [sg.Text("Tipo                                 Quantidade")],

            [sg.Text("Bolos:", font=("Helvetica", 14))],
            [sg.Text("Bolo de aniversário", font=("Helvetica", 11)), sg.Text("    ", font=("Helvetica", 2)), sg.InputText(key="bolo_aniversario", default_text=0 , size=(10,1))],
            [sg.Text("Bolo de casamento", font=("Helvetica", 11)), sg.Text("  ", font=("Helvetica", 2)), sg.InputText(key="bolo_casamento", default_text=0, size=(10,1))],   
        
            [sg.Text("Salgadinhos:", font=("Helvetica", 14))],
            [
                sg.Text("Tamanho mini", font=("Helvetica", 11)),
                sg.Text("                 ", font=("Helvetica", 5)),
                sg.InputText(key="qtd_mini", size=(10,1), default_text=0),
            ],
            [
                sg.Text("Tamanho normal", font=("Helvetica", 11)),
                sg.Text("        ", font=("Helvetica", 5)),
                sg.InputText(key="qtd_normal", size=(10,1), default_text=0)
            ],

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