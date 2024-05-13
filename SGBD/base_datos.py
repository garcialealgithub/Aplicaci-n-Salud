# SISTEMA DE GESTIÓN DE BASE DE DATOS

# Módulos necesarios
import sqlite3, bcrypt


# Función que hashea las contraseñas
def hasher(password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password

# Función que comprueba si el hash coincide con la contraseña
def comprobar_hash(password, hashed_password):
    comprobacion = bcrypt.checkpw(password.encode(), hashed_password)
    return comprobacion




# BASE DE DATOS

def crear_tabla(tabla):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS security 
               (user TEXT PRIMARY KEY, 
               password TEXT NOT NULL,
               email TEXT,
               everification BOOLEAN)""")
    db.commit()
    db.close()



def password_verification(usuario):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    consulta = f"SELECT password FROM security WHERE user = ?;"
    cursor.execute(consulta, (usuario,))
    resultado = cursor.fetchone()
    db.commit()
    db.close()

    if resultado:
        return resultado[0]
    else:
        return "Usuario no encontrado"
    
    





# Función que borra una tabla
def borrar_tabla(tabla):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {tabla}")
    db.commit()
    db.close()
    print(f"La tabla '{tabla}' ha sido eliminada")



def insert_user_info(user, password):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    # Verificamos que exista el usuario
    cursor.execute(f"SELECT * FROM security WHERE user = ?", (user,))
    data = cursor.fetchone()
    # Si el usuario no existe introduce los valores
    if data is None:
        cursor.execute(f"INSERT INTO security (user, password) VALUES (?, ?)", (user, password))
        db.commit()
        db.close()
    else:
        print(f"El usuario {user} ya existe en la base de datos.")
        db.close()

def insert_user_email(user, email):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()

    cursor.execute("SELECT email FROM security WHERE user = ?", (user,))
    data = cursor.fetchone()

    if data:
        if data[0] is None:
            cursor.execute("UPDATE security SET email = ? WHERE user = ?", (email, user))
            print(f"El email '{email}' ha sido añadido correctamente para el usuario '{user}'")
        else:
            print(f"El usuario '{user}' ya tiene un email asignado")
    else:
        print(f"El usuario '{user}' no existe en nuestra BD")

    db.commit()
    db.close()


# Así funcionan los parámetros:
#   future_status es el estado al que quieres cambiar (1 es verificado)
#   status es el estado actual (al crearla es NULL, 0 es false) --> la primera vez pongamos todo a 0: future_status = 0, status = NULL
def insert_email_status(user, future_status, status):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute(f"UPDATE security SET everification = {status} WHERE everification = {status}; ") #Al crear la tabla es NULL (hay que cambiarlo)
    db.commit()
    db.close()


# Añadir bucle for (tiene que ser capaz de saber el número total de usuarios antes del bucle)
def update_users_status(future_status):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute(f"UPDATE security SET everification = {future_status} WHERE everification != {future_status}; ")
    db.commit()
    db.close()

    




# Si alguien ve esto, hay que vincular esta fución con eliminar cuenta (antes hay que hacer la verificación con el código del gmail)
def drop_user_info(user):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM security WHERE user = ?", (user,))
    db.commit()
    db.close()
    print(f"El usuario '{user}' ha  sido eliminado de la base de datos")

