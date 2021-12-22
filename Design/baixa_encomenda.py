import PySimpleGUI as sg

class BaixaEncomenda:
    def baixa_encomenda():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Informe o número da encomenda: ")],
            [sg.InputText(key="numero_encomenda", size=(115,2))],
            [sg.Text("Informe o peso final da encomenda:")],
            [sg.InputText(key="peso_final", size=(115,2))],
            [sg.Button("Listar encomendas", size=(100,2))],
            [sg.Button("Confirmar", size=(100,2))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Dar baixa em encomenda", layout=layout, finalize=True)
        
    def confirmar_baixa(valor_final):
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text(f"O valor final da encomenda é: R$ {valor_final}", font=("Helvetica", 15))],
            [sg.Text("Deseja realmente dar baixa na encomenda?", font=("Time New Roman", 13))],
            [sg.Button("Sim", size=(45,2)), sg.Button("Não", size=(45,2))],
        ]
        return sg.Window("Confirmar baixa", layout=layout, finalize=True)