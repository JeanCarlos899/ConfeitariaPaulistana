from tkinter import filedialog
import os
from click import option

keys_caminho = 'caminhos.csv'

if os.stat(keys_caminho).st_size == 0:
    pasta = filedialog.askdirectory()
    with open(keys_caminho, 'w') as arquivo:
        arquivo.write(pasta + '\n')

else:
    localOriginal = 'dados.db'
    novolocal = keys_caminho
