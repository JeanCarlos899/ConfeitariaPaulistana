from Scripts.sqlite import SQLite

class Revenues:
    def __init__(self, data_inicial: str, data_final: str):
        self.data_inicial = data_inicial
        self.data_final = data_final

    def get_value(self) -> str:
        valores = SQLite('dados.db').selected_select(
            'dados', ['valor_final'], 
            f'''
            data_entrega >= "{self.data_inicial}" 
            and data_entrega <= "{self.data_final}" 
            and status = "Concluído"
            '''
        )
        valor_total = 0
        for valor in valores:
            valor_total += float(valor[0])

        return f"\nR$ {valor_total:.2f}"
