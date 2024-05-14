# SISTEMA DE GESTIÓN DE BASE DE DATOS

# Módulos necesarios
import sqlite3, bcrypt

# ESTRUCTURA DE LAS FUNCIONES:

    # CREAR TABLA
 
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

    # USUARIOS Y CONTRASEÑAS

# Función que hashea las contraseñas
def hasher(password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password

# Función que comprueba si el hash coincide con la contraseña (devuelve True o False)
def comprobar_hash(password, hashed_password):
    comprobacion = bcrypt.checkpw(password.encode(), hashed_password)
    return comprobacion

# Buscar que hace
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

# Introduce los datos de usuario y contraseña si no están el BD
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


    # CORREO Y VERIFICACIÓN

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
#   user: usuario al que modificar el estado
#   future_status: nuevo estado al que se desea cambiar (0 FALSE, 1 TRUE)
def update_email_status(user, future_status):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute("UPDATE security SET everification = ? WHERE user = ?", (future_status, user))
    db.commit()
    db.close()

def update_all_email_status(future_status):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM security")
    total_users = cursor.fetchone()[0]
    for i in range(total_users):
        cursor.execute("UPDATE security SET everification = ?", (future_status,))
    db.commit()
    db.close()
    print("Todos los estados han sido actualizados")
    
def saber_user_con_email(email):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()

    cursor.execute("SELECT user FROM security WHERE email = ?", (email,))
    user = cursor.fetchone()
    db.commit()
    db.close()

    if user:
        return user[0]
    else:
        return None

    # BORRAR DATOS

# Función que borra una tabla
def borrar_tabla(tabla):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {tabla}")
    db.commit()
    db.close()
    print(f"La tabla '{tabla}' ha sido eliminada")

# Si alguien ve esto, hay que vincular esta fución con eliminar cuenta (antes hay que hacer la verificación con el código del gmail)
def drop_user_info(user):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM security WHERE user = ?", (user,))
    db.commit()
    db.close()
    print(f"El usuario '{user}' ha  sido eliminado de la base de datos")


