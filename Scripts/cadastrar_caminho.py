from turtle import color
import PySimpleGUI as sg
import os
from click import option

keys_caminho = 'caminhos.csv'

class Criar:
    def criar():
        if os.stat(keys_caminho).st_size == 0:
            sg.theme('Default1')
            pasta = sg.PopupGetFolder('Escolha a pasta de destino')
            with open(keys_caminho, 'w') as arquivo:
                arquivo.write(pasta + '/backup_dados.db\n')

        else:
            localOriginal = 'dados.db'
            # Descobrir o caminho
            with open(keys_caminho, 'r') as arquivo:
                caminhos = arquivo.readlines()
                caminhos = [x.strip() for x in caminhos]

class Editar:
    def editar():
        os.remove(keys_caminho)

        sg.theme('Default1')
        pasta = sg.PopupGetFolder('Escolha a pasta de destino')
        with open(keys_caminho, 'w') as arquivo:
            arquivo.write(pasta + '/backup_dados.db\n')

Criar.criar()