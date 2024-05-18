# SISTEMA DE GESTIÓN DE BASE DE DATOS

# Módulos necesarios
import sqlite3, bcrypt, csv
from tkinter import messagebox

# ESTRUCTURA DE LAS FUNCIONES:

    # CREAR TABLA
 
def crear_tabla_security():
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS security 
               (user TEXT PRIMARY KEY, 
               password TEXT NOT NULL,
               edad INT,
               sexo TEXT,
               email TEXT,
               everification BOOLEAN)""")
    db.commit()
    db.close()

def añadir_datos_security(users, hashed_passwords, sexo, edad, correo, email_status):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()

    for i in range(len(users)):
        cursor.execute('''
        INSERT INTO security (user, password, edad, sexo, email, everification) 
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (users[i], hashed_passwords[i], edad[i], sexo[i], correo[i], email_status[i]))
    
    db.commit()
    db.close()

def crear_tabla_weight():

    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE weight (
    user TEXT,
    date TEXT,
    peso REAL,
    PRIMARY KEY(user, date),
    FOREIGN KEY(user) REFERENCES security(user)
)
''')
        
    db.commit()
    db.close()


def añadir_datos_weight_from_csv():
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()

    # Abrir el archivo CSV y leer los datos
    with open("SGBD/weight.csv", 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = row['user']
            date = row['date']
            weight = float(row['weight'])  # Convertir a tipo float si es necesario
            # Verificar si ya existe una fila con la misma combinación de date y user
            cursor.execute('''
            SELECT * FROM weight WHERE date = ? AND user = ?
            ''', (date, user))
            existing_row = cursor.fetchone()
            # Insertar el nuevo registro si no existe una fila con la misma combinación de date y user
            if existing_row is None:
                cursor.execute('''
                INSERT INTO weight (user, date, peso) 
                VALUES (?, ?, ?)
                ''', (user, date, weight))
    
    db.commit()
    db.close()

def crear_tabla_steps():

    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE steps (
    user TEXT,
    date TEXT,
    pasos INT,
    PRIMARY KEY(user, date),
    FOREIGN KEY(user) REFERENCES security(user)
)
''')
        
    db.commit()
    db.close()


def añadir_datos_steps_from_csv():
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()

    # Abrir el archivo CSV y leer los datos
    with open("SGBD/steps.csv", 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = row['user']
            date = row['date']
            pasos = float(row['number_of_steps'])  # Convertir a tipo float si es necesario
            # Verificar si ya existe una fila con la misma combinación de date y user
            cursor.execute('''
            SELECT * FROM steps WHERE date = ? AND user = ?
            ''', (date, user))
            existing_row = cursor.fetchone()
            # Insertar el nuevo registro si no existe una fila con la misma combinación de date y user
            if existing_row is None:
                cursor.execute('''
                INSERT INTO steps (user, date, pasos) 
                VALUES (?, ?, ?)
                ''', (user, date, pasos))
    
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
def insert_user_info(user, password, edad, sexo):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    # Verificamos que exista el usuario
    cursor.execute(f"SELECT * FROM security WHERE user = ?", (user,))
    data = cursor.fetchone()
    # Si el usuario no existe introduce los valores
    if data is None:
        cursor.execute(f"INSERT INTO security (user, password, sexo, edad) VALUES (?, ?, ?, ?)", (user, password, sexo, edad))
        db.commit()
        db.close()
        return True
    else:
        messagebox.showerror("Error", "El usuario ya existe")
        db.close() 
        return False


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



# Función que borra una tabla
def borrar_tabla(tabla):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {tabla}")
    db.commit()
    db.close()
    print(f"La tabla '{tabla}' ha sido eliminada")

# Función que borra un usuario
def drop_user_info(user):
    try:
        db = sqlite3.connect("SGBD/data.db")
        cursor = db.cursor()
        cursor.execute("DELETE FROM security WHERE user = ?", (user,))
        db.commit()
        db.close()
        messagebox.showinfo("Correcto", "Usuario eliminado correctamente")
    except:
        messagebox.showerror("Error", "No se ha podido eliminar el usuario")


def change_password(user, new_password):
    try:
        new_password = hasher(new_password)
        db = sqlite3.connect("SGBD/data.db")
        cursor = db.cursor()
        cursor.execute("UPDATE security SET password = ? WHERE user = ?", (new_password, user))
        db.commit()
        db.close()
        return True
    except Exception as e:
        messagebox.showerror("Error", str(e))
        
def saber_email(user):
    db = sqlite3.connect("SGBD/data.db")
    cursor = db.cursor()
    cursor.execute("SELECT email FROM security WHERE user = ?", (user,))
    data = cursor.fetchone()
    db.commit()
    db.close()
    return data[0]