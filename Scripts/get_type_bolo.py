from openpyxl import load_workbook

class GetTypeBolo:
    def __init__(self, index):
        self.index = index
    
    def return_type_bolo(self):
        planilha = load_workbook("dados.xlsx")
        aba_ativa = planilha.active
        lista = []
        for celula in aba_ativa["E"]:
            valores = celula.value
            lista.append(valores) if valores != "Tipo bolo" else None
        
        index_bolo = lista[int(self.index) - 1]

        return index_bolo
