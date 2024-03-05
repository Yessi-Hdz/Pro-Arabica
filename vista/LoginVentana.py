from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow
from controlador.Login import Login


class LoginVentana(QMainWindow):
    def __init__(self, login_controlador):
        super().__init__()
        self.login_controlador = login_controlador
        
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(400, 300, 300, 250)

        layout = QVBoxLayout()

        self.username_label = QLabel("Usuario:")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Contraseña:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.clicked.connect(self.login_inicio)

        self.crear_usuario_button = QPushButton("Crear Usuario")
        self.crear_usuario_button.clicked.connect(self.crear_usuario)
        
        self.salir_button = QPushButton("Salir")
        self.salir_button.clicked.connect(self.salir)
        
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.crear_usuario_button)
        layout.addWidget(self.salir_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    #se llama al Login del controlador 
    def login_inicio(self):
        login = Login()
        login.login(self.username_input, self.password_input, self.login_controlador, self)

    #se llama al CrearUsuario del controlador 
    def crear_usuario(self):
        self.login_controlador.mostrar_ventana_crear_usuario()
    
    #cierra ventana
    def salir(self):
        self.close()
    