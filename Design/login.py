from Scripts.validade_login import validadeLogin
from Scripts.sqlite import SQLite
import PySimpleGUI as sg

class Login:
    def __init__(self):
        self.initializeSQLite = SQLite("dados.db")

    def loginWindow():
        sg.theme("DefaultNoMoreNagging")

        layout = [
  
            [sg.Text("Login", size=(100, 1), font=("Helvetica", 25), justification="center")],
            [sg.Text("Usuário:", size=(15, 1))],
            [sg.InputText(key="-USERNAME-", size=(100, 1))],
            [sg.Text("Senha:", size=(15, 1))],
            [sg.InputText(key="-PASSWORD-", size=(100, 1), password_char="*")],
            [sg.Text("")],
            [sg.Button("Logar", size=(100, 2), button_color=("White", "#027F9E"), border_width=0)],
     
            [sg.Text(" ", font=("Arial", 5))],

            [
                sg.Text("Clique aqui para criar novo cadastro: "),
                sg.Button("Nova conta", size=(100, 1), button_color=("white", "green"), border_width=0)
            ],
            [sg.Text("_________________________________________________________________________________", text_color="#FF8C01")],
            [sg.Text(" ", font=("Arial", 5))],
            [
                sg.Text("Um produto desenvolvido por JD technology® e licenciado para Confeitaria Paulistana.\nTelefone para suporte: 0800-000-1234\nsuporte@jdtechnology.com.br", 
                font=(None, 10), justification="center", size=(1366, 3))
            ]
        ]
        return sg.Window("Confeitaria Paulistana", layout=layout, finalize=True, size=(550, 400))

    def __call__(self):
        window = Login.loginWindow()
        while True:
            event, values = window.read()
            if event == "Logar":
                token = validadeLogin(values["-USERNAME-"], values["-PASSWORD-"])

                if token():
                    window.close()
                    return True
                else:
                    sg.popup("Usuário ou senha incorretos. Tente novamente.")
            elif event == sg.WIN_CLOSED:
                break