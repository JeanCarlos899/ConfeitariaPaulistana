import PySimpleGUI as sg 
from prettytable import PrettyTable
from Scripts.xlsx_to_list import Xlsx_to_list
 
class PrintTable:
    def imprimir_tabela(tipo):
        id = Xlsx_to_list("A").toListStr()
        nome_cliente = Xlsx_to_list("B").toListStr()
        data_entrega = Xlsx_to_list("C").toListStr()
        bolo_aniversario = Xlsx_to_list("D").toListStr()
        bolo_casamento = Xlsx_to_list("E").toListStr()
        salgado_mini = Xlsx_to_list("F").toListStr()
        salgado_normal = Xlsx_to_list("G").toListStr()
        valor_final = Xlsx_to_list("H").toListStr()
        status = Xlsx_to_list("I").toListStr()

        id.pop(0), nome_cliente.pop(0), data_entrega.pop(0)
        bolo_aniversario.pop(0), bolo_casamento.pop(0), valor_final.pop(0)
        salgado_mini.pop(0), salgado_normal.pop(0), status.pop(0)

        x = PrettyTable()

        x.field_names = [
            "ID", 
            "Nome Cliente", 
            "Data Entrega",
            "Bolo Aniversário",
            "Bolo Casamento",
            "Salgado Mini",
            "Salgado Normal",
            "Valor final"
            ]

        for valor in range(len(id)):
            if id[valor] != None and status[valor] == tipo:
                x.add_row(
                    [
                        id[valor],
                        nome_cliente[valor],
                        data_entrega[valor],
                        bolo_aniversario[valor],
                        bolo_casamento[valor],
                        salgado_mini[valor],
                        salgado_normal[valor],
                        valor_final[valor]
                    ]
                )
        return x

class ListarEncomendas:
    def menu_encomendas():
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Selecione a listagem", font=("Helvetica", 15))],
            [sg.Button("Encomendas em aberto", size=(100,2))],
            [sg.Button("Encomendas fechadas", size=(100,2))],
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True)

    def listar_encomendas(tipo):
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text("Lista de encomendas", font=("Helvetica", 15))],
            [sg.Text(PrintTable.imprimir_tabela(tipo), font=("Courier New", 10))], #Fonte monoespaçada para ficar alinhado
            [sg.Button("Voltar", size=(100,2))],
        ]
        return sg.Window("Listar encomendas", layout=layout, finalize=True)
