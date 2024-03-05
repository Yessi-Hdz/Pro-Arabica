import sqlite3
from Usuario.Usuario import Usuario

class BaseDatosManager:
    def __init__(self, db_file):
        self.db_file = db_file
    
    def abrir_conexion(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        return conn, cursor

    def cerrar_conexion(self, conn):
        conn.close()

    #Para cargar la lista [] 
    def obtener_todos_usuarios(self):
        conn, cursor = self.abrir_conexion()
        cursor.execute("SELECT * FROM usuarios")
        usuarios_data = cursor.fetchall()
        self.cerrar_conexion(conn)

        usuarios = []
        for usuario_data in usuarios_data:
            usuario = Usuario(*usuario_data)
            usuarios.append(usuario)

        return usuarios

    #para modificar la db con la lista modificada
    def actualizar_usuario(self, usuario):
        conn, cursor = self.abrir_conexion()
        try:
            cursor.execute('''UPDATE usuarios 
                            SET usuario=?, contrasena=?, nombre=?, apellido=?, cp=?, email=? 
                            WHERE usuario_id=?''',
                            (usuario.usuario, usuario.contrasena, usuario.nombre, usuario.apellido, usuario.cp, usuario.email, usuario.usuario_id))
            conn.commit()
            self.cerrar_conexion(conn)
            print("Usuario actualizado correctamente en la base de datos.")
            return True
            
        except sqlite3.Error as e:
            print("Error al actualizar usuario en la base de datos:", e)
            self.cerrar_conexion(conn)
            return False

    #aqui ingreso el nuevo usuario
    def insertar_usuario(self, usuario):
        if not usuario.usuario or not usuario.contrasena:
            print("Usuario y contraseña son obligatorios.")
            return False

        conn, cursor = self.abrir_conexion()
        try:
            cursor.execute('''INSERT INTO usuarios (usuario, contrasena, nombre, apellido, cp, email)
                            VALUES (?, ?, ?, ?, ?, ?)''',
                            (usuario.usuario, usuario.contrasena, usuario.nombre, usuario.apellido, usuario.cp, usuario.email))
            conn.commit()
            print("Usuario insertado correctamente.")
            return True
        except sqlite3.IntegrityError:
            print("El usuario ya existe.")
            return False
        except sqlite3.Error as e:
            print("Error al insertar usuario:", e)
            return False
        finally:
            self.cerrar_conexion(conn)

    #se da paso al iniciar login
    def verificar_credenciales(self, usuario, contrasena):
        conn, cursor = self.abrir_conexion()
        cursor.execute('''SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?''', (usuario, contrasena))
        usuario_data = cursor.fetchone()
        self.cerrar_conexion(conn)

        if usuario_data:
            return Usuario(*usuario_data)
        else:
            return None
        
    # lo he agregado aqui por que es la misma base de datos que se modifica, 
    def mod_password(self, usuario, old_password, new_password):
        conn, cursor = self.abrir_conexion()
        
        # Verificar la contraseña antigua del usuario
        cursor.execute("SELECT contrasena FROM usuarios WHERE usuario=?", (usuario,))
        stored_password = cursor.fetchone()
        
        if not stored_password:
            self.cerrar_conexion(conn)
            return False, "Usuario no encontrado"
        
        if stored_password[0] != old_password:
            self.cerrar_conexion(conn)
            return False, "La contraseña antigua es incorrecta"
        
        # Actualiza la contraseña del usuario
        cursor.execute("UPDATE usuarios SET contrasena=? WHERE usuario=?", (new_password, usuario))
        conn.commit()
        self.cerrar_conexion(conn)
        
        return True, "Contraseña modificada exitosamente"