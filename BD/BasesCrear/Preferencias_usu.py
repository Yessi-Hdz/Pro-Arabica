import sqlite3

class PreferenciaManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def crear_tabla_respuestas_encuesta(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS respuestas_encuesta (
                                    id INTEGER PRIMARY KEY,
                                    usuario_id INTEGER,
                                    respuesta_pregunta1 TEXT,
                                    respuesta_pregunta2 TEXT,
                                    respuesta_pregunta3 TEXT,
                                    respuesta_pregunta4 TEXT,
                                    respuesta_pregunta5 TEXT,
                                    respuesta_pregunta6 TEXT,
                                    respuesta_pregunta7 TEXT,
                                    respuesta_pregunta8 TEXT,
                                    respuesta_pregunta9 TEXT,
                                    respuesta_pregunta10 TEXT,
                                    respuesta_pregunta11 TEXT,
                                    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                    FOREIGN KEY(usuario_id) REFERENCES usuarios(usuario_id),
                                    CONSTRAINT fk_usuario UNIQUE (usuario_id)
                                )''')
        self.conn.commit()


    def guardar_respuesta_encuesta(self, usuario_id, respuestas):
        try:
            self.cursor.execute("""
                INSERT INTO respuestas_encuesta (usuario_id, respuesta_pregunta1, respuesta_pregunta2, respuesta_pregunta3,
                                                respuesta_pregunta4, respuesta_pregunta5, respuesta_pregunta6, respuesta_pregunta7,
                                                respuesta_pregunta8, respuesta_pregunta9, respuesta_pregunta10, respuesta_pregunta11)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (usuario_id,) + tuple(respuestas))
            self.conn.commit()
            print("Respuestas guardadas exitosamente.")
        except sqlite3.Error as e:
            print("Error al guardar las respuestas:", e)

    def cerrar_conexion(self):
        self.conn.close()

# Ejemplo de uso:
if __name__ == "__main__":
    manager = PreferenciaManager("preferencias_usu.db")  # Nombre de la base de datos
    manager.crear_tabla_respuestas_encuesta()
    #manager.guardar_respuesta_encuesta()
    manager.cerrar_conexion()
