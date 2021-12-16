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
        ws["B1"] = "Valor"
        ws["C1"] = "Data de entrega"
        ws["D1"] = "Nome do cliente"
        wb.save("dados.xlsx")
        continue

class InsertDados:
    def __init__(self, valor_bolo, data_entrega, nome_cliente):
        self.valor_bolo = valor_bolo
        self.data_entrega = data_entrega
        self.nome_cliente = nome_cliente
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
        
        dados.save("dados.xlsx")