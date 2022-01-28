from turtle import color
import PySimpleGUI as sg
import os
from click import option

keys_caminho = 'caminhos.csv'

class Criar:
    def criar():
        # Se for escolhido um local faça, se não, não faça nada
        try:
            if os.stat(keys_caminho).st_size == 0:
                sg.theme('Default1')
                pasta = sg.PopupGetFolder('Escolha a pasta de destino')
                with open(keys_caminho, 'w') as arquivo:
                    arquivo.write(pasta + '/backup_dados.db\n')
                
                sg.Popup('Caminho cadastrado com sucesso!', 'Aperte OK para continuar')

            else:
                sg.popup('Já existe um caminho cadastrado, você pode editá-lo')

                with open(keys_caminho, 'r') as arquivo:
                    caminho = arquivo.read()

                pasta = caminho

        except:
            sg.popup('Não foi escolhido um caminho')

        return pasta
        

class Editar:
    def editar():
        os.remove(keys_caminho)
        try:
            sg.theme('Default1')
            pasta = sg.PopupGetFolder('Escolha a pasta de destino')
            with open(keys_caminho, 'w') as arquivo:
                arquivo.write(pasta + '/backup_dados.db\n')

            sg.popup('Caminho editado com sucesso!', 'Aperte OK para continuar')

        except:
            sg.popup('Não foi escolhido um local')

        return pasta
