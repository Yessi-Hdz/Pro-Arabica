from PySide6.QtWidgets import QFormLayout


class FormularioController:
    def __init__(self, vista, db):
        self.vista = vista
        self.db = db

    def obtener_preguntas_y_opciones(self):
        return self.db.cargar_formulario_db()

    def obtener_respuestas(self):
        respuestas = {}
        for i in range(self.vista.formulario_layout.rowCount()):
            pregunta_widget = self.vista.formulario_layout.itemAt(i, QFormLayout.LabelRole).widget()
            pregunta = pregunta_widget.text()
            respuesta_widget = self.vista.formulario_layout.itemAt(i, QFormLayout.FieldRole).widget()
            respuesta = respuesta_widget.currentText()
            respuestas[pregunta] = respuesta
        print(respuestas)
        return respuestas

#Obtiene el diccionario con la preguntas y opciones pra la encuesta