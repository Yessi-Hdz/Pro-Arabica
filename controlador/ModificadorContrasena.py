from vista.Mensajes import MensajeInterfazUsuario


class ModificadorContrasena:
    def __init__(self, usuario_manager):
        self.usuario_manager = usuario_manager

    def modificar_contrasena(self, username_input, old_password_input, new_password_input, confirm_new_password_input):
        usuario = username_input.text()
        old_password = old_password_input.text()
        new_password = new_password_input.text()
        confirm_new_password = confirm_new_password_input.text()

        if not usuario or not old_password or not new_password or not confirm_new_password:
            MensajeInterfazUsuario.mostrar_error(None, "Error, Por favor, complete todos los campos.")
            return

        if new_password != confirm_new_password:
            MensajeInterfazUsuario.mostrar_error(None, "Error, Las contraseñas no coinciden.")
            return

        success = self.usuario_manager.mod_password(usuario, old_password, new_password)

        if success:
            MensajeInterfazUsuario.mostrar_informacion(None, "Perfecto, Contraseña modificada.")
            username_input.clear()
            old_password_input.clear()
            new_password_input.clear()
            confirm_new_password_input.clear()
        else:
            MensajeInterfazUsuario.mostrar_error(None, "Error, No se pudo modificar la pass.")

#Gestiona la funcion de modificar al usuario ya creado.