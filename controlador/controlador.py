from vista.LoginVentana import LoginVentana
from vista.TriviaVentana import TriviaVentana
from vista.ModPasswordVentana import ModPasswordVentana
from vista.CrearUsuarioVentana import CrearUsuarioVentana
from vista.OpcionVentana import OpcionVentana
from Formulario.VentanaFormu import PreferenciasForm



class LoginControlador:
    def __init__(self, usuario_manager):
        self.usuario_manager = usuario_manager

    def iniciar_aplicacion(self):
        self.login_ventana = LoginVentana(self)
        self.login_ventana.show()

    def verificar_credenciales(self, usuario, contrasena):
        return self.usuario_manager.verificar_credenciales(usuario, contrasena)

    def mostrar_ventana_trivia(self, usuario):
        self.trivia_ventana = TriviaVentana(usuario)
        self.trivia_ventana.show()

    def mostrar_ventana_mod_password(self):
        self.mod_password_ventana = ModPasswordVentana(self.usuario_manager)
        self.mod_password_ventana.show()

    def mostrar_ventana_crear_usuario(self):
        self.crear_usuario_ventana = CrearUsuarioVentana(self.usuario_manager)
        self.crear_usuario_ventana.show()

    def mostrar_ventana_opciones(self, usuario):
        self.opcion_ventana = OpcionVentana(usuario, self)
        self.opcion_ventana.show()
    
    def mostrar_encuesta_cafe(self, usuario):
        self.encuesta_cafe = PreferenciasForm(usuario, self.usuario_manager)
        self.encuesta_cafe.show()
        
#Es Controlador Principal, que maneja las funciones y la ventanas para el menu principal