from tkinter import filedialog
import os
from click import option

keys_caminho = 'caminhos.csv'

class caminho:
    def criar():
        if os.stat(keys_caminho).st_size == 0:
            pasta = filedialog.askdirectory()
            with open(keys_caminho, 'w') as arquivo:
                arquivo.write(pasta + '/backup_dados.db\n')

        else:
            localOriginal = 'dados.db'
            # Descobrir o caminho
            with open(keys_caminho, 'r') as arquivo:
                caminhos = arquivo.readlines()
                caminhos = [x.strip() for x in caminhos]


    def editar():
        with open(keys_caminho, 'r') as arquivo:
            caminhos = arquivo.readlines()
            caminhos = [x.strip() for x in caminhos]
        return caminhos

test = caminho.criar()