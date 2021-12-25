import PySimpleGUI as sg
#set the theme for the screen/window
sg.theme("DarkTanBlue")
#define layout
[sg.Frame('Choose your Bread',[[sg.Button(image_filename="Design/Images/nova_encomenda.png", image_size=(80, 80), key="Nova encomenda", border_width=3, button_color=("#808080", "#808080")),
                                        sg.Button(image_filename="Design/Images/listar_encomenda.png", image_size=(80, 80), key="Listar encomendas", border_width=3, button_color=("#808080", "#808080")),
                                        sg.Button(image_filename="Design/Images/baixa_encomenda.png", image_size=(80, 80), key="Dar baixa em encomenda", border_width=3, button_color=("#808080", "#808080")),
                                        sg.Button(image_filename="Design/Images/sair.png", image_size=(80, 80), key="Sair", border_width=3, button_color=("#808080", "#808080"))]],border_width=10)],
       