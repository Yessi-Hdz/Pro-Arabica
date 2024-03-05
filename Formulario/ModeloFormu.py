import sqlite3

class FormuDB:
    @staticmethod
    def cargar_formulario_db():
        preencuesta = []

        conn = sqlite3.connect("BD/BasesDatos/formulario.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM preencuesta")
        rows = cursor.fetchall()

        conn.close()

        preguntas = [(row[0], row[1], [opcion for opcion in row[2:] if opcion]) for row in rows]  
        return preguntas
    #lista en local, como modo estatico, de la base con las preguntas


class UserDB:
    def __init__(self):
        self.conn = sqlite3.connect("BD/BasesDatos/preferencias_usu.db")
        self.cursor = self.conn.cursor()

    def guardar_respuesta_encuesta(self, usuario_id, respuestas):
        try:
            self.cursor.execute("""
                INSERT INTO respuestas_encuesta (usuario_id, respuesta_pregunta1, respuesta_pregunta2, respuesta_pregunta3,
                                                respuesta_pregunta4, respuesta_pregunta5, respuesta_pregunta6, respuesta_pregunta7,
                                                respuesta_pregunta8, respuesta_pregunta9, respuesta_pregunta10, respuesta_pregunta11)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (usuario_id,) + tuple(respuestas))
            self.conn.commit()
            print("Respuestas guardadas.")
        except sqlite3.Error as e:
            print("Error al guardar las respuestas:", e)

    def cerrar_conexion(self):
        self.conn.close()


    #maneja las preferencias del usuario, guarda lo que el usuario elige.