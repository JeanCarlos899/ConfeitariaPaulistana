import PySimpleGUI as sg

class MenuPrincipal:
    def menu_principal():
        sg.theme('Dark Blue 3')
        layout = [
            # [sg.Text("CONFEITARIA PAULISTANA - MENU PRINCIPAL", justification="center", font=("Helvetica", 15), size=(1366, 1))],
            [
                sg.Button(image_filename="Design/Images/nova_encomenda.png", image_size=(80, 80), key="Nova encomenda", border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/listar_encomenda.png", image_size=(80, 80), key="Listar encomendas", border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/baixa_encomenda.png", image_size=(80, 80), key="Dar baixa em encomenda", border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/branco.png", image_size=(80, 80), border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/branco.png", image_size=(80, 80), border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/branco.png", image_size=(80, 80), border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/branco.png", image_size=(80, 80), border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/branco.png", image_size=(80, 80), border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/branco.png", image_size=(80, 80), border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/branco.png", image_size=(80, 80), border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/branco.png", image_size=(80, 80), border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/branco.png", image_size=(80, 80), border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/branco.png", image_size=(80, 80), border_width=3, button_color=("#808080", "#808080")),
                sg.Button(image_filename="Design/Images/sair.png", image_size=(80, 80), key="Sair", border_width=3, button_color=("#808080", "#808080")),
            ],
            [sg.Text("", background_color="white", size=(1366, 37))],
        ]
        return sg.Window("Confeitaria Paulistana", layout=layout, finalize=True, resizable=True, size=(1366,768), margins=(10,0))