from Scripts.cadastrar_caminho import caminho
import PySimpleGUI as sg

class FrtCam:
    def tela():
        sg.theme('DefaultNoMoreNagging')
        layout = [
            [sg.Frame('informe o caminho onde ficará o backup do banco de dados',
                [
                    [sg.Button('Procurar', key='-PROCURAR-', size=(100,1), button_color=("White", "#FF8C01"))],
                ], size=(500, 100)
            )],

            [sg.Frame('Já tem um caminho cadastrado? Informe um novo caminho',
                [
                    [sg.Button('Editar Caminho', key='-EDITAR-', size=(100,1), button_color=("White", "#FF8C01"))],
                ], size=(500, 100)
            )],
        ]
        return sg.Window('Caminho do backup', layout, size=(500, 400), finalize=True)
        
FrtCam.tela()