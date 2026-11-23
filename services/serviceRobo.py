from entities.robo import Robo
from database.robo_repository import RoboRepository

class ServiceRobo:
    def __init__(self, repo: RoboRepository):
        self.repo = repo
    
    
    def create(self, nome: str, anoFabricaco: int, ligado: bool = False, modelo: str = "") -> int:
        nome, anoFabricacao = self._validar_robo(nome, anoFabricacao)
        
        if modelo not in ["OpenIA", "Sonny2000", "LG360"]:
            return "Categoria inválida"
        
        robo = Robo(
            nome=nome,
            anoFabricacao=anoFabricacao,
            ligado=ligado,
            modelo=modelo,
            )
        
        
        return self.create(robo)
    
    def _validar_robo(self, nome: str, anoFabricacao: int):
        nome = nome.strip()
        
        if not nome:
            return ValueError("O nome do robô é obrigatório.")
        if type(anoFabricacao) is not int:
            return ValueError("O ano de fabricação do robô deve ser um número inteiro.")
        
        return nome, anoFabricacao