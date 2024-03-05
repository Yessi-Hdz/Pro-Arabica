import sqlite3

class TriviaDB:
    @staticmethod
    def cargar_preguntas_db():
        preguntas = [] #se carga en local 
        
        conn = sqlite3.connect("BD/BasesDatos/preguntas.db")
        cursor = conn.cursor()
        cursor.execute("SELECT pregunta, opcion1, opcion2, opcion3, respuesta_correcta FROM preguntas")
        rows = cursor.fetchall()
        conn.close()
        for row in rows:
            pregunta = {
                "pregunta": row[0],
                "opciones": [row[1], row[2], row[3]],
                "respuesta_correcta": row[4]
            }
            preguntas.append(pregunta)
        return preguntas #devuelve la lista

#se utiliza un método estático para no instanciarlo en donde se llame triviaGame, sin self, genra las preguntas de la trivia