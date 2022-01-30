import sqlite3

class SQLite:
    def __init__(self, db_file='dados.db'):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        
        self.create_table(
            'dados', 
            '''
                id INTEGER PRIMARY KEY, 
                nome_cliente TEXT, 
                data_entrega TEXT, 
                hora_entrega TEXT, 
                bolo_aniversario INTERGER, 
                bolo_casamento INTERGER, 
                salgado_mini INTERGER, 
                salgado_normal INTERGER, 
                valor_final INTERGER, 
                mensagem TEXT,
                status TEXT
            '''
        )

        self.create_table(
            'usuarios',
            '''
                username TEXT PRIMARY KEY,
                password TEXT,
                tipo TEXT
            '''
        )

    def create_table(self, table_name, col_list):
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({col_list})"
        self.cursor.execute(sql)

    def insert(self, table_name, data_str):
        sql = 'INSERT INTO {} VALUES ({})'.format(table_name, data_str)
        self.cursor.execute(sql)
        self.conn.commit()

    def selected_insert(self, table_name, col_list, data_list):
        col_str = ', '.join(col_list)
        data_str = ', '.join(['?'] * len(col_list))
        sql = 'INSERT INTO {} ({}) VALUES ({})'.format(table_name, col_str, data_str)
        self.cursor.execute(sql, data_list)
        self.conn.commit()

    def select(self, table_name, col_str='*', condition=None):
        sql = 'SELECT {} FROM {}'.format(col_str, table_name)
        if condition:
            sql += ' WHERE {}'.format(condition)
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def selected_select(self, table_name, col_list, condition):
        col_str = ', '.join(col_list)
        sql = 'SELECT {} FROM {} WHERE {}'.format(col_str, table_name, condition)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self, table_name, col_str, data_str, condition):
        sql = f'UPDATE {table_name} SET {col_str} = {data_str} WHERE {condition}'
        self.cursor.execute(sql)
        self.conn.commit()

    def delete(self, table_name, condition):
        sql = 'DELETE FROM {} WHERE {}'.format(table_name, condition)
        self.cursor.execute(sql)
        self.conn.commit()

    def drop_table(self, table_name):
        sql = 'DROP TABLE {}'.format(table_name)
        self.cursor.execute(sql)
        self.conn.commit()

if __name__ == '__main__':

    # SQLite('dados.db').create_table(
    #     'dados', 
    #     '''
    #         id INTEGER PRIMARY KEY, 
    #         nome_cliente TEXT, 
    #         data_entrega TEXT, 
    #         hora_entrega TEXT, 
    #         bolo_aniversario INTERGER, 
    #         bolo_casamento INTERGER, 
    #         salgado_mini INTERGER, 
    #         salgado_normal INTERGER, 
    #         valor_final INTERGER, 
    #         status TEXT
    #     '''
    #     )

    # SQLite('dados.db').insert("dados", "Null, 'teste', '2020-01-01', '12:00', '0', '0', '0', '0', '0', 'Pendente'")

    # print(SQLite('dados.db').select('dados', '*', 'status = "Pendente"'))

    # SQLite('dados.db').update('dados', 'id', '"1"', 'id=3')

    # SQLite('dados.db').delete('dados', 'id=1')

    # SQLite('test.db').drop_table('dados')

    # print(SQLite('dados.db').selected_select('dados', ['id', 'nome_cliente', 'data_entrega', 'hora_entrega', 'bolo_aniversario', 'bolo_casamento', 'salgado_mini', 'salgado_normal', 'valor_final', 'status'], 'id=1'))

    # SQLite('dados.db').update('dados', 'status', '"Concluído"', 'id=1')

    # print(SQLite('dados.db').selected_select('dados', ['salgado_mini'], f'id={1}')[0][0])

    # print(SQLite('dados.db').select(
    #                     'dados', '*', 'status = "Pendente"'
    #                 ))


    # print(SQLite('dados.db').select(
    #                 'dados', '*', 'status = "Pendente"'
    #             )[0])



    class ReturnList:
        def __init__(self, col_name: str) -> None:
            self.col_name = col_name

        def __call__(self) -> list:
            colList = []

            idList = SQLite("dados.db").select(
                'dados',
                col_str=self.col_name,
            )

            for value in idList:
                if value != None:
                    colList.append(value[0]) 

            return colList
        
    lista = ReturnList('id').__call__()