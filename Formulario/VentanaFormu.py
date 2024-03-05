from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QPushButton, QComboBox, QLabel, QHBoxLayout
from .ModeloFormu import FormuDB, UserDB
from .ControlFormu import FormularioController
from Usuario.Usuarios import UsuarioManager
from vista.Mensajes import MensajeInterfazUsuario
from Formulario.Formulario import encuesta

class PreferenciasForm(QWidget, encuesta):
    def __init__(self, usuario, usuario_manager):
        super().__init__()
        self.setWindowTitle("Encuesta de Preferencias de Café")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.usuario = usuario
        self.usuario_manager = usuario_manager
        
        self.username_label = QLabel(f"Bienvenido {usuario.usuario}, Dime tus gustos")
        self.layout.addWidget(self.username_label)
        #muetsra el nombre
        self.formulario_layout = QFormLayout()
        self.layout.addLayout(self.formulario_layout)

        # Inicia el formulario
        self.formula = FormularioController(self, FormuDB())
        preguntas_opciones = self.formula.obtener_preguntas_y_opciones()

        #Que se pasa aqui el setter? o para mostrarlo al formulario?
        self._respuestas = {}
        for id_pregunta, pregunta, opciones in preguntas_opciones:
            label_pregunta = QLabel(pregunta)
            combo = QComboBox()
            combo.addItems(opciones)
            self.formulario_layout.addRow(label_pregunta, combo)

        # Espaciado entre los elementos
        self.layout.addSpacing(25)

        # Botones Aceptar y salir
        btn_aceptar_layout = QHBoxLayout()
        self.layout.addLayout(btn_aceptar_layout)
        btn_aceptar_layout.addStretch(1)
        btn_aceptar = QPushButton("Aceptar")
        btn_aceptar.clicked.connect(self.enviar_respuestas)
        btn_aceptar_layout.addWidget(btn_aceptar)
        btn_aceptar_layout.addStretch(1)

        btn_salir = QPushButton("Salir")
        btn_salir.clicked.connect(self.salir)
        btn_aceptar_layout.addWidget(btn_salir)
        btn_aceptar_layout.addStretch(1)

        # Centrar la ventana en pantalla
        self.center()

    def center(self):
        # Centrar la ventana en pantalla
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().geometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def salir(self):
        self.close()

    def enviar_respuestas(self):
        # Obtener el ID del usuario, me costo un mundo
        usuario_id = self.usuario_manager.obtener_id_usuario(self.usuario.usuario)

        # Recorrer el formulario y obtener las respuestas
        respuestas = []
        for index in range(self.formulario_layout.rowCount()):
            pregunta_widget = self.formulario_layout.itemAt(index, QFormLayout.LabelRole).widget()
            respuesta_widget = self.formulario_layout.itemAt(index, QFormLayout.FieldRole).widget()

            pregunta_texto = pregunta_widget.text()
            respuesta = respuesta_widget.currentText()

            respuestas.append(respuesta)

            print("Pregunta:", pregunta_texto)
            print("Respuesta:", respuesta)
        
        # Verificar si hay 11 respuestas, modo de comprobacion
        if len(respuestas) != 11:
            print("Número incorrecto de respuestas.")
            return

        # Guardar todas las respuestas en la db de preferencias del usuario
        user_db = UserDB()
        print("ID de usuario obtenido:", usuario_id)
        user_db.guardar_respuesta_encuesta(usuario_id, respuestas)
        user_db.cerrar_conexion()

        print("Respuestas enviadas exitosamente.")
        MensajeInterfazUsuario.mostrar_informacion(None, "Respuestas enviadas exitosamente.")
