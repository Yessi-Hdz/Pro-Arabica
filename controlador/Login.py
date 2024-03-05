from vista.Mensajes import MensajeInterfazUsuario

class Login:
    def login(self, username_input, password_input, login_controlador, ventana):
        usuario = username_input.text()
        contrasena = password_input.text()

        if not usuario or not contrasena:
            MensajeInterfazUsuario.mostrar_advertencia(ventana, "Inserta un usuario y una contraseña.")
            return

        usuario = login_controlador.verificar_credenciales(usuario, contrasena)

        if usuario:
            MensajeInterfazUsuario.mostrar_informacion(ventana, "Inicio de sesión")
            login_controlador.mostrar_ventana_opciones(usuario)
            ventana.close() #si se inicia sesion y cierra la ventana
        else:
            MensajeInterfazUsuario.mostrar_error(ventana, "Usuario o contraseña incorrectas")
            #Deberia meter una opcion de restaurar contraseña enviando un email al final...

#Funcion de Inicializar al usuario, iniciar sesion.