from ctypes import alignment
import PySimpleGUI as sg

class FrtCam:
    def tela():
        sg.theme('DefaultNoMoreNagging')
        layout = [
            [sg.Frame('informe o caminho onde ficará o backup do banco de dados',
                [                    
                    [sg.Button(image_filename="Design/Images/escolher.png", button_color=("#E8E5EA", "#E8E5EA"), key="-PROCURAR-",image_size=(500, 100), pad=(5, 5))],
                    
                ], size=(500, 150)
            )],

            [sg.Frame('Já tem um caminho cadastrado? Informe um novo caminho',
                [
                    [sg.Button(image_filename="Design/Images/editar.png", button_color=("#E8E5EA", "#E8E5EA"), key="-EDITAR-",image_size=(500, 100), pad=(5, 5))],
    
              ], size=(500, 150)
            )],
            [sg.Button('Voltar', key='-VOLTAR-', size=(100,1), button_color=("White", "#FF8C01"))],
        ]
        return sg.Window('Caminho do backup', layout, size=(500, 400), finalize=True)
        