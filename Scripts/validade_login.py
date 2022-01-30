from Scripts.sqlite import SQLite

class validadeLogin:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __call__(self):
        user = SQLite('dados.db').select(
            'usuarios', '*', f"username='{self.user}' AND password='{self.password}'"
            )

        if user:
            return True