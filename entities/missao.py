class Missao:
    def __init__(
        self,
        missao_id: int | None = None,
        nome: str = "",
        duracao: int = 0,
        concluida: bool = False,
        categoria: str = ""
    ) -> None:
        self.id = missao_id
        self.nome = nome
        self.duracao = duracao
        self.concluida = concluida
        self.categoria = categoria
