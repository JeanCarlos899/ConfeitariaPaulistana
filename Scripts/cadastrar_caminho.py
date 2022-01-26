from tkinter import filedialog
import os
from click import option

keys_caminho = 'caminhos.csv'

class caminho:
    def criar():
        if os.stat(keys_caminho).st_size == 0:
            pasta = filedialog.askdirectory()
            with open(keys_caminho, 'w') as arquivo:
                arquivo.write(pasta + '\n')

        else:
            localOriginal = 'dados.db'
            novolocal = keys_caminho

        return novolocal, localOriginal

    def editar():
        with open(keys_caminho, 'r') as arquivo:
            caminhos = arquivo.readlines()
            caminhos = [x.strip() for x in caminhos]
        return caminhos
