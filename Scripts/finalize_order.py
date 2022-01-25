from Scripts.sqlite import SQLite

class FinalizeOrder:
    def __init__(self, lista_encomendas, index_encomenda, kg_aniversario, kg_casamento):
        self.lista_encomendas = lista_encomendas
        self.index_encomenda = index_encomenda
        self.kg_aniversario = kg_aniversario
        self.kg_casamento = kg_casamento

    def get_preco_final(self):
        index = self.index_encomenda[0]
        id = self.lista_encomendas[index][0]

        qtdMini = SQLite('dados.db').selected_select(
            'dados', ['salgado_mini'], f'id={id}'
            )[0][0]
        qtdNormal = SQLite('dados.db').selected_select(
            'dados', ['salgado_mini'], f'id={id}'
            )[0][0]

        preco_final = ((float(self.kg_aniversario) * 5) 
                        + (float(self.kg_casamento) * 10) 
                        + (float(qtdMini) * 0.35) 
                        + (float(qtdNormal) * 0.75))
                
        SQLite('dados.db').update(
            'dados', 'status', '"Concluído"', f'id={id}'
            )
        SQLite('dados.db').update(
            'dados', 'valor_final', f'"{preco_final}"', f'id={id}'
            )
        
        return preco_final