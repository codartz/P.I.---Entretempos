import mysql.connector
from mysql.connector import Error

class DataManager:

    @staticmethod
    def conectar():

        try:

            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="senha_banco",
                database="db_entretempos"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL!")

            return conexao

        except Error as erro:
            print(f"Erro ao conectar: {erro}")
            return None
