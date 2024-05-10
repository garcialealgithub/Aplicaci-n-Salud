# SISTEMA DE GESTIÓN DE BASE DE DATOS

# Módulos necesarios
import sqlite3, bcrypt, time

# Función que hashea las contraseñas
def hasher(password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password

# Función que comprueba si el hash coincide con la contraseña
def comprobar_hash(password, hashed_password):
    comprobacion = bcrypt.checkpw(password.encode(), hashed_password)
    return comprobacion




# BASE DE DATOS

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
    cursor.execute("""CREATE TABLE IF NOT EXISTS security 
               (user TEXT PRIMARY KEY, 
               password TEXT NOT NULL)""")
    cursor.execute(f"SELECT * FROM security WHERE user = ?", (user,))
    data = cursor.fetchone()
    if data is None:
        cursor.execute(f"INSERT INTO security (user, password) VALUES (?, ?)", (user, password))
        db.commit()
        db.close()
    else:
        print(f"El usuario {user} ya existe en la base de datos.")
        db.close()


# Si alguien ve esto, hay que vincular esta fución con eliminar cuenta (antes hay que hacer la verificación con el código del gmail)
def drop_user_info(user):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM security WHERE user = ?", (user,))
    db.commit()
    db.close()
    print(f"El usuario '{user}' ha  sido eliminado de la base de datos")

