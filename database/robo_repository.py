from database.connection import get_db_connection
from entities.robo import Robo

class RoboRepository:
    def __init__(self):
        self.conn = get_db_connection()
        
    def criar(self, robo: Robo):
        try:
            cur = self.conn.cursor()
            
            cur.execute(f"""
                INSERT INTO robo VALUES
                (NULL, '{robo.nome}', {robo.anoFabricacao}, {robo.ligado}, '{robo.modelo}')
            """)
            
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise Exception("ERRO AO CRIAR NO BANCO")