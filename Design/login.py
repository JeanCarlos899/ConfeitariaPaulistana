from Scripts.validade_login import validadeLogin
from Scripts.sqlite import SQLite
import PySimpleGUI as sg

class Login:
    def __init__(self):
        self.initializeSQLite = SQLite("dados.db")
        pass

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

    def newAccount():
        sg.theme("DefaultNoMoreNagging")

        layout = [
            [sg.Text("Cadastro", size=(100, 1), font=("Helvetica", 25), justification="center")],
            [sg.Frame("Login de administrador", 
                [
                    [sg.Text("Usuário:", size=(20, 1))],
                    [sg.InputText(key="-ADMIN-USERNAME-", size=(100, 1))],
                    [sg.Text("Senha:", size=(15, 1))],
                    [sg.InputText(key="-ADMIN-PASSWORD-", size=(100, 1), password_char="*")],
                    [sg.Text("")],
                ]
            )],
            [sg.Frame("Dados do usuário a ser cadastrado",
                [
                    [sg.Text("Usuário:", size=(15, 1))],
                    [sg.InputText(key="-USERNAME-", size=(100, 1))],
                    [sg.Text("Senha:", size=(15, 1))],
                    [sg.InputText(key="-PASSWORD-", size=(100, 1), password_char="*")],
                    [sg.Text("")],
                    [sg.Button("Cadastrar", size=(100, 2), button_color=("White", "#027F9E"), border_width=0)],
                    [sg.Text(" ", font=("Arial", 5))],
                    [
                        sg.Text("Clique aqui para voltar ao login: "),
                        sg.Button("Login", size=(100, 1), button_color=("white", "green"), border_width=0)
                    ],
                    [sg.Frame("Tipo de usuário",
                        [
                            [
                                sg.Radio("Administrador", "tipo", size=(15, 1), key="-ADMIN-"), 
                                sg.Radio("Funcionário", "tipo", default=True, size=(15, 1), key="-FUNCIONARIO-")
                            ]
                        ], size=(600, 60)
                    )],
                ]
            )],
            [sg.Text("_________________________________________________________________________________", text_color="#FF8C01")],
            [sg.Text(" ", font=("Arial", 5))],
            [
                sg.Text("Um produto desenvolvido por JD technology® e licenciado para Confeitaria Paulistana.\nTelefone para suporte: 0800-000-1234\nsuporte@jdtechnology.com.br", 
                font=(None, 10), justification="center", size=(1366, 3))
            ]
        ]
        return sg.Window("Confeitaria Paulistana", layout=layout, finalize=True, size=(550, 640))
            

    def __call__(self):
        login = Login.loginWindow()
        newAccount = None
        while True:
            window, event, values = sg.read_all_windows()
            if window == login:
                if event == sg.WIN_CLOSED:
                    break
                elif event == "Logar":
                    token = validadeLogin(values["-USERNAME-"], values["-PASSWORD-"])

                    if token():
                        window.close()
                        return True
                    else:
                        sg.popup("Usuário ou senha incorretos. Tente novamente.")
                    
                elif event == "Nova conta":
                    login.hide()
                    newAccount = Login.newAccount()
            
            if window == newAccount:
                if event == sg.WIN_CLOSED:
                    break
                elif event == "Login":
                    newAccount.close()
                    login.un_hide()
                
                elif event == "Cadastrar":
                    adminUsername = values["-ADMIN-USERNAME-"]
                    adminPassword = values["-ADMIN-PASSWORD-"]

                    username = values["-USERNAME-"]
                    password = values["-PASSWORD-"]

                    if values["-ADMIN-"] == True:
                        tipo = "admin"

                    elif values["-FUNCIONARIO-"] == True:
                        tipo = "funcionario"

                    if validadeLogin(username, password).newAccount(adminUsername, adminPassword, tipo) == True:
                        sg.popup("Cadastro realizado com sucesso. ")
                        newAccount.close()
                        login.un_hide()
                    else:
                        sg.popup("O usuário não tem permissão para criar novos usuários.")