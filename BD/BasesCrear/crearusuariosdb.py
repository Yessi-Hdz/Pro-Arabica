import sqlite3
#crea la tabla
def crear_tabla_usuarios(self):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            usuario_id INTEGER PRIMARY KEY,
                            usuario TEXT NOT NULL UNIQUE,
                            contrasena TEXT NOT NULL,
                            nombre TEXT,
                            apellido TEXT,
                            cp TEXT,
                            email TEXT)''')
        conn.commit()
        conn.close()
        
def insertar_datos_prueba(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Datos de ejemplo de usuarios
    datos_usuarios = [
        ("Aitor", "A1234", "Aitor", "Martinez", "20045", "aitor@mail.com"),
        ("AneG", "G2345", "Ane", "Gonzalez", "20021", "ane@email.com"),
        ("Iker", "I3456", "Iker", "Lopez", "20890", "iker@email.com"),
        ("Maika", "M1234","Mai", "kara", "20003", "maika@email.com" )
        ]
    
    # Insertar usuarios en tabla
    cursor.executemany('''INSERT INTO usuarios (usuario, contrasena, nombre, apellido, cp, email)
                        VALUES (?, ?, ?, ?, ?, ?)''', datos_usuarios)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_file = "usuarios.db"
    crear_tabla_usuarios(db_file)
    #insertar_datos_prueba(db_file) #es el nombre del archivo db Usuarios