import sqlite3, inicio_sesion
import SGBD.base_datos as BD

ejemplos = inicio_sesion.plain_passwords


def obtener_password_hash(usuario):
    # Conectar a la base de datos
    conexion = sqlite3.connect('SGBD/data.db')
    cursor = conexion.cursor()

    # Consulta SQL para obtener la contraseña hasheada del usuario
    consulta = "SELECT password FROM security WHERE user = ?"
    cursor.execute(consulta, (usuario,))
    resultado = cursor.fetchone()

    # Cerrar la conexión con la base de datos
    conexion.close()

    if resultado:
        return resultado[0]
    else:
        return "Usuario no encontrado"

for user, password in ejemplos.items():
    print(obtener_password_hash(usuario=user))
    print(BD.hasher(password))