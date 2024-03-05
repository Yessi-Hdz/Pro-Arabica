from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMainWindow


class OpcionVentana(QMainWindow):
    def __init__(self, usuario, login_controlador):
        super().__init__()
        self.setWindowTitle(f"Opciones para {usuario.usuario}")
        self.setGeometry(200, 100, 300, 200)
        self.usuario = usuario
        self.login_controlador = login_controlador

        layout = QVBoxLayout()

        self.username_label = QLabel(f"Bienvenido {usuario.usuario}")
        self.mod_password_button = QPushButton("Modificar Contraseña")
        self.mod_password_button.clicked.connect(self.mod_password)

        self.play_trivia_button = QPushButton("Jugar Trivial")
        self.play_trivia_button.clicked.connect(self.play_trivia)

        self.play_encuesta_button = QPushButton("Encuesta Cafe")
        self.play_encuesta_button.clicked.connect(self.play_encuesta)
        
        self.salir_button = QPushButton("Salir")
        self.salir_button.clicked.connect(self.salir)

        layout.addWidget(self.username_label)
        layout.addWidget(self.mod_password_button)
        layout.addWidget(self.play_trivia_button)
        layout.addWidget(self.play_encuesta_button)
        layout.addWidget(self.salir_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    #son metodos? para llamar a las siguientes ventanas
    def mod_password(self):
        self.login_controlador.mostrar_ventana_mod_password()

    def play_trivia(self):
        self.login_controlador.mostrar_ventana_trivia(self.usuario)

    def play_encuesta(self):
        self.login_controlador.mostrar_encuesta_cafe(self.usuario)
        
    def salir(self):
        self.close()
