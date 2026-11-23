class Fabricante:
    def __init__(self, id = None, nome: str = "", quantidadeRobos: int= 0, ativo= False, tecnologia: str= ""):
        self.id = id
        self.nome = nome
        self.quantidadeRobos = quantidadeRobos
        self.ativo = ativo
        self.tecnologia = tecnologia
    