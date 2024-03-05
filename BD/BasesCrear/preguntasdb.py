import sqlite3

def crear_tabla_preguntas(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS preguntas (
                        pregunta_id INTEGER PRIMARY KEY,
                        pregunta TEXT NOT NULL,
                        opcion1 TEXT NOT NULL,
                        opcion2 TEXT NOT NULL,
                        opcion3 TEXT NOT NULL,
                        respuesta_correcta TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def insertar_pregunta(db_file, pregunta):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO preguntas (pregunta, opcion1, opcion2, opcion3, respuesta_correcta)
                    VALUES (?, ?, ?, ?, ?)''',
                    (pregunta["pregunta"], pregunta["opciones"][0], pregunta["opciones"][1],
                    pregunta["opciones"][2], pregunta["respuesta_correcta"]))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_file = "preguntas.db"
    crear_tabla_preguntas(db_file)

    preguntas = [
        {
                "pregunta": "¿Qué país es conocido por haber introducido el café en Europa?",
                "opciones": ["Etiopía", "Arabia", "Yemen"],
                "respuesta_correcta": "Arabia"
            },
            {
                "pregunta": "¿En qué siglo se cree que se descubrió el café?",
                "opciones": ["Siglo IX", "Siglo XV", "Siglo XVII"],
                "respuesta_correcta": "Siglo IX"
            },
            {
                "pregunta": "¿Qué ácido presente en el café contribuye a su sabor característico?",
                "opciones": ["Ácido clorogénico", "Ácido cítrico", "Ácido ascórbico"],
                "respuesta_correcta": "Ácido clorogénico"
            },
            {
                "pregunta": "¿En qué país se celebró la primera cafetería conocida?",
                "opciones": ["Egipto", "Italia", "Turquía"],
                "respuesta_correcta": "Turquía"
            },
            {
                "pregunta": "¿Qué tipo de café se caracteriza por ser producido a partir de granos excretados por un animal?",
                "opciones": ["Café robusta", "Café arábica", "Café civeta"],
                "respuesta_correcta": "Café civeta"
            },
            {
                "pregunta": "¿Dónde es originario el café?",
                "opciones": ["Etiopía", "Colombia", "Brasil"],
                "respuesta_correcta": "Etiopía"
            },
            {
                "pregunta": "¿Qué efecto tiene la cafeína en el cuerpo humano?",
                "opciones": ["Aumenta la frecuencia cardíaca", "Reduce el apetito", "Aumenta la producción de insulina"],
                "respuesta_correcta": "Aumenta la frecuencia cardíaca"
            },
            {
                "pregunta": "¿Qué país es el mayor productor de café arábica en el mundo?",
                "opciones": ["Brasil", "Colombia", "Etiopía"],
                "respuesta_correcta": "Colombia"
            },
            {
                "pregunta": "¿Cuál de los siguientes no es un sabor típico encontrado en una cata de café?",
                "opciones": ["Astringencia", "Umami", "Acidez"],
                "respuesta_correcta": "Umami"
            },
            {
                "pregunta": "¿Cuál es el principal productor de café robusta en el mundo?",
                "opciones": ["Vietnam", "Colombia", "Brasil"],
                "respuesta_correcta": "Vietnam"
            },
            {
                "pregunta": "¿Qué país tiene la mayor cantidad de cafés per capita en el mundo?",
                "opciones": ["Finlandia", "Estados Unidos", "Italia"],
                "respuesta_correcta": "Finlandia"
            }
    ]

    for pregunta in preguntas:
        insertar_pregunta(db_file, pregunta)

    print("Base de datos de preguntas creada y poblada exitosamente.")
