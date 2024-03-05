from Usuario.Usuario import Usuario
from modelo.modelo import BaseDatosManager

class UsuarioManager:
    def __init__(self, db_file):
        self.db_manager = BaseDatosManager(db_file)
        self.lista_usuarios = []
        self.cargar_usuarios_desde_db()

    def cargar_usuarios_desde_db(self):
        self.lista_usuarios = self.db_manager.obtener_todos_usuarios()
        print("Usuarios cargados correctamente desde la base de datos:")
        for usuario in self.lista_usuarios:
            print("ID:", usuario.usuario_id, "Usuario:", usuario.usuario)
    #carga de la db los datos para la lista local

    def insertar_usuario(self, nuevo_usuario_data):
        usuario = Usuario(*nuevo_usuario_data)
        if not usuario.usuario or not usuario.contrasena:
            print("Usuario y contraseña es obligado.")
            return False
        self.lista_usuarios.append(usuario) 
        if self.db_manager.insertar_usuario(usuario):
            print("Usuario insertado bien.")
            return True
        else:
            print("No se pudo insertar.")
            return False

    def verificar_credenciales(self, nombre_usuario, contrasena):
        for usuario in self.lista_usuarios:
            if usuario.usuario == nombre_usuario and usuario.contrasena == contrasena:
                return usuario
        return False

    def mod_password(self, nombre_usuario, old_password, new_password):
        for usuario in self.lista_usuarios:
            if usuario.usuario == nombre_usuario and usuario.contrasena == old_password:
                usuario.contrasena = new_password
                print("Contraseña modificada.")
                return True
        print("No se pude modificar la pass.")
        return False

    def obtener_id_usuario(self, nombre_usuario):
        for usuario in self.lista_usuarios:
            if usuario.usuario == nombre_usuario:
                return usuario.usuario_id
        return None 

    def guardar_cambios_en_db(self):
        for usuario in self.lista_usuarios:
            if usuario:
                self.db_manager.actualizar_usuario(usuario)
        print("Cambios realizados en db, al cerrar.")

#Gestiona al usuario y las funciones que le afectan