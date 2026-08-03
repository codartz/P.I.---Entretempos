from data.data_manager import DataManager

class TarefaService:

    @staticmethod
    def opcoes_tarefa(id_usuario):
        while True:
            print("\n=== TAREFAS ===")
            print("1. Listar minhas tarefas")
            print("2. Criar tarefa")
            print("3. Atualizar tarefa")
            print("4. Concluir tarefa")
            print("5. Cancelar tarefa")
            print("6. Deletar tarefa")
            print("7. Voltar")

            opcao = input("Escolha: ")

            if opcao == "1":
                TarefaService.listar_tarefas_por_usuario(id_usuario)

            elif opcao == "2":
                TarefaService.criar_tarefa(id_usuario)

            elif opcao == "3":
                TarefaService.atualizar_tarefa()

            elif opcao == "4":
                TarefaService.concluir_tarefa()

            elif opcao == "5":
                TarefaService.cancelar_tarefa()

            elif opcao == "6":
                TarefaService.deletar_tarefa()

            elif opcao == "7":
                break

            else:
                print("Opção inválida")


    @staticmethod
    def criar_tarefa_ia(titulo, descricao, prazo, id_usuario):

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        try:

            sql = """
            INSERT INTO tarefas
            (
                titulo,
                descricao,
                dthr_prazo,
                frequencia,
                despertar,
                status,
                fk_grupo
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s)
            """

            valores = (
                titulo,
                descricao,
                prazo,
                0,
                False,
                "PENDENTE",
                None
            )

            cursor.execute(sql, valores)

            conexao.commit()

            id_tarefa = cursor.lastrowid

            sql_relacao = """
            INSERT INTO usuario_rel_tarefas
            (
                fk_rel_usuario,
                fk_rel_tarefas
            )
            VALUES
            (%s,%s)
            """

            cursor.execute(
                sql_relacao,
                (id_usuario, id_tarefa)
            )

            conexao.commit()

        finally:

            cursor.close()
            conexao.close()


    @staticmethod
    def criar_tarefa(id_usuario):

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        titulo = input("Título: ")
        descricao = input("Descrição: ")
        dthr_prazo = input("Prazo (yyyy-MM-dd HH:mm:ss): ")
        frequencia = int(input("Frequência: "))

        despertar = (input("Despertar? (s/n): ").lower() == "s")
        status = "PENDENTE"

        fk_grupo = int(
            input("ID do grupo: ")
        )

        sql_tarefa = """
        INSERT INTO tarefas
        (
            titulo,
            descricao,
            dthr_prazo,
            frequencia,
            despertar,
            status,
            fk_grupo
        )
        VALUES
        (%s, %s, %s, %s, %s, %s, %s)
        """

        valores_tarefa = (
            titulo,
            descricao,
            dthr_prazo,
            frequencia,
            despertar,
            status,
            fk_grupo
        )

        cursor.execute(
            sql_tarefa,
            valores_tarefa
        )
        conexao.commit()

        id_tarefa = cursor.lastrowid

        sql_relacao = """
        INSERT INTO usuario_rel_tarefas
        (
            fk_rel_usuario,
            fk_rel_tarefas
        )
        VALUES
        (%s, %s)
        """

        valores_relacao = (id_usuario, id_tarefa)

        cursor.execute(sql_relacao, valores_relacao)
        conexao.commit()

        print("Tarefa criada com sucesso!")

        cursor.close()
        conexao.close()


    @staticmethod
    def listar_tarefas():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT *
        FROM tarefas
        """

        cursor.execute(sql)
        tarefas = cursor.fetchall()

        for tarefa in tarefas:
            print(tarefa)

        cursor.close()
        conexao.close()


    @staticmethod
    def atualizar_tarefa():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        id_tarefa = int(input("ID da tarefa: "))

        titulo = input("Novo título: ")
        descricao = input("Nova descrição: ")

        dthr_prazo = input(
            "Novo prazo: "
        )

        frequencia = int(
            input("Nova frequência: ")
        )

        despertar = (
            input("Despertar? (s/n): ").lower()
            == "s"
        )

        fk_grupo = int(
            input("Novo grupo: ")
        )

        sql = """
        UPDATE tarefas
        SET
            titulo = %s,
            descricao = %s,
            dthr_prazo = %s,
            frequencia = %s,
            despertar = %s,
            fk_grupo = %s
        WHERE id_tarefa = %s
        """

        valores = (
            titulo,
            descricao,
            dthr_prazo,
            frequencia,
            despertar,
            fk_grupo,
            id_tarefa
        )

        cursor.execute(sql, valores)
        conexao.commit()

        print("Tarefa atualizada!")

        cursor.close()
        conexao.close()


    @staticmethod
    def alterar_status_tarefa():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        id_tarefa = int(input("ID da tarefa: "))

        novo_status = input("Novo status: ").upper()

        sql = """
        UPDATE tarefas
        SET status = %s
        WHERE id_tarefa = %s
        """

        cursor.execute(sql, (novo_status, id_tarefa))
        conexao.commit()

        print("Status alterado!")

        cursor.close()
        conexao.close()


    @staticmethod
    def listar_tarefas_por_usuario(id_usuario):

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        sql = """
        SELECT t.*
        FROM tarefas t
        INNER JOIN usuario_rel_tarefas urt
            ON urt.fk_rel_tarefas = t.id_tarefa
        WHERE urt.fk_rel_usuario = %s
        """

        cursor.execute(sql, (id_usuario,))
        tarefas = cursor.fetchall()

        for tarefa in tarefas:
            print(tarefa)

        cursor.close()
        conexao.close()


    @staticmethod
    def concluir_tarefa():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        id_tarefa = int(input("ID da tarefa: "))

        sql = """
        UPDATE tarefas
        SET status = 'CONCLUIDA'
        WHERE id_tarefa = %s
        """

        cursor.execute(sql, (id_tarefa,))
        conexao.commit()

        print("Tarefa concluída!")

        cursor.close()
        conexao.close()


    @staticmethod
    def cancelar_tarefa():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        id_tarefa = int(input("ID da tarefa: "))

        sql = """
        UPDATE tarefas
        SET status = 'CANCELADA'
        WHERE id_tarefa = %s
        """

        cursor.execute(sql, (id_tarefa,))
        conexao.commit()

        print("Tarefa cancelada!")

        cursor.close()
        conexao.close()


    @staticmethod
    def deletar_tarefa():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        id_tarefa = int(input("ID da tarefa: "))

        sql_relacao = """
        DELETE FROM usuario_rel_tarefas
        WHERE fk_rel_tarefas = %s
        """

        cursor.execute(sql_relacao, (id_tarefa,))

        sql_tarefa = """
        DELETE FROM tarefas
        WHERE id_tarefa = %s
        """

        cursor.execute(sql_tarefa, (id_tarefa,))
        conexao.commit()

        print("Tarefa deletada!")

        cursor.close()
        conexao.close()