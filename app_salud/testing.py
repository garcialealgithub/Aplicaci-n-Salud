import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

def grafico_entrenamiento(user, date, dias):
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('app_salud/SGBD/database.db')
    cursor = conn.cursor()
    
    # Consulta para obtener los datos de entrenamiento del usuario en el rango de fechas
    consulta = """
    SELECT date, mean_cardiac_frequency, duration, calories
    FROM training
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
        raise ValueError(f"No se encontraron datos de entrenamiento para el usuario: {user} en el rango de fechas especificado")
    
    # Convertir los datos en un DataFrame de pandas
    df = pd.DataFrame(rows, columns=['date', 'mean_cardiac_frequency', 'duration', 'calories'])
    
    # Crear la figura y los subgráficos
    fig, axs = plt.subplots(3, 1, figsize=(10, 15), sharex=True)
    
    # Graficar la frecuencia cardiaca en el primer subgráfico (color rojo)
    axs[0].plot(df['date'], df['mean_cardiac_frequency'], marker='o', linestyle='-', color='red')
    axs[0].set_ylabel('FRECUENCIA CARDIACA')
    axs[0].grid(True)
    
    # Graficar la duración en el segundo subgráfico (color negro)
    axs[1].plot(df['date'], df['duration'], marker='o', linestyle='-', color='black')
    axs[1].set_ylabel('DURACIÓN')
    axs[1].grid(True)
    
    # Graficar las calorías en el tercer subgráfico (color naranja fuerte)
    axs[2].plot(df['date'], df['calories'], marker='o', linestyle='-', color='orange')
    axs[2].set_ylabel('CALORÍAS')
    axs[2].grid(True)
    
    # Añadir título
    plt.suptitle(f"GRÁFICA ENTRENAMIENTO '{user.upper()}' | {date} por {dias} días", y=0.95)
    
    # Ajustar diseño y guardar la imagen
    plt.tight_layout()
    directorio_destino = 'app_salud/GRAFOS/grafos_images/entreno'
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
    plt.savefig(f'{directorio_destino}/entreno_{user}_{date}.png')  # Guardar la imagen en la ubicación especificada
    


