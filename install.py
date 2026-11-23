from database.connection import get_connection

    def install:
        connection = get_connection()
        
    try:
        
        connection.execute = ("BEGIN IMMEDIATE")
        connection.execute = ("""
            CREATE TABLE IF NOT EXISTS robos (
                id INTERGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                anoFabricacao INTEGER NOT NULL,
                ligado BOOLEAN NOT NULL DEFAULT FALSE,
                modelo TEXT NOT NULL DEFAULT '',

            )
        """)
        
         versao = connection.execute("PRAGMA user_version").fetchone()[0]
         
         if versao == 0:
            connection.executemany(
                """
                INSERT INTO robos (nome, anoFabricacao, ligado, modelo)
                VALUES (?, ?, ?, ?)
                """,
                [("Rodolfo", 2002, False, "Sony3000"),
                 ("Neon", 2026, True, "TechEvolution2.0"),
                 ("Doroteia", 1999, False, "LG4000"),
                 ("Siri", 2015, True, "AppleTech360"),
                 ("Lenovan", 1985, False, "QuadraTecnon"),
                                  ], )
            
            versao = connection.execute("PRAGMA user_version = 1")
            
        connection.commit()
        
    finally:
        connection.close()
        
        
        
        
