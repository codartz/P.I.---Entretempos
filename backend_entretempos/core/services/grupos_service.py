from data.data_manager import DataManager


class GrupoService:

    @staticmethod
    def listar_grupos():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM grupos"

        cursor.execute(sql)
        grupos = cursor.fetchall()

        if not grupos:
            print("Nenhum grupo cadastrado.")
        else:
            for grupo in grupos:
                print(grupo)

        cursor.close()
        conexao.close()


    @staticmethod
    def criar_grupo():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        nome_grupo = input(
            "Insira o nome do grupo: "
        )

        sql = """
        INSERT INTO grupos (titulo)
        VALUES (%s)
        """

        cursor.execute(
            sql,
            (nome_grupo,)
        )

        conexao.commit()

        print("Grupo criado com sucesso!")

        cursor.close()
        conexao.close()


    @staticmethod
    def buscar_grupo_por_id():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        id_grupo = int(
            input(
                "Insira o ID do grupo: "
            )
        )

        sql = """
        SELECT *
        FROM grupos
        WHERE id_grupo = %s
        """

        cursor.execute(
            sql,
            (id_grupo,)
        )

        grupo = cursor.fetchone()

        if grupo:
            print(grupo)
        else:
            print(
                "Grupo não encontrado."
            )

        cursor.close()
        conexao.close()


    @staticmethod
    def atualizar_grupo():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        id_grupo = int(
            input(
                "Insira o ID do grupo: "
            )
        )

        nome_grupo = input(
            "Novo nome do grupo: "
        )

        sql = """
        UPDATE grupos
        SET titulo = %s
        WHERE id_grupo = %s
        """

        cursor.execute(
            sql,
            (
                nome_grupo,
                id_grupo
            )
        )

        conexao.commit()

        print(
            "Grupo atualizado com sucesso!"
        )

        cursor.close()
        conexao.close()


    @staticmethod
    def deletar_grupo():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        id_grupo = int(
            input(
                "Insira o ID do grupo: "
            )
        )

        sql = """
        DELETE FROM grupos
        WHERE id_grupo = %s
        """

        cursor.execute(
            sql,
            (id_grupo,)
        )

        conexao.commit()

        print(
            "Grupo deletado com sucesso!"
        )

        cursor.close()
        conexao.close()


    @staticmethod
    def opcoes_grupos():

        while True:

            print("\n=== GRUPOS ===")
            print("1. Listar grupos")
            print("2. Cadastrar grupo")
            print("3. Buscar grupo por ID")
            print("4. Atualizar grupo")
            print("5. Deletar grupo")
            print("6. Voltar")

            opcao = input(
                "Escolha: "
            )

            if opcao == "1":
                GrupoService.listar_grupos()

            elif opcao == "2":
                GrupoService.criar_grupo()

            elif opcao == "3":
                GrupoService.buscar_grupo_por_id()

            elif opcao == "4":
                GrupoService.atualizar_grupo()

            elif opcao == "5":
                GrupoService.deletar_grupo()

            elif opcao == "6":
                break

            else:
                print("Opção inválida.")