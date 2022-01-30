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
                    shutil.copy(file, 'dados.db')            
        except:
            sg.popup('Não foi escolhido nenhum arquivo')

        return file


