from PySide6.QtWidgets import QApplication
from Usuario.Usuarios import UsuarioManager
from controlador.controlador import LoginControlador


if __name__ == "__main__":
    app = QApplication([])

    db_file = "BD/BasesDatos/usuarios.db" 
    usuario_manager = UsuarioManager(db_file)
    login_controlador = LoginControlador(usuario_manager)
    login_controlador.iniciar_aplicacion()

    app.exec()