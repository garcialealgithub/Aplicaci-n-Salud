import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import os

def grafico_peso(user, date, dias, color):
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('app_salud/SGBD/database.db')
    cursor = conn.cursor()
    
    # Consulta para obtener los datos de peso del usuario en el rango de fechas
    consulta = """
    SELECT date, weight
    FROM weight
    WHERE user = ?
    AND date BETWEEN date(?) AND date(?, '+' || ? || ' days')
    ORDER BY date;
    """
    cursor.execute(consulta, (user, date, date, dias-1))
    rows = cursor.fetchall()
    
    # Cerrar la conexión a la base de datos
    conn.close()
    
    # Verificar si se obtuvieron datos
    if not rows:
        raise ValueError(f"No se encontraron datos para el usuario: {user} en el rango de fechas especificado")
    
    # Convertir los datos en un DataFrame de pandas
    df = pd.DataFrame(rows, columns=['date', 'weight'])
    
    # Asegurarse de que la columna 'date' sea del tipo datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Formatear las fechas para mostrar solo día y mes
    df['date'] = df['date'].dt.strftime('%d-%b')
    
    # Crear el gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['weight'], marker='o', linestyle='-', color=color)
    plt.title(f"GRÁFICA PESO '{user.upper()}' | {date} por {dias} días")
    plt.xlabel('FECHA')
    plt.ylabel('PESO (kg)')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Verificar si el directorio de destino existe, si no, créalo
    directorio_destino = 'app_salud/GRAFOS/grafos_images/peso'
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.savefig(f'{directorio_destino}/peso_{user}_{date}.png')  # Guardar la imagen en la ubicación especificada


def grafico_pasos(user, date, dias, color):
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('app_salud/SGBD/database.db')
    cursor = conn.cursor()
    
    # Consulta para obtener los datos de pasos del usuario en el rango de fechas
    consulta = """
    SELECT date, steps
    FROM steps
    WHERE user = ?
    AND date BETWEEN date(?) AND date(?, '+' || ? || ' days')
    ORDER BY date;
    """
    cursor.execute(consulta, (user, date, date, dias-1))
    rows = cursor.fetchall()
    
    # Cerrar la conexión a la base de datos
    conn.close()
    
    # Verificar si se obtuvieron datos
    if not rows:
        raise ValueError(f"No se encontraron datos de pasos para el usuario: {user} en el rango de fechas especificado")
    
    # Convertir los datos en un DataFrame de pandas
    df = pd.DataFrame(rows, columns=['date', 'steps'])
    
    # Asegurarse de que la columna 'date' sea del tipo datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Formatear las fechas para mostrar solo día y mes
    df['date'] = df['date'].dt.strftime('%d-%b')
    
    # Crear el gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['steps'], marker='o', linestyle='-', color=color)
    plt.title(f"GRÁFICA PASOS '{user.upper()}' | {date} por {dias} días")
    plt.xlabel('FECHA')
    plt.ylabel('PASOS')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Verificar si el directorio de destino existe, si no, créalo
    directorio_destino = 'app_salud/GRAFOS/grafos_images/pasos'
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.savefig(f'{directorio_destino}/pasos_{user}_{date}.png')  # Guardar la imagen en la ubicación especificada
    

# Ejemplo de uso
grafico_peso('Ana Pérez', '2024-05-16', 3, color="darkblue")

grafico_pasos('Ana Pérez', '2024-05-16', 3, color="darkblue")