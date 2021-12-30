from openpyxl import load_workbook
from Scripts.xlsx_to_list import Xlsx_to_list

class DeleteOrder:
    def __init__(self, order_id, customer_list):
        self.order_id = order_id
        self.customer_list = customer_list
    
    def deletar_encomenda(self):
        arquivo = load_workbook("dados.xlsx")
        planilha = arquivo.active
        
        def get_real_index(lista_encomenda, index_encomenda):
            encomenda = lista_encomenda[int(index_encomenda[0])]
            id_encomenda = encomenda[1]
            return int(int(id_encomenda) + 1)

        index = get_real_index(self.customer_list, self.order_id)

        planilha.delete_rows(index)
        arquivo.save("dados.xlsx")
        self.atualizar_id_tabela()

    def atualizar_id_tabela(self):
        arquivo = load_workbook("dados.xlsx")
        planilha = arquivo.active

        id = Xlsx_to_list("A").toListNum()

        for i in range(len(id)):
            planilha.cell(row=i+2, column=1).value = i + 1
        
        arquivo.save("dados.xlsx")



