from data.data_manager import DataManager
from datetime import datetime
import time


class PomodoroService:

    @staticmethod
    def opcoes_pomodoro():

        while True:

            print("\n=== POMODORO ===")
            print("1. Iniciar Pomodoro")
            print("2. Voltar")

            opcao = input("Escolha: ")

            if opcao == "1":
                PomodoroService.iniciar_pomodoro()

            elif opcao == "2":
                break

            else:
                print("Opção inválida.")


    @staticmethod
    def iniciar_pomodoro():

        conexao = DataManager.conectar()
        cursor = conexao.cursor()

        duracao = int(
            input("Duração em minutos (25 recomendado): ")
        )

        dthr_inicio = datetime.now()

        segundos = duracao * 60

        while segundos > 0:

            minutos = segundos // 60
            segundos_restantes = segundos % 60

            print(
                f"\rTempo restante: {minutos:02d}:{segundos_restantes:02d}",
                end=""
            )

            time.sleep(1)
            segundos -= 1

        dthr_termino = datetime.now()

        print("\nPomodoro finalizado!")

        cursor.close()

        conexao.close()