import os
import time
import shutil
import sys

localOriginal = 'dados.db'
novolocal = 'C:\\Users\\Rodrigues\\Desktop\\dados.db'

class Sicronizar:
    def __init__(self, localOriginal, novolocal):
        self.localOriginal = localOriginal
        self.novolocal = novolocal
    
    @property
    def localOriginal(self):
        return self._localOriginal

    @localOriginal.setter
    def localOriginal(self, localOriginal):
        self._localOriginal = localOriginal

    @property
    def novolocal(self):
        return self._novolocal

    @novolocal.setter
    def novolocal(self, novolocal):
        self._novolocal = novolocal

    def sincronizar(self):
        if os.path.exists(self.localOriginal):
            shutil.copy(self.localOriginal, self.novolocal)
            print('Arquivo copiado com sucesso!')
        else:
            print('Arquivo não encontrado!')

teste = Sicronizar(localOriginal, novolocal)
teste.sincronizar()