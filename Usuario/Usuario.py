#Los getters y setters 

class Usuario:
    def __init__(self, usuario_id, usuario, contrasena, nombre, apellido, cp, email):
        self._usuario_id = usuario_id
        self._usuario = usuario
        self._contrasena = contrasena
        self._nombre = nombre
        self._apellido = apellido
        self._cp = cp
        self._email = email

    @property
    def usuario_id(self):
        return self._usuario_id

    @property
    def usuario(self):
        return self._usuario

    @property
    def contrasena(self):
        return self._contrasena

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def cp(self):
        return self._cp

    @property
    def email(self):
        return self._email

    @usuario.setter
    def usuario(self, nuevo_usuario):
        self._usuario = nuevo_usuario

    @contrasena.setter
    def contrasena(self, nuevo_contrasena):
        self._contrasena = nuevo_contrasena

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @cp.setter
    def cp(self, nuevo_cp):
        self._cp = nuevo_cp

    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email
        