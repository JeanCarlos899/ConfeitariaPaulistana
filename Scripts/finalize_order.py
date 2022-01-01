from openpyxl import load_workbook
from Scripts.get_real_index import GetRealIndex

class FinalizeOrder:
    def __init__(self, lista_encomenda, index_encomenda, kg_aniversario, kg_casamento):
        self.lista_encomendas = lista_encomenda
        self.index_encomenda = index_encomenda
        self.kg_aniversario = kg_aniversario
        self.kg_casamento = kg_casamento

    def get_preco_final(self):
        arquivo = load_workbook("dados.xlsx")
        planilha_ativa = arquivo.active
        
        index = GetRealIndex(self.lista_encomendas, self.index_encomenda).return_index()

        qtd_salgadinho_mini = planilha_ativa[f"G{index}"].value
        qtd_salgadinho_normal = planilha_ativa[f"H{index}"].value

        preco_final = ((float(self.kg_aniversario) * 5) 
                        + (float(self.kg_casamento) * 10) 
                        + (float(qtd_salgadinho_mini) * 0.35) 
                        + (float(qtd_salgadinho_normal) * 0.75))
        
        planilha_ativa[f"I{index}"] = preco_final
        planilha_ativa[f"K{index}"] = "Concluído"
        arquivo.save("dados.xlsx")

        return preco_final