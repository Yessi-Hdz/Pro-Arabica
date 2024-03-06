from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow
from controlador.ModificadorContrasena import ModificadorContrasena

class ModPasswordVentana(QMainWindow):
    def __init__(self, usuario_manager):
        super().__init__()
        self.usuario_manager = usuario_manager
        self.setWindowTitle("Modificar Contraseña")
        self.setGeometry(100, 100, 300, 200)
        

        layout = QVBoxLayout()

        self.username_label = QLabel("Usuario:")
        self.username_input = QLineEdit()

        self.old_password_label = QLabel("Contraseña Actual:")
        self.old_password_input = QLineEdit()
        self.old_password_input.setEchoMode(QLineEdit.Password)

        self.new_password_label = QLabel("Nueva Contraseña:")
        self.new_password_input = QLineEdit()
        self.new_password_input.setEchoMode(QLineEdit.Password)

        self.confirm_new_password_label = QLabel("Confirmar Nueva Contraseña:")
        self.confirm_new_password_input = QLineEdit()
        self.confirm_new_password_input.setEchoMode(QLineEdit.Password)

        self.modify_button = QPushButton("Modificar")
        self.modify_button.clicked.connect(self.modificar_contrasena)
        
        self.salir_button = QPushButton("Salir")
        self.salir_button.clicked.connect(self.salir)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.old_password_label)
        layout.addWidget(self.old_password_input)
        layout.addWidget(self.new_password_label)
        layout.addWidget(self.new_password_input)
        layout.addWidget(self.confirm_new_password_label)
        layout.addWidget(self.confirm_new_password_input)
        layout.addWidget(self.modify_button)
        layout.addWidget(self.salir_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    #llama a ModContraseña del controlador
    def modificar_contrasena(self):
        control = ModificadorContrasena(self.usuario_manager)
        control.modificar_contrasena(self.username_input, self.old_password_input, self.new_password_input, self.confirm_new_password_input)
        
    def salir(self):
        self.close()
        self.usuario_manager.guardar_cambios_en_db() #Al final esta es la linea que me faltaba
