from datetime import datetime

class UsuarioRelTarefas:

    def __init__(
        self,
        fk_rel_usuario,
        fk_rel_tarefas,
        id_rel_user_tarefas=None
    ):

        self.id_rel_user_tarefas = (
            id_rel_user_tarefas
        )

        self.fk_rel_usuario = fk_rel_usuario
        self.fk_rel_tarefas = fk_rel_tarefas

    def __str__(self):
        return (
            f"Usuário: {self.fk_rel_usuario} "
            f"- Tarefa: {self.fk_rel_tarefas}"
        )