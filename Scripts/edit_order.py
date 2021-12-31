from openpyxl import load_workbook, Workbook

class EditOrder:
    def __init__(self, order_id, customer_list, nome_cliente:str, 
                data_entrega:str, horario_entrega:str, qtd_aniversario:int, 
                qtd_casamento:int, qtd_salgadinho_mini:int, qtd_salgadinho_normal:int, 
                info_complementares:str, status:str):

        self.order_id = order_id
        self.customer_list = customer_list
        self.nome_cliente = nome_cliente
        self.data_entrega = data_entrega
        self.horario_entrega = horario_entrega
        self.qtd_aniversario = qtd_aniversario
        self.qtd_casamento = qtd_casamento
        self.qtd_salgadinho_mini = qtd_salgadinho_mini
        self.qtd_salgadinho_normal = qtd_salgadinho_normal
        self.info_complementares = info_complementares
        self.status = status
    
    def editar_encomenda(self):
        dados = load_workbook("dados.xlsx")
        planilha_ativa = dados.active

        def get_real_index(lista_encomenda, index_encomenda):
            encomenda = lista_encomenda[int(index_encomenda[0])]
            id_encomenda = encomenda[1]
            return int(int(id_encomenda) + 1)

        index = get_real_index(self.customer_list, self.order_id)
        
        planilha_ativa[f"A{index}"] = index - 1
        planilha_ativa[f"B{index}"] = self.nome_cliente
        planilha_ativa[f"C{index}"] = self.data_entrega
        planilha_ativa[f"D{index}"] = self.horario_entrega
        planilha_ativa[f"E{index}"] = self.qtd_aniversario
        planilha_ativa[f"F{index}"] = self.qtd_casamento
        planilha_ativa[f"G{index}"] = self.qtd_salgadinho_mini
        planilha_ativa[f"H{index}"] = self.qtd_salgadinho_normal
        planilha_ativa[f"J{index}"] = self.info_complementares
        planilha_ativa[f"K{index}"] = self.status
        
        dados.save("dados.xlsx")