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
        
        # Entidade Fabricante
        cur.execute("""
            CREATE TABLE IF NOT EXISTS fabricante(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidadeRobos INT,
                ativo INTEGER NOT NULL DEFAULT 0,
                tecnologia TEXT NOT NULL
                )
            """)
        
        
        cur.execute("SELECT COUNT(*) FROM missao")
        cur.execute("SELECT COUNT(*) FROM robos")
        cur.execute("SELECT COUNT(*) FROM fabricante")
        if cur.fetchone()[0] != 0:
            cur.execute("DELETE FROM missao")
            cur.execute("DELETE FROM robos")
            cur.execute("DELETE FROM fabricante")
            
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
        
        cur.execute(
            "INSERT INTO fabricante (nome, quantidadeRobos, ativo, tecnologia) VALUES (?, ?, ?, ?)",
            ("factory", 2, 0, "rapida")
            )
        cur.execute(
            "INSERT INTO fabricante (nome, quantidadeRobos, ativo, tecnologia) VALUES (?, ?, ?, ?)",
            ("mercedes", 4, 0, "tecnologia com ia")
            )
        cur.execute(
            "INSERT INTO fabricante (nome, quantidadeRobos, ativo, tecnologia) VALUES (?, ?, ?, ?)",
            ("toyota", 3, 0, "super tecnologia")
            )
        cur.execute(
            "INSERT INTO fabricante (nome, quantidadeRobos, ativo, tecnologia) VALUES (?, ?, ?, ?)",
            ("mercedes", 4, 0, "tecnologia com ia")
            )
        cur.execute(
            "INSERT INTO fabricante (nome, quantidadeRobos, ativo, tecnologia) VALUES (?, ?, ?, ?)",
            ("arco vita", 5, 0, "ultima geracao")
            )
        
    
    except Exception:
        conn.rollback()
    finally:
        conn.close()
    
if __name__ == "__main__":
    install()
