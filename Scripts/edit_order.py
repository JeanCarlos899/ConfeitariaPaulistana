from openpyxl import load_workbook
from Scripts.get_real_index import GetRealIndex
from datetime import datetime

class EditOrder:
    def __init__(self, order_id, lista_clientes, lista_dados: list, status):
        self.lista_dados = lista_dados
        self.order_id = order_id
        self.lista_clientes = lista_clientes
        self.status = status

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

    def editar_encomenda(self) -> bool:
        dados = load_workbook("dados.xlsx")
        planilha_ativa = dados.active

        index = GetRealIndex(self.lista_clientes, self.order_id).return_index()

        if self.lista_dados[0] != "":
            if self.verificar_data(self.lista_dados[2], self.lista_dados[1]) == True:
                if int(self.lista_dados[3]) >= 0 and int(self.lista_dados[4]) >= 0:
                    if (int(self.lista_dados[5]) + int(self.lista_dados[6]) >= 25 
                        or int(self.lista_dados[5]) + int(self.lista_dados[6]) == 0):
                        letras = ["B", "C", "D", "E", "F", "G", "H", "J"]
                        
                        planilha_ativa[f"A{index}"] = index - 1
                        for i in range(len(self.lista_dados)):
                            planilha_ativa[letras[i] + str(index)] = self.lista_dados[i]
                        planilha_ativa[f"K{index}"] = self.status

                        dados.save("dados.xlsx")
                        return "Dados atualizados com sucesso!"
                    else:
                        return "O valor total dos salgadinhos devem ser igual ou maior que 25"
                else:
                    return "O valor total dos bolos devem ser maior que 0"
            else:
                return "A data de entrega deve ser maior ou igual a data atual"
        else:
            return "Preencha todos os campos"