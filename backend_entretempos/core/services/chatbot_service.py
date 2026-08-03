import json
from ollama import chat

from core.services.tarefas_service import TarefaService


class ChatBotService:

    @staticmethod
    def interpretar_mensagem(mensagem, id_usuario):

        try:

            resposta = chat(
                model="phi3",
                messages=[
                    {
                        "role": "system",
                        "content": """
                        Você é um assistente que converte mensagens em tarefas.

                        Sua resposta deve ser SOMENTE um JSON válido.

                        Formato obrigatório:

                        {
                            "titulo": "texto",
                            "descricao": "texto",
                            "prazo": "YYYY-MM-DD HH:MM:SS"
                        }

                        Exemplo:

                        Usuário:
                        Ir para faculdade dia 09/03/2025 às 18h

                        Resposta:
                        {
                            "titulo": "Ir para faculdade",
                            "descricao": "Comparecer à faculdade",
                            "prazo": "2025-03-09 18:00:00"
                        }

                        Não utilize markdown.
                        Não utilize ```json.
                        Não escreva explicações.
                        Não escreva texto fora do JSON.
                        """
                    },
                    {
                        "role": "user",
                        "content": mensagem
                    }
                ],
                options={
                    "temperature": 0
                }
            )

            conteudo = resposta["message"]["content"]

            print("\nResposta bruta da IA:")
            print(conteudo)

            # Procura o JSON na resposta
            inicio = conteudo.find("{")
            fim = conteudo.rfind("}") + 1

            if inicio == -1 or fim == 0:
                raise Exception(
                    "A IA não retornou um JSON válido."
                )

            json_limpo = conteudo[inicio:fim]

            dados = json.loads(json_limpo)

            titulo = dados.get("titulo")
            descricao = dados.get("descricao")
            prazo = dados.get("prazo")

            if not titulo:
                raise Exception(
                    "Título não encontrado."
                )

            if not descricao:
                descricao = titulo

            if not prazo:
                prazo = "2099-12-31 23:59:59"

            print("\n=== TAREFA INTERPRETADA ===")
            print(f"Título: {titulo}")
            print(f"Descrição: {descricao}")
            print(f"Prazo: {prazo}")

            confirmar = input(
                "\nDeseja salvar a tarefa? (s/n): "
            )

            if confirmar.lower() == "s":

                TarefaService.criar_tarefa_ia(
                    titulo=titulo,
                    descricao=descricao,
                    prazo=prazo,
                    id_usuario=id_usuario
                )

                print("\nTarefa criada com sucesso!")

            else:
                print("\nOperação cancelada.")

        except json.JSONDecodeError as erro:

            print(
                f"\nErro ao converter JSON: {erro}"
            )

        except Exception as erro:

            print(
                f"\nErro ao interpretar tarefa: {erro}"
            )