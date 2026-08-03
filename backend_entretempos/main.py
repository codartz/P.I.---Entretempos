from ui.utils import exibir_cabecalho

from core.services.usuarios_service import UsuarioService
from core.services.grupos_service import GrupoService
from core.services.tarefas_service import TarefaService
from core.services.pomodoros_service import PomodoroService
from core.services.chatbot_service import ChatBotService


def menu_inicial():

    while True:
        exibir_cabecalho()

        print("1. Entrar")
        print("2. Criar conta")
        print("3. Encerrar")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            id_usuario = UsuarioService.autenticar_usuario()

            if id_usuario:
                painel_principal(id_usuario)

        elif opcao == "2":
            UsuarioService.cadastrar_usuario()

        elif opcao == "3":
            print("Até logo!")
            break

        else:
            print("Opção inválida.")
            input("\nPressione ENTER...")

def painel_principal(id_usuario):

    while True:
        exibir_cabecalho()
        print("=== MENU PRINCIPAL ===\n")

        print("1. Grupos")
        print("2. Tarefas")
        print("3. Pomodoro")
        print("4. Chatbot IA")
        print("5. Meu Perfil")
        print("6. Logout")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            GrupoService.opcoes_grupos()

        elif opcao == "2":
            TarefaService.opcoes_tarefa(id_usuario)

        elif opcao == "3":
            PomodoroService.opcoes_pomodoro()

        elif opcao == "4":

            mensagem = input(
                "\nDescreva sua tarefa: "
            )

            ChatBotService.interpretar_mensagem(
                mensagem,
                id_usuario
            )

            input("\nPressione ENTER...")

        elif opcao == "5":
            menu_perfil(id_usuario)

        elif opcao == "6":
            break

        else:
            print("Opção inválida.")
            input("\nPressione ENTER...")


def menu_perfil(id_usuario):

    while True:
        exibir_cabecalho()

        print("=== MEU PERFIL ===\n")
        print("1. Atualizar dados")
        print("2. Deletar conta")
        print("3. Voltar")

        opcao = input("\nEscolha: ")
        if opcao == "1":
            UsuarioService.atualizar_usuario(id_usuario)

        elif opcao == "2":
            UsuarioService.deletar_usuario(id_usuario)
            break

        elif opcao == "3":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_inicial()

