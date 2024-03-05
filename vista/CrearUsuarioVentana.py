from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,  QMainWindow
from controlador.CrearUsuario import CrearUsuario


class CrearUsuarioVentana(QMainWindow):
    def __init__(self, usuario_manager):
        super().__init__()
        self.usuario_manager = usuario_manager
        self.setWindowTitle("Crear Usuario")
        self.setGeometry(200, 200, 500, 200)

        layout = QVBoxLayout()

        self.username_label = QLabel("Nuevo Usuario")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Ingrese el usuario")

        self.nombre_label = QLabel("Nombre")
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Ingrese Nombre")

        self.apellido_label = QLabel("Apellido")
        self.apellido_input = QLineEdit()
        self.apellido_input.setPlaceholderText("Ingrese Apellido")

        self.cp_label = QLabel("Código Postal")  
        self.cp_input = QLineEdit()             
        self.cp_input.setPlaceholderText("Ingrese CP")  

        self.email_label = QLabel("Email")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Ingrese Email")

        self.password_label = QLabel("Contraseña")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Ingrese la contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.confirm_password_label = QLabel("Confirmar Contraseña")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirme la contraseña")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)#pone***

        self.create_button = QPushButton("Crear Usuario")
        self.create_button.clicked.connect(self.crear_usuario1)
        
        self.salir_button = QPushButton("Salir")
        self.salir_button.clicked.connect(self.salir)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.apellido_label)
        layout.addWidget(self.apellido_input)
        layout.addWidget(self.cp_label)       
        layout.addWidget(self.cp_input)       
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)
        layout.addWidget(self.create_button)
        layout.addWidget(self.salir_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def crear_usuario1(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        cp = self.cp_input.text()
        email = self.email_input.text()

        crear_usuario = CrearUsuario(self.usuario_manager)
        crear_usuario.crear_usuario(username, password, confirm_password,
                                    nombre, apellido, cp,
                                    email)

    def salir(self):
        self.close()