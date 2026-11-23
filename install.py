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
        
        # Entidade Robô
        cur.execute("""
                CREATE TABLE IF NOT EXISTS robos (
                    id INTERGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    anoFabricacao INTEGER NOT NULL,
                    ligado BOOLEAN NOT NULL DEFAULT FALSE,
                    modelo TEXT NOT NULL DEFAULT '',

                )
            """)
        
        
        cur.execute("SELECT COUNT(*) FROM missao")
        cur.execute("SELECT COUNT(*) FROM robos")
        if cur.fetchone()[0] != 0:
            cur.execute("DELETE FROM missao")
            cur.execute("DELETE FROM robos")
            
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
        
        cur.executemany("""
            INSERT INTO robos (nome, anoFabricacao, ligado, modelo)
            VALUES (?, ?, ?, ?)
        """, [
            ("Rodolfo", 2002, False, "Sony3000"),
            ("Neon", 2026, True, "TechEvolution2.0"),
            ("Doroteia", 1999, False, "LG4000"),
            ("Siri", 2015, True, "AppleTech360"),
            ("Lenovan", 1985, False, "QuadraTecnon"),
        ])
        
        
        
    except Exception:
        conn.rollback()
    finally:
        conn.close()
    
if __name__ == "__main__":
    install()
