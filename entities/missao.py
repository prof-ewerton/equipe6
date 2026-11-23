class Missao:
    def __init__(
        self,
        nome: str = "",
        duracao: int = 0,
        concluida: bool = False,
        categoria: str = "",
        missao_id: int | None = None
    ) -> None:
        self.id = missao_id
        self.nome = nome
        self.duracao = duracao
        self.concluida = concluida
        self.categoria = categoria
