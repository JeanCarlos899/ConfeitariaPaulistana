import PySimpleGUI as sg
   
class NovaEncomenda:
    def nova_encomenda():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Nova encomenda", justification="center", font=("Helvetica", 15))],
            [sg.Checkbox("Bolo de aniversário", key="bolo_aniversario")],
            [sg.Checkbox("Bolo de casamento", key="bolo_casamento")],
            [sg.Checkbox("Salgadinhos", key="salgadinhos")],
            [sg.Text("Informações do pedido:")],
            [sg.InputText(key="info_pedido", size=(115, 10))],
            [sg.Button("Confirmar", size=(100,2))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Nova encomenda", layout=layout, finalize=True)

    def salgadinhos():
        sg.theme("Dark Blue 3")
        layout = [
            [sg.Text("Salgadinhos", font=("Helvetica", 15))],
            [sg.Checkbox("Tamanho mini:   ", key="mini"), sg.InputText(key="qtd_mini", size=(10,1))],
            [sg.Checkbox("Tamanho normal", key="normal"), sg.InputText(key="qtd_normal", size=(10,1))],
            [sg.Button("Voltar", size=(30,2)), sg.Button("Confirmar", size=(30,2))],
        ]
        return sg.Window("Salgadinhos", layout=layout, finalize=True)
        
    def dados_encomenda():
        sg.theme('Dark Blue 3')
        layout = [
            #input para nome do cliente, data de entrega e peso do bolo
            [sg.Text("Nome do cliente:")],
            [sg.InputText(key="nome_cliente", size=(115,2))],
            [sg.Text("Data de entrega:")],
            [sg.InputText(key="data_entrega", size=(115,2))],
            [sg.Text("Peso do bolo (aproximado): *o valor final será calculado ao final da encomenda")],
            [sg.InputText(key="peso", size=(115,2))],
            [sg.Button("Confirmar", size=(100,2))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Informações", layout=layout, finalize=True)