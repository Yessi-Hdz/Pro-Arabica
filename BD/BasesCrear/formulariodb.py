import sqlite3

DB_FILE = "formulario.db"
PREGUNTAS_TABLE = "preencuesta"
COLUMN_NAMES = ["pregunta", "opcion1", "opcion2", "opcion3", "opcion4", "opcion5", "opcion6", "opcion7", "opcion8"]

def crear_tabla_preguntas(db_file):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {PREGUNTAS_TABLE} (
                            pregunta_id INTEGER PRIMARY KEY,
                            pregunta TEXT NOT NULL,
                            opcion1 TEXT NOT NULL,
                            opcion2 TEXT NOT NULL,
                            opcion3 TEXT NOT NULL,
                            opcion4 TEXT,
                            opcion5 TEXT,
                            opcion6 TEXT,
                            opcion7 TEXT,
                            opcion8 TEXT
                            )''')
        
# Ajuste para tener todas las opciones, que se rellene en las opciones que corresponden a las preguntas por eso apàrtir de la tercera es null
def insertar_pregunta(db_file, pregunta):
    opciones = pregunta["opciones"] + [''] * (len(COLUMN_NAMES) - 1 - len(pregunta["opciones"]))  
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(f'''INSERT INTO {PREGUNTAS_TABLE} ({", ".join(COLUMN_NAMES)})
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', [pregunta["pregunta"]] + opciones)

if __name__ == "__main__":
    crear_tabla_preguntas(DB_FILE)

    lista = [
        {
            "pregunta": "Preferencia respecto al tipo de grano de café:",
            "opciones": ["Arábica", "Robusta", "No le da importancia/lo desconoce"],
        },
        {
            "pregunta": "El tipo de café que más consumes es:",
            "opciones": ["Café solo/moka", "Espresso", "Café con leche", "Descafeinado", "Cappuccino", "Americano"],
        },
        {
            "pregunta": "Cuando compras café para consumir en casa, generalmente, lo compras:",
            "opciones": ["En grano", "Molido", "En cápsulas", "Café soluble", "Café frío listo para tomar"],
        },
        {
            "pregunta": "Sueles comprar el café para preparar en casa en:",
            "opciones": ["Supermercado", "Cafetería", "Tiendas especializadas", "Internet", "Otros"],
        },
        {
            "pregunta": "Frecuencia de consumo:",
            "opciones": ["Diario", "Varias veces por semana", "Una vez por semana", "Ocasionalmente", "Otro"],
        },
        {
            "pregunta": "Azúcar: Preferencia de agregar azúcar al café:",
            "opciones": ["Sí", "No", "A veces"],
        },
        {
            "pregunta": "Temperatura: Temperatura preferida del café:",
            "opciones": ["Caliente", "Tibio", "Frío"],
        },
        {
            "pregunta": "Leche o sin: Preferencia de añadir leche al café o consumirlo sin:",
            "opciones": ["Con leche", "Sin leche", "Otros"],
        },
        {
            "pregunta": "Acidez: Preferencia de acidez del café:",
            "opciones": ["Amargo", "No amargo", "Neutro"],
        },
        {
            "pregunta": "Perfil de Aroma: ¿Qué más te atrae?",
            "opciones": ["Achocolatado", "Afrutado", "Especiado", "Exótico", "Floral", "Láctico", "Vinoso"],
        },
        {
            "pregunta": "¿Qué tipo de sabor te gusta?",
            "opciones": ["Anuezados", "Cacao", "Canela", "Caramelos", "Especiados", "Florales", "Tequila", "Vino Rosado"],
        }
    ]

    for pregunta in lista:
        insertar_pregunta(DB_FILE, pregunta)

    print("Base de datos de preguntas creada y rellenada exitosamente.")
    
#Para crear base datos, cargar el formulario con sus preguntas y opciones