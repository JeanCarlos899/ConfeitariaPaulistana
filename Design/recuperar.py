import PySimpleGUI as sg
import os
import shutil

class Recuperar:
    def escolher_arquivo():
        try:
            sg.theme('Default1')
            file = sg.popup_get_file('Escolha o arquivo que deseja recuperar')

            if file == None:
                pass
            else:
                if file[-3:] != '.db':
                    sg.popup('O arquivo deve ser do formato .db')
                    file = Recuperar.escolher_arquivo()

                else:
                    if os.path.exists(file):
                        if os.path.exists('dados.db'):
                            os.remove('dados.db')

                        shutil.copy(file, 'dados.db')
                    else:
                        sg.popup('Arquivo não encontrado')
            
        except:
            sg.popup('Não foi escolhido um arquivo')

        return file


