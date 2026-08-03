from datetime import datetime

class Pomodoro:

    def __init__(
        self,
        dthr_inicio,
        dthr_termino,
        duracao,
        valor,
        id_pomodoro=None,
        dthr_cadastro=None
    ):

        self.id_pomodoro = id_pomodoro
        self.dthr_inicio = dthr_inicio
        self.dthr_termino = dthr_termino
        self.duracao = duracao
        self.valor = valor

        self.dthr_cadastro = (
            dthr_cadastro or datetime.now()
        )

    def __str__(self):
        return (
            f"Pomodoro {self.duracao} min "
            f"- Valor: {self.valor}"
        )