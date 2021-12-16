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
        ws["B1"] = "Valor aproximado"
        ws["C1"] = "Data de entrega"
        ws["D1"] = "Nome do cliente"
        ws["E1"] = "Tipo bolo"
        wb.save("dados.xlsx")
        continue

class InsertDados:
    def __init__(self, valor_bolo, data_entrega, nome_cliente, tipo_bolo):
        self.valor_bolo = valor_bolo
        self.data_entrega = data_entrega
        self.nome_cliente = nome_cliente
        self.tipo_bolo = tipo_bolo
    def inserir_dados(self):
        dados = load_workbook("dados.xlsx")
        planilha_ativa = dados.active

        try:
            index = max(Xlsx_to_list("A").toList()) + 1
        except:
            index = 1
            
        planilha_ativa[f"A{index+1}"] = index
        planilha_ativa[f"B{index+1}"] = self.valor_bolo
        planilha_ativa[f"C{index+1}"] = self.data_entrega
        planilha_ativa[f"D{index+1}"] = self.nome_cliente
        if self.tipo_bolo == 1:
            planilha_ativa[f"E{index+1}"] = "Aniversário"
        else: 
            planilha_ativa[f"E{index+1}"] = "Casamento"
        
        dados.save("dados.xlsx")