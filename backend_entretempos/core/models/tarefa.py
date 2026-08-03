from datetime import datetime

class Tarefa:

    def __init__(
        self,
        titulo,
        descricao,
        dthr_prazo,
        frequencia,
        despertar,
        status,
        fk_grupo,
        id_tarefa=None,
        dthr_insercao=None
    ):

        self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.descricao = descricao

        self.dthr_insercao = (
            dthr_insercao or datetime.now()
        )

        self.dthr_prazo = dthr_prazo
        self.frequencia = frequencia
        self.despertar = despertar
        self.status = status
        self.fk_grupo = fk_grupo

    def __str__(self):

        return f"{self.titulo} - {self.status}"