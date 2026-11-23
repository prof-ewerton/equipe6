class Robo:
    def __init__(
        self,
        nome: str,
        anoFabricacao: int,
        robo_id= int | None = None,
        ligado: bool = False,
        modelo: str = ""):
        self.nome=nome,
        self.anoFabricacao=anoFabricacao
        self.ligado=ligado
        self.modelo=modelo