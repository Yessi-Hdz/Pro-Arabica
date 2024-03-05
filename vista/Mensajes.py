from PySide6.QtWidgets import QMessageBox

class MensajeInterfazUsuario:
    @staticmethod
    def mostrar_advertencia(ventana, mensaje):
        QMessageBox.warning(ventana, "Advertencia", mensaje)

    @staticmethod
    def mostrar_informacion(ventana, mensaje):
        QMessageBox.information(ventana, "Información", mensaje)

    @staticmethod
    def mostrar_error(ventana, mensaje):
        QMessageBox.critical(ventana, "Error", mensaje)

#Gestiona las comunicaciones de las ventanas, solo define 3