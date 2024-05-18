import base_datos as BD
import _sqlite3, csv
# FUNCIÓN QUE BORRA TABLAS: BD.borrar_tabla(tabla = "")
# BD.borrar_tabla(tabla="security")

# --- SECURITY ---
# FUNCIÓN QUE CREA LA TABLA (security): 
# BD.crear_tabla_security()

# FUNCIÓN QUE AÑADE DATOS INCIALES A SECURITY:
# BD.añadir_datos_security(users, hashed_passwords, sexo, edad, correo, email_status)


# --- WEIGHT ---
# FUNCIÓN QUE CREA LA TABLA (weight): 
# BD.crear_tabla_weight()

# FUNCIÓN QUE AÑADE DATOS INCIALES A weight:
# BD.añdir_datos_weight_from_csv()

# --- STEPS ---
# FUNCIÓN QUE CREA LA TABLA (steps): 
# BD.crear_tabla_steps()

# FUNCIÓN QUE AÑADE DATOS INCIALES A steps:
# BD.añdir_datos_steps_from_csv()

users = ["Juan García", "María Rodríguez", "Alejandro Martínez", "Sofía López", "Carlos Fernández", "Ana Pérez", "Luis González", "Elena Ruiz", "Diego Sánchez", "Carmen Gómez"]

contraseña_txtplano = ["clave 123", "segura456", "contraseña789", "sofiapw", "carlitos123", "anapass", "luisgpw", "elena123", "diego456", "carmen789"]

sexo = ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F"]

edad = [28, 35, 42, 30, 25, 33, 37, 29, 31, 40]

correo = ["juan@gmail.com", "maria.r@email.com", "alejandro.m@gmail.com", "sofialopez@gmail.com", "carlos.f@gmail.com", "ana.p@gmail.com", "luisg@gmail.com", "elena.r@gmail.com", "diego.s@gmail.com", "carmen.g@gmail.com"]

email_status = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0]

hashed_passwords = []

for i in range(len(contraseña_txtplano)):
    hashed_passwords.append(BD.hasher(password=contraseña_txtplano[i]))


BD.borrar_tabla(tabla="steps")
BD.crear_tabla_steps()

BD.añadir_datos_steps_from_csv()