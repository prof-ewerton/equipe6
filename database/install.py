from database.connection import get_db_connection()

def install():
    connection = get_connection()

    try:
        
        connection.execute("""
            CREATE TABLE IF NOT EXISTS fabricante(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidadeRobos INT,
                ativo INTEGER NOT NULL DEFAULT 0,
                tecnologia TEXT NOT NULL
                )
            """)

        
        cursor = connection.execute("SELECT COUNT(*) FROM fabricante")
        total = cursor.fetchone()[0]
        
        if total == 0:
            connection.execute(
                "INSERT INTO fabricante (nome, quantidadeRobos, ativo, tecnologia) VALUES (?, ?, ?, ?)",
                ("factory", 2, 0, "rapida")
                )
            connection.execute(
                "INSERT INTO fabricante (nome, quantidadeRobos, ativo, tecnologia) VALUES (?, ?, ?, ?)",
                ("mercedes", 4, 0, "tecnologia com ia")
                )
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")