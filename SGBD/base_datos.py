# SISTEMA DE GESTIÓN DE BASE DE DATOS

# Módulos necesarios
import sqlite3, bcrypt, time

# Función que hashea las contraseñas
def hasher(password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password

# Función que comprueba si el hash coincide con la contraseña
def comprobar_hash(password, hashed_password):
    password = bcrypt.checkpw(password.encode(), hashed_password)
    return password




# BASE DE DATOS
db = sqlite3.connect("SGBD/data.db")
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS security 
               (user TEXT PRIMARY KEY, 
               password TEXT NOT NULL)""")





# Función que borra una tabla
def borrar_tabla(tabla):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {tabla}")
    db.commit()
    db.close()

def insert_security(user, password):
    cursor.execute(f"SELECT * FROM security WHERE user = ?", (user,))
    data = cursor.fetchone()
    if data is None:
        cursor.execute(f"INSERT INTO security (user, password) VALUES (?, ?)", (user, password))
        db.commit()
        db.close()
    else:
        print(f"El usuario {user} ya existe en la base de datos.")
        db.close()










