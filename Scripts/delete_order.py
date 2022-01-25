from Scripts.sqlite import SQLite

class DeleteOrder:
    def __init__(self, customer_list: list, index: int) -> None:
        self.customer_list = customer_list
        self.index = index

    def deletar_encomenda(self) -> None:
        id = self.customer_list[self.index]
        SQLite.delete('dados', f'id = {id}')