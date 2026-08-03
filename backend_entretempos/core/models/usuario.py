from datetime import datetime

class Usuario:

    def __init__(
        self,
        nome_usuario,
        email,
        senha,
        data_cadastro=None
    ):

        self.nome_usuario = nome_usuario
        self.email = email
        self.senha = senha

        self.data_cadastro = (
            data_cadastro or datetime.now()
        )

    def __str__(self):
        return f"{self.nome_usuario} - {self.email}"