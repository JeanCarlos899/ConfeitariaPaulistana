

class GetRealIndex:
    def __init__(self, lista_encomenda:list, index_encomenda:list):
        self.lista_encomenda = lista_encomenda
        self.index_encomenda = index_encomenda

    def return_index(self) -> int:
        encomenda = self.lista_encomenda[int(self.index_encomenda[0])]
        id_encomenda = encomenda[1]
        return int(int(id_encomenda) + 1)