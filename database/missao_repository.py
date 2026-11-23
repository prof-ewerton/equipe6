from database.connection import get_db_connection
from entities.missao import Missao

class MissaoRepository:
    def __init__(self):
        self.conn = get_db_connection()
        
    def criar(self, missao: Missao):
        try:
            cur = self.conn.cursor()
            
            cur.execute(f"""
                INSERT INTO missao VALUES
                (NULL, '{missao.nome}', {missao.duracao}, {missao.concluida}, '{missao.categoria}')
            """)
            
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise Exception("ERRO AO CRIAR NO BANCO")
