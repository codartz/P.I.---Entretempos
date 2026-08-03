class Grupo:

    def __init__(
        self,
        titulo,
        id_grupo=None
    ):

        self.id_grupo = id_grupo
        self.titulo = titulo

    def __str__(self):
        return self.titulo