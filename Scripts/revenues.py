from Scripts.xlsx_to_list import Xlsx_to_list
from datetime import datetime

class Revenues:
    def __init__(self, data_inicial: str, data_final: str):
        self.data_inicial = data_inicial
        self.data_final = data_final

    def get_value(self) -> str:
        datas = Xlsx_to_list("C").toListStr()
        status = Xlsx_to_list("K").toListStr()
        valor = Xlsx_to_list("I").toListStr()

        valor_total = 0

        for i in range(len(datas)):
            try:
                data_lista = datetime.strptime(datas[i], '%d/%m/%Y').strftime("%d/%m/%Y")
                data_inicial = datetime.strptime(self.data_inicial, '%d/%m/%Y').strftime('%d/%m/%Y')
                data_final = datetime.strptime(self.data_final, '%d/%m/%Y').strftime('%d/%m/%Y')
            except:
                return "Erro nas datas, confira se estão no formato correto."
            if status[i] == "Concluído":
                if data_lista >= data_inicial and data_lista <= data_final:
                    valor_total += float(valor[i])

        return f"\nR$ {valor_total:.2f}"