from openpyxl import load_workbook
import PySimpleGUI as sg


class PrecoFinal:
    def __init__(self, id, kg_aniversario, kg_casamento):
        self.id = id
        self.kg_aniversario = kg_aniversario
        self.kg_casamento = kg_casamento
    
    def modificar_status(self):
        arquivo = load_workbook("dados.xlsx")
        planilha_ativa = arquivo.active

        qtd_salgadinho_mini = planilha_ativa[f"F{int(self.id) + 1}"].value
        qtd_salgadinho_normal = planilha_ativa[f"G{int(self.id) + 1}"].value

        preco_final = (float(self.kg_aniversario) * 5) + (float(self.kg_casamento) * 10) + (float(qtd_salgadinho_mini) * 0.35) + (float(qtd_salgadinho_normal) * 0.75)

        planilha_ativa[f"H{int(self.id) + 1}"] = preco_final
        planilha_ativa[f"I{int(self.id) + 1}"] = "Concluído"

        arquivo.save("dados.xlsx")

        return preco_final
