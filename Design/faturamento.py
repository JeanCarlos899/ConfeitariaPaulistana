import PySimpleGUI as sg
from datetime import datetime

class Faturamento:
    
    def faturamento():
        sg.theme('Default1')
        layout = [
            [sg.Frame("Filtros",
                [
                    [
                        sg.Text("De:"), sg.InputText(
                            key="-DATA_INICIAL-", size=(10, 1), default_text=datetime.now().strftime('01/%m/%Y')
                            ),
                        sg.Text("Até:"), sg.InputText(
                            key="-DATA_FINAL-", size=(10, 1), default_text=datetime.today().strftime("%d/%m/%Y")
                            ),
                        sg.Button("Filtrar", key="-FILTRAR-", size=(20, 1), button_color=("White", "#FF8C01"))
                    ], 
                ], size=(420, 60)
            )],
            [sg.Multiline(
                size=(50, 3), key="-VALOR_FATURAMENTO-", disabled=True, no_scrollbar=True, justification="center",
                font=("Times New Roman", 25, "bold"), background_color="#e0e0e0")],
            [sg.Button("Voltar", key="-VOLTAR-", size=(100, 2), button_color=("White", "#FF8C01"))]
        ]
        return sg.Window("Faturamento", layout=layout, finalize=True, size=(420, 250))

if __name__ == "__main__":
    janela = Faturamento.faturamento()

    while True:
        janela, evento, valor = sg.read_all_windows()
        if evento == sg.WIN_CLOSED:
            break



