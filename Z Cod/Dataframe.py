from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
import pandas as pd
import sqlite3

def cargar_datos_desde_bd(query):
    try:
        with sqlite3.connect('BD/BasesDatos/preferencias_usu.db') as conn:
            return pd.read_sql(query, conn)
    except sqlite3.Error as e:
        print("Error al leer la base de datos:", e)
        return None

def calcular_similitud(respuestas_usuario, productos, pesos):
    similitud = {}
    for index, producto in productos.iterrows():
        total_similitud = 0
        for pregunta, peso in pesos.items():
            if pregunta in producto.index and pregunta in respuestas_usuario.columns:
                if producto[pregunta] == respuestas_usuario[pregunta].iloc[0]:
                    total_similitud += peso
        similitud[index] = total_similitud
    return similitud

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recomendaciones de Café")
        self.setGeometry(250, 250, 900, 300) 

        self.lista_recomendaciones = QListWidget(self)
        self.lista_recomendaciones.setGeometry(10, 10, 880, 280) 
        self.mostrar_recomendaciones()

    def mostrar_recomendaciones(self):
        # Consulta SQL para seleccionar todos db respesutas
        sql_query = "SELECT * FROM respuestas_encuesta"
        # Cargar datos de respuestas desde db
        df_respuestas = cargar_datos_desde_bd(sql_query)

        if df_respuestas is not None:
            respuestas_dict = df_respuestas.iloc[0].to_dict()
            respuestas_usuario = pd.DataFrame(respuestas_dict, index=[0])

            # Definir pesos para cada pregunta, pero algunas no tienen mucho sentido
            pesos = {
                'respuesta_pregunta1': 0.1,
                'respuesta_pregunta2': 0.1,
                'respuesta_pregunta3': 0.05,
                'respuesta_pregunta4': 0.05,
                'respuesta_pregunta5': 0.05,
                'respuesta_pregunta6': 0.1,
                'respuesta_pregunta7': 0.1,
                'respuesta_pregunta8': 0.05,
                'respuesta_pregunta9': 0.05,
                'respuesta_pregunta10': 0.3,
                'respuesta_pregunta11': 0.3
            }

            # DF 'productos', sacados de la web
            productos = pd.read_csv("Relaciones/cafe.csv", sep=";")
            # Calcular similitud entre respuestas del usuario y productos
            similitud = calcular_similitud(respuestas_usuario, productos, pesos)
            # Ordenar productos por similitud descendente, pero ordena sin mas
            productos_similares = sorted(similitud.items(), key=lambda x: x[1], reverse=True)

            # Mostrar recomendaciones
            top_recomendaciones = 5
            for i in range(top_recomendaciones):
                index = productos_similares[i][0]
                recomendacion = productos.iloc[index]
                texto = f'Recomendación {i+1}: {recomendacion["producto"]} - {recomendacion["origen"]} -  {recomendacion["variedad"]} - {recomendacion["puntuacion_sca"]}  -  {recomendacion["url"]}'
                item = QListWidgetItem(texto)
                self.lista_recomendaciones.addItem(item)

if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec_()

#no implementado, se queria generar unas recomendaciones para el usuario segun sus respuestas a la encuesta.