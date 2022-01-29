from datetime import datetime
from genericpath import exists
from Scripts.sqlite import SQLite

class InsertDados:
    def __init__(self, lista_dados: list):
        self.lista_dados = lista_dados

    def verificar_data(self, horario_entrega: str, data_entrega: str) -> bool:
        if horario_entrega.count(":") == 1:
            if len(horario_entrega.split(":")) == 2:
                try:
                    hora_entrada = datetime.strptime(
                        (str(data_entrega) + " " + str(horario_entrega)), "%d/%m/%Y %H:%M"
                        ).strftime("%d/%m/%Y %H:%M")
                    hora_atual = datetime.today().strftime('%d/%m/%Y %H:%M')
                    
                    if hora_entrada >= hora_atual:
                        return True
                except:
                    return False
            else:
                return False
        else:
            return False

    def __call__(self) -> str:
        if self.lista_dados[0] != "":
            if self.verificar_data(self.lista_dados[2], self.lista_dados[1]) == True:
                if int(self.lista_dados[3]) > 0 or int(self.lista_dados[4]) > 0:
                    if (int(self.lista_dados[5]) + int(self.lista_dados[6]) >= 25 
                        or int(self.lista_dados[5]) + int(self.lista_dados[6]) == 0):

                        SQLite('dados.db').insert(
                            "dados", 
                            f'''Null, 
                            '{self.lista_dados[0]}', 
                            '{self.lista_dados[1]}', 
                            '{self.lista_dados[2]}', 
                            '{self.lista_dados[3]}', 
                            '{self.lista_dados[4]}', 
                            '{self.lista_dados[5]}', 
                            '{self.lista_dados[6]}', 
                            Null, 
                            '{self.lista_dados[7]}',
                            'Pendente'
                            '''
                        ) 

                        return True
                    else:
                        return "O valor total dos salgadinhos devem ser igual ou maior que 25"
                else:
                    return "O valor total dos bolos devem ser maior que 0"
            else:
                return "A data de entrega deve ser maior ou igual a data atual"
        else:
            return "Preencha todos os campos"