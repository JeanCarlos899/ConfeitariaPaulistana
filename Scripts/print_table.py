from prettytable import PrettyTable
from openpyxl import load_workbook

def print_table():
    def retornar_lista(coluna):
            planilha = load_workbook("dados.xlsx")
            aba_ativa = planilha.active
            lista = []
            for celula in aba_ativa[coluna]:
                valores = celula.value
                lista.append(valores)
            return list(lista)

    id = retornar_lista("A")
    valor = retornar_lista("B")
    data_entrega = retornar_lista("C")
    nome_cliente = retornar_lista("D")

    id.pop(0)
    valor.pop(0)
    data_entrega.pop(0)
    nome_cliente.pop(0)

    x = PrettyTable()
    x.field_names = ["ID", "Valor", "Data de entrega", "Nome do cliente"]

    for coisa in range(len(id)):
        x.add_row([id[coisa], valor[coisa], data_entrega[coisa], nome_cliente[coisa]])
    return x



