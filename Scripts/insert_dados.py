from Scripts.xlsx_to_list import Xlsx_to_list
from openpyxl import load_workbook, Workbook

while True:
    try:
        teste = load_workbook("dados.xlsx")
        break
    except:
        wb = Workbook()
        ws = wb.active
        ws.title = "Dados"
        ws["A1"] = "ID"
        ws["B1"] = "Nome cliente"
        ws["C1"] = "Data de entrega"
        ws["D1"] = "Hora de entrega"
        ws["E1"] = "Bolo de aniversário"
        ws["F1"] = "Bolo de casamento"
        ws["G1"] = "Salgado mini"
        ws["H1"] = "Salgado normal"
        ws["I1"] = "Valor final"
        ws["J1"] = "Mensagem adicional"
        ws["K1"] = "Status"
        wb.save("dados.xlsx")
        continue

class InsertDados:
    def __init__(self, nome_cliente:str, data_entrega:str, horario_entrega:str, qtd_aniversario:int, qtd_casamento:int, qtd_salgadinho_mini:int, qtd_salgadinho_normal:int, info_complementares:str, status = "Pendente"):
        self.nome_cliente = nome_cliente
        self.data_entrega = data_entrega
        self.horario_entrega = horario_entrega
        self.qtd_aniversario = qtd_aniversario
        self.qtd_casamento = qtd_casamento
        self.qtd_salgadinho_mini = qtd_salgadinho_mini
        self.qtd_salgadinho_normal = qtd_salgadinho_normal
        self.info_complementares = info_complementares
        self.status = status
        
    def inserir_dados(self):
        dados = load_workbook("dados.xlsx")
        planilha_ativa = dados.active

        try:
            index = max(Xlsx_to_list("A").toListNum()) + 1
        except:
            index = 1
            
        planilha_ativa[f"A{index+1}"] = index
        planilha_ativa[f"B{index+1}"] = self.nome_cliente
        planilha_ativa[f"C{index+1}"] = self.data_entrega
        planilha_ativa[f"D{index+1}"] = self.horario_entrega
        planilha_ativa[f"E{index+1}"] = self.qtd_aniversario
        planilha_ativa[f"F{index+1}"] = self.qtd_casamento
        planilha_ativa[f"G{index+1}"] = self.qtd_salgadinho_mini
        planilha_ativa[f"H{index+1}"] = self.qtd_salgadinho_normal
        planilha_ativa[f"J{index+1}"] = self.info_complementares
        planilha_ativa[f"K{index+1}"] = self.status
        
        dados.save("dados.xlsx")