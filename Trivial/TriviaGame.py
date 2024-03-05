from modelo.TriviaDB import TriviaDB
from vista.Mensajes import MensajeInterfazUsuario

class TriviaGame:
    def __init__(self, trivia_ventana):
        self.trivia_ventana = trivia_ventana
        self.preguntas = TriviaDB.cargar_preguntas_db() #nos devuelve la lista, del modelo trivia
        self.puntos = 0
        self.total_preguntas = 0
        self.preguntas_respondidas = 0
        self.tiempo_restante = 0

    # en preguntas se cargan desde TriviaDB 
    def mostrar_pregunta(self):
        if self.preguntas:
            pregunta_actual = self.preguntas.pop(0)
            self.trivia_ventana.question_label.setText(pregunta_actual["pregunta"])
            self.trivia_ventana.option1_radio.setText(pregunta_actual["opciones"][0])
            self.trivia_ventana.option2_radio.setText(pregunta_actual["opciones"][1])
            self.trivia_ventana.option3_radio.setText(pregunta_actual["opciones"][2])
            self.trivia_ventana.respuesta_correcta = pregunta_actual["respuesta_correcta"]
            self.total_preguntas += 1
            self.tiempo_restante = 10
            self.trivia_ventana.timer.start(1000)
        else:
            self.trivia_ventana.timer.stop()
            MensajeInterfazUsuario.mostrar_informacion(self.trivia_ventana, f"Fin del Trivial. Has obtenido {self.puntos} puntos de {self.total_preguntas} preguntas.")

    def check_answer(self, respuesta):
        if respuesta == self.trivia_ventana.respuesta_correcta:
            MensajeInterfazUsuario.mostrar_informacion(self.trivia_ventana, "¡Respuesta Correcta!")
            self.puntos += 1
        else:
            MensajeInterfazUsuario.mostrar_informacion(self.trivia_ventana, f"Respuesta Incorrecta. La respuesta correcta es: {self.trivia_ventana.respuesta_correcta}")

        self.trivia_ventana.puntos_label.setText(f"Puntos: {self.puntos}/{self.total_preguntas}")
        self.preguntas_respondidas += 1
        self.trivia_ventana.timer.stop()
        self.mostrar_pregunta()

    #el tiempo que siempre esta contando :P
    def actualizar_temporizador(self):
        self.tiempo_restante -= 1
        if self.tiempo_restante <= 0:
            MensajeInterfazUsuario.mostrar_informacion(self.trivia_ventana, "Tiempo Expirado. Se acabó el tiempo para responder.")
            self.check_answer("")  # Se pasa una respuesta vacia para indicar que no se selecciono ninguna opcion
            self.trivia_ventana.timer.stop()

#carga la preguntas y opciones de la trivia, de acuerdo  a la ventana