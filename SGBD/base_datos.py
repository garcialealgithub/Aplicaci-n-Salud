# SISTEMA DE GESTIÓN DE BASE DE DATOS

# Módulos necesarios
import sqlite3, bcrypt

# Función que hashea las contraseñas
def hasher(password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password

# Función que comprueba si el hash coincide con la contraseña
def comprobar_hash(password, hashed_password):
    password = bcrypt.checkpw(password.encode(), hashed_password)
    return password



ejemplos = [["paco", "djklf"], ["ruben", "dkj985"], ["carlos", "ejkr"], ["ivan", "kjdjf"], ["jonh", "dkfjd"]]

ejemplos_usuarios = {"user" : "password"}
for i in range(len(ejemplos)):
    ejemplos_usuarios[ejemplos[i][0]] = hasher(ejemplos[i][1])

print(ejemplos_usuarios)


# BASE DE DATOS


db = sqlite3.connect("SGBD/data.db")
cursor = db.cursor()

# Creamos las tablas
cursor.execute("""CREATE TABLE IF NOT EXISTS security 
               (user TEXT PRIMARY KEY, 
               password TEXT NOT NULL)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS data 
               (user TEXT PRIMARY KEY,
               datos INT,
               datos_2 INT,
               datos_3 INT,
               datos_4 INT,
               datos_5 INT)""")
db.commit()



# Función que borra una tabla
def borrar_tabla(cursor, tabla):
    cursor.execute(f"DROP TABLE IF EXISTS {tabla}")
    db.commit()

def insertar_datos(cursor, tabla, user, password):
    cursor.execute(f"INSERT INTO {tabla} (user, password) VALUES (?, ?)", (user, password))
    db.commit()

for user, password in ejemplos_usuarios.items():
    insertar_datos(cursor, tabla = "security", user = user, password = password)

















db.close()