from database.missao_repository import MissaoRepository
from entities.missao import Missao

class MissaoService:
    def __init__(self, repo: MissaoRepository):
        self.repo = repo
        
    def criar(self, nome, duracao, concluida, categoria) -> str:
        if nome.strip() == "" or nome is None:
            return "Nome obrigatório"
        
        if categoria not in ["combate", "exploracao", "resgate"]:
            return "Categoria inválida"
        
        missao = Missao(nome, duracao, concluida, categoria)
        
        try:
            self.repo.criar(missao)
            return "Cadastro realizado com sucesso"
        except Exception:
            return "Erro na operação de cadastro"