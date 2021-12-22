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
    tipo_bolo = retornar_lista("E")

    id.pop(0)
    valor.pop(0)
    data_entrega.pop(0)
    nome_cliente.pop(0)
    tipo_bolo.pop(0)

    x = PrettyTable()
    x.field_names = ["ID", "Valor R$", "Data de entrega", "Cliente", "Tipo do bolo"]

    for valor in range(len(id)):
        x.add_row([id[valor], valor[valor], data_entrega[valor], nome_cliente[valor], tipo_bolo[valor]]) if id[valor] != None else ''
    return x



