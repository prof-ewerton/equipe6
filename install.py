from database.connection import get_db_connection

def install():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Entidade Missão
        cur.execute("""
            CREATE TABLE IF NOT EXISTS missao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR NOT NULL DEFAULT '',
                duracao INTEGER NOT NULL DEFAULT 0,
                concluida BOOLEAN DEFAULT FALSE,
                categoria VARCHAR NOT NULL DEFAULT ''
            )
        """)
        
        cur.execute("SELECT COUNT(*) FROM missao")
        if cur.fetchone()[0] != 0:
            cur.execute("DELETE FROM missao")
            
        cur.executemany("""
            INSERT INTO missao
            VALUES (?, ?, ?, ?)
        """, [
            ('missao 1', 5, False, 'combate'),
            ('missao 2', 7, True , 'combate'),
            ('missao 3', 3, False, 'exploracao'),
            ('missao 4', 5, False, 'resgate'),
            ('missao 5', 10, True , 'combate'),
        ])
        
    except Exception:
        conn.rollback()
    finally:
        conn.close()
    
if __name__ == "__main__":
    install()