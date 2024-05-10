# SISTEMA DE GESTIÓN DE BASE DE DATOS

import sqlite3

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect('usuarios.db')

# Crear un cursor
cursor = conn.cursor()

def crear_tabla(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        user TEXT NOT NULL,
                        password INTEGER)''')
    
    # Guardar los cambios
    conn.commit()

def insertar_datos(cursor):
    # Insertar datos
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Juan', 30))
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('María', 25))

    

# Consulta
cursor.execute("SELECT * FROM usuarios")
print("Todos los usuarios:")
for row in cursor.fetchall():
    print(row)

# Actualizar datos
cursor.execute("UPDATE usuarios SET edad = ? WHERE nombre = ?", (35, 'Juan'))
conn.commit()

# Consulta después de la actualización
cursor.execute("SELECT * FROM usuarios")
print("\nTodos los usuarios después de la actualización:")
for row in cursor.fetchall():
    print(row)

# Eliminar datos
cursor.execute("DELETE FROM usuarios WHERE nombre = ?", ('María',))
conn.commit()

# Consulta después de la eliminación
cursor.execute("SELECT * FROM usuarios")
print("\nTodos los usuarios después de la eliminación:")
for row in cursor.fetchall():
    print(row)


def cerrar_conexión():
    # Cerrar la conexión
    conn.close()
