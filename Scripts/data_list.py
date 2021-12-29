from Scripts.xlsx_to_list import Xlsx_to_list

class DataList:
    def __init__(self, tipo):
        self.tipo = tipo
        self.id = Xlsx_to_list("A").toListStr()
        self.nome = Xlsx_to_list("B").toListStr()
        self.data_entrega = Xlsx_to_list("C").toListStr()
        self.hora_entrega = Xlsx_to_list("D").toListStr()
        self.bolo_aniversario = Xlsx_to_list("E").toListStr()
        self.bolo_casamento = Xlsx_to_list("F").toListStr()
        self.salgado_mini = Xlsx_to_list("G").toListStr()
        self.salgado_normal = Xlsx_to_list("H").toListStr()
        self.valor_final = Xlsx_to_list("I").toListStr()
        self.mensagem = Xlsx_to_list("J").toListStr()
        self.status = Xlsx_to_list("K").toListStr()
    
    def get_dados_pedido_resumido(self):
        lista = []
        cont = 1

        for valor in range(len(self.id)):
            if self.status[valor] == self.tipo:
                lista.append([cont, self.id[valor], self.nome[valor], self.data_entrega[valor], self.hora_entrega[valor]])
                cont += 1
        return lista
 
    def get_dados_pedido(self, tem_msg = False):
        lista = []
        if tem_msg == False:
            for valor in range(len(self.id)):
                if self.status[valor] == self.tipo:
                    lista.append(
                        [
                            str(self.bolo_aniversario[valor]), 
                            str(self.bolo_casamento[valor]), 
                            str(self.salgado_mini[valor]), 
                            str(self.salgado_normal[valor]), 
                            str(self.valor_final[valor]), 
                            str(self.status[valor])
                        ]
                    )   
            return lista
        if tem_msg == True:
            for valor in range(len(self.id)):
                if self.status[valor] == self.tipo:
                    lista.append(str(self.mensagem[valor]))
            return lista
