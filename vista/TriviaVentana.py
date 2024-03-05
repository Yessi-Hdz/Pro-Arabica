from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMainWindow, QRadioButton
from PySide6.QtCore import QTimer
from Trivial.TriviaGame import TriviaGame
from modelo.TriviaDB import TriviaDB


class TriviaVentana(QMainWindow):
    def __init__(self, usuario):
        super().__init__()
        self.setWindowTitle("Trivia")
        self.setGeometry(100, 100, 500, 300)

        self.usuario = usuario

        self.layout = QVBoxLayout()

        self.username_label = QLabel(f"Bienvenido {usuario.usuario}")
        self.layout.addWidget(self.username_label)

        self.puntos_label = QLabel("Puntos: 0/0")
        self.layout.addWidget(self.puntos_label)
        
        self.question_label = QLabel()
        self.layout.addWidget(self.question_label)

        self.option1_radio = QRadioButton()
        self.layout.addWidget(self.option1_radio)

        self.option2_radio = QRadioButton()
        self.layout.addWidget(self.option2_radio)

        self.option3_radio = QRadioButton()
        self.layout.addWidget(self.option3_radio)

        self.submit_button = QPushButton("Enviar Respuesta")
        self.submit_button.clicked.connect(self.check_answer1)
        self.layout.addWidget(self.submit_button)
        
        #cree este boton revisar queria poner un icono pero L=l
        self.salir_button = QPushButton("Salir")
        self.salir_button.clicked.connect(self.salir)
        self.layout.addWidget(self.salir_button)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        # Inicializa el juego trivia
        self.trivia_game = TriviaGame(self)
        self.trivia_game.preguntas = TriviaDB.cargar_preguntas_db()

        # Configurar el temporizador
        self.timer = QTimer()
        self.timer.timeout.connect(self.trivia_game.actualizar_temporizador)
        self.timer.start(1000)
        
        # Mostrar la primera pregunta
        self.trivia_game.mostrar_pregunta()

    #llama a TriviaGame del controlador y pasa la forma
    def check_answer1(self):
        respuesta = None
        if self.option1_radio.isChecked():
            respuesta = self.option1_radio.text()
        elif self.option2_radio.isChecked():
            respuesta = self.option2_radio.text()
        elif self.option3_radio.isChecked():
            respuesta = self.option3_radio.text()
    
        self.trivia_game.check_answer(respuesta)
        
    def salir(self):
        self.close()