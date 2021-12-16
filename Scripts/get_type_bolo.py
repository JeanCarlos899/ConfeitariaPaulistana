from openpyxl import load_workbook

def retornar_lista(coluna):
        planilha = load_workbook("dados.xlsx")
        aba_ativa = planilha.active
        lista = []
        for celula in aba_ativa[coluna]:
            valores = celula.value
            lista.append(valores)
        return list(lista)

lista_bolo = retornar_lista("E")
lista_bolo.pop(0)

def get_type_bolo(index):
    index = index - 1
    return str(lista_bolo[index])
    