from Scripts.xlsx_to_list import Xlsx_to_list
import PySimpleGUI as sg


mensagem = Xlsx_to_list("J").toListStr()[3]

def tetla():
    layout = [
        [sg.Multiline(size=(800, 12), default_text=mensagem)],
    ]
    return sg.Window("Mais informações", layout=layout, finalize=True, size=(800, 500)) 

if __name__ == "__main__":
    janela = tetla()

    while True:
        janela, evento, valor = sg.read_all_windows()
        if evento == sg.WIN_CLOSED:
            break