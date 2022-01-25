from Scripts.sqlite import SQLite

class ReturnList:
    def __init__(self, col_name: str, condition=None) -> None:
        self.col_name = col_name
        self.condition = condition

    def __call__(self) -> list:
        colList = []

        idList = SQLite("dados.db").select(
            'dados',
            col_str=self.col_name,
            condition=self.condition
        )

        for value in idList:
            if value != None:
                colList.append(value[0]) 

        return colList