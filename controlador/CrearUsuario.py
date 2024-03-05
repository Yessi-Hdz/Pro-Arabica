import re
from vista.Mensajes import MensajeInterfazUsuario

    
class CrearUsuario:
    def __init__(self, usuario_manager):
        self.usuario_manager = usuario_manager

    def crear_usuario(self, username, password, confirm_password, nombre, apellido, cp, email):
        # Verificar si todos los campos obligatorios estan llenos
        if not self.validar_campos_obligatorios(username, password, nombre, apellido, cp, email):
            return False
        
        # Verificar si las contraseñas coinciden y demas validadores
        if not self.validar_contrasenas(password, confirm_password):
            return False

        if not self.validar_formato_email(email):
            return False

        if not self.validar_formato_codigo_postal(cp):
            return False
        
        # Crear un nuevo objeto usuario con los datos recopilados en la ventana con getters
        nuevo_usuario_data = (None, username, password, nombre, apellido, cp, email)
    

        # Insertar el nuevo usuario 
        if self.usuario_manager.insertar_usuario(nuevo_usuario_data):
            MensajeInterfazUsuario.mostrar_informacion(None, "Usuario creado.")
            return True
        else:
            MensajeInterfazUsuario.mostrar_error(None, "No se pudo crear el usuario.")
            return False

    # son los validadores 4 de ellos los que vimos en clase
    def validar_campos_obligatorios(self, username, password, nombre, apellido, cp, email):
        if not username or not password or not nombre or not apellido or not cp or not email:
            MensajeInterfazUsuario.mostrar_advertencia(None, "Por favor, completa todos los campos.")
            return False
        return True

    def validar_contrasenas(self, password, confirm_password):
        if password != confirm_password:
            MensajeInterfazUsuario.mostrar_advertencia(None, "Las contraseñas no coinciden.")
            return False
        return True

    def validar_formato_email(self, email):
        patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(patron_email, email):
            MensajeInterfazUsuario.mostrar_advertencia(None, "El formato del email no es valido.")
            return False
        return True

    def validar_formato_codigo_postal(self, cp):
        patron_codigo_postal = r'\b\d{5}\b'
        if not re.match(patron_codigo_postal, cp):
            MensajeInterfazUsuario.mostrar_advertencia(None, "El formato del cp no es válido.")
            return False
        return True

#Este maneja las funciones de crear usuario