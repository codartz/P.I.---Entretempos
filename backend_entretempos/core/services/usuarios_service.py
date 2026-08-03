from data.data_manager import DataManager

from datetime import datetime
from getpass import getpass

import bcrypt


class UsuarioService:

    @staticmethod
    def listar_usuarios():

        try:
            conexao = DataManager.conectar()
            cursor = conexao.cursor()

            sql = "SELECT id_usuario, nome_usuario, email, data_cadastro FROM usuarios"

            cursor.execute(sql)

            usuarios = cursor.fetchall()

            if not usuarios:
                print("Nenhum usuário cadastrado.")

            else:
                for usuario in usuarios:
                    print(usuario)

        except Exception as erro:
            print(f"Erro: {erro}")

        finally:
            cursor.close()
            conexao.close()


    @staticmethod
    def cadastrar_usuario():
        
        try:

            conexao = DataManager.conectar()
            cursor = conexao.cursor()

            nome_usuario = input("Digite seu nome: ")
            email_usuario = input("Digite seu email: ")

            senha_usuario = getpass("Digite sua senha: ")

            data_nascimento = input("Data de nascimento (yyyy-MM-dd): ")

            try:
                data_convertida = datetime.strptime(data_nascimento,"%Y-%m-%d")
                data_mysql = data_convertida.strftime("%Y-%m-%d")

            except ValueError:
                print("Data inválida.")
                return

            cursor.execute(
                """
                SELECT id_usuario
                FROM usuarios
                WHERE email = %s
                """,
                (email_usuario,)
            )

            if cursor.fetchone():
                print("Email já cadastrado.")
                return

            senha_hash = bcrypt.hashpw(senha_usuario.encode("utf-8"), bcrypt.gensalt())

            sql = """
            INSERT INTO usuarios
            (
                nome_usuario,
                email,
                senha,
                data_nascimento
            )
            VALUES
            (%s, %s, %s, %s)
            """

            valores = (
                nome_usuario,
                email_usuario,
                senha_hash.decode("utf-8"),
                data_mysql
            )

            cursor.execute(sql, valores)
            conexao.commit()

            print("Usuário cadastrado com sucesso!")

        except Exception as erro:
            print(f"Erro ao cadastrar usuário: {erro}")

        finally:
            cursor.close()
            conexao.close()


    @staticmethod
    def autenticar_usuario():

        try:
            conexao = DataManager.conectar()
            cursor = conexao.cursor()

            email = input("Email: ")
            senha = getpass("Senha: ")

            sql = """
            SELECT
                id_usuario,
                senha
            FROM usuarios
            WHERE email = %s
            """

            cursor.execute(sql, (email,))
            usuario = cursor.fetchone()

            if not usuario:
                print("Usuário não encontrado.")
                return None

            id_usuario = usuario[0]
            senha_hash = usuario[1]

            if bcrypt.checkpw(
                senha.encode("utf-8"),
                senha_hash.encode("utf-8")
            ):

                print("Login realizado com sucesso!")
                return id_usuario

            print("Senha inválida.")
            return None

        except Exception as erro:
            print(f"Erro no login: {erro}")
            return None

        finally:
            cursor.close()
            conexao.close()


    @staticmethod
    def atualizar_usuario(id_usuario):

        try:
            conexao = DataManager.conectar()
            cursor = conexao.cursor()

            nome_usuario = input("Novo nome: ")

            email_usuario = input("Novo email: ")

            sql = """
            UPDATE usuarios
            SET
                nome_usuario = %s,
                email = %s
            WHERE id_usuario = %s
            """

            valores = (
                nome_usuario,
                email_usuario,
                id_usuario
            )

            cursor.execute(sql, valores)

            conexao.commit()

            print("Usuário atualizado com sucesso!")

        except Exception as erro:
            print(f"Erro ao atualizar usuário: {erro}")

        finally:
            cursor.close()
            conexao.close()


    @staticmethod
    def deletar_usuario(id_usuario):

        try:
            conexao = DataManager.conectar()
            cursor = conexao.cursor()

            confirmacao = input("Deseja realmente excluir sua conta? (s/n): ")

            if confirmacao.lower() != "s":
                return

            cursor.execute(
                """
                DELETE FROM usuarios
                WHERE id_usuario = %s
                """,
                (id_usuario,)
            )

            conexao.commit()

            print("Conta removida com sucesso!")

        except Exception as erro:
            print(f"Erro ao deletar usuário: {erro}")

        finally:
            cursor.close()
            conexao.close()