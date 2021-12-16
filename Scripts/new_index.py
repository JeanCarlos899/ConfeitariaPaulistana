from Scripts.xlsx_to_list import Xlsx_to_list
from openpyxl import load_workbook


def get_new_index():
    indices = Xlsx_to_list("A").toList()
    qtd_indices = len(indices)
    lista_indices = list(range(1, qtd_indices+1))

    dados = load_workbook("dados.xlsx")
    aba_ativa = dados.active

    for indice in lista_indices:
        aba_ativa[f"A{indice+1}"] = indice
    dados.save("dados.xlsx")
