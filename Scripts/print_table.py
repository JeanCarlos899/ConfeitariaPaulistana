from prettytable import PrettyTable
from Scripts.xlsx_to_list import Xlsx_to_list

class PrintTable:
    def pendentes():
        id = Xlsx_to_list("A").toListStr()
        nome_cliente = Xlsx_to_list("B").toListStr()
        data_entrega = Xlsx_to_list("C").toListStr()
        bolo_aniversario = Xlsx_to_list("D").toListStr()
        bolo_casamento = Xlsx_to_list("E").toListStr()
        salgado_mini = Xlsx_to_list("F").toListStr()
        salgado_normal = Xlsx_to_list("G").toListStr()
        status = Xlsx_to_list("I").toListStr()

        id.pop(0), nome_cliente.pop(0), data_entrega.pop(0)
        bolo_aniversario.pop(0), bolo_casamento.pop(0)
        salgado_mini.pop(0), salgado_normal.pop(0), status.pop(0)

        x = PrettyTable()

        x.field_names = [
            "ID", 
            "Nome Cliente", 
            "Data Entrega",
            "Bolo Aniversário",
            "Bolo Casamento",
            "Salgado Mini",
            "Salgado Normal"
            ]

        for valor in range(len(id)):
            x.add_row(
                [
                    id[valor],
                    nome_cliente[valor],
                    data_entrega[valor],
                    bolo_aniversario[valor],
                    bolo_casamento[valor],
                    salgado_mini[valor],
                    salgado_normal[valor]
                ]
            ) if id[valor] != None and status[valor] == 'Pendente' else ''
        return x



