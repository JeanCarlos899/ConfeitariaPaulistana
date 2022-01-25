from datetime import datetime
from Scripts.sqlite import SQLite

class EditDados:
    def __init__(self, lista_dados: list, id: int):
        self.lista_dados = lista_dados
        self.id = id

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

    def inserir_dados(self) -> str:
        if self.lista_dados[0] != "":
            if self.verificar_data(self.lista_dados[2], self.lista_dados[1]) == True:
                if int(self.lista_dados[3]) > 0 or int(self.lista_dados[4]) > 0:
                    if (int(self.lista_dados[5]) + int(self.lista_dados[6]) >= 25 
                        or int(self.lista_dados[5]) + int(self.lista_dados[6]) == 0):

                        col_name = [
                            'nome_cliente',
                            'data_entrega',
                            'hora_entrega',
                            'bolo_aniversario',
                            'bolo_casamento',
                            'salgado_mini',
                            'salgado_normal',
                            'mensagem'
                        ]

                        for i in range(len(col_name)):
                            SQLite('dados.db').update(
                                'dados',
                                col_name[i],
                                f'"{self.lista_dados[i]}"',
                                f'id = {self.id}'
                            )

                        return "Dados atualizados com sucesso!"
                    else:
                        return "O valor total dos salgadinhos devem ser igual ou maior que 25"
                else:
                    return "O valor total dos bolos devem ser maior que 0"
            else:
                return "A data de entrega deve ser maior ou igual a data atual"
        else:
            return "Preencha todos os campos"