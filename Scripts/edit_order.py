from openpyxl import load_workbook
from Scripts.get_real_index import GetRealIndex
import datetime

class EditOrder:
    def __init__(self, order_id, lista_clientes, lista_dados: list, status):
        self.lista_dados = lista_dados
        self.order_id = order_id
        self.lista_clientes = lista_clientes
        self.status = status

    def verificar_data(self, data_entrega:str) -> bool:
        if data_entrega.count("/") == 2:
            if len(data_entrega.split("/")) == 3:
                try:
                    datetime.datetime.strptime(data_entrega, "%d/%m/%Y")
                    return True
                except:
                    return False
            else:
                return False
        else:
            return False

    def verificar_hora(self, horario_entrega:str) -> bool:
        if horario_entrega.count(":") == 1:
            if len(horario_entrega.split(":")) == 2:
                try:
                    datetime.datetime.strptime(horario_entrega, "%H:%M")
                    return True
                except:
                    return False
            else:
                return False
        else:
            return False

    def editar_encomenda(self) -> bool:
        dados = load_workbook("dados.xlsx")
        planilha_ativa = dados.active

        index = GetRealIndex(self.lista_clientes, self.order_id).return_index()

        if self.lista_dados[0] != "":
            if self.verificar_data(self.lista_dados[1]) and self.verificar_hora(self.lista_dados[2]) == True:
                if int(self.lista_dados[3]) >= 0 and int(self.lista_dados[4]) >= 0:
                    if (int(self.lista_dados[5]) + int(self.lista_dados[6]) >= 25 
                        or int(self.lista_dados[5]) + int(self.lista_dados[6]) == 0):
                        #   NOME       DATA       HORA        QTDS           MSG
                        # ['Jean', '02/05/2005', '00:00', 10, 20, 30, 40, ' Teste']
                        letras = ["B", "C", "D", "E", "F", "G", "H", "J"]
                        
                        planilha_ativa[f"A{index}"] = index - 1
                        for i in range(len(self.lista_dados)):
                            planilha_ativa[letras[i] + str(index)] = self.lista_dados[i]
                        planilha_ativa[f"K{index}"] = self.status
                        dados.save("dados.xlsx")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False