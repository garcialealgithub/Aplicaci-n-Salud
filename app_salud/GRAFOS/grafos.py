import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import messagebox
import os

tipografo = ['Peso', 'Pasos', 'F. Cardíaca', 'Sueño', 'Entrenamiento']

def devolver_diasDisponibles(tipo):
    return diasDisponibles[tipo]


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
        messagebox.showerror("Error", f"No se encontraron datos de peso para el usuario: {user} en el rango de fechas especificado")
    
    # Convertir los datos en un DataFrame de pandas
    df = pd.DataFrame(rows, columns=['date', 'weight'])
    
    # Asegurarse de que la columna 'date' sea del tipo datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Formatear las fechas para mostrar solo día y mes
    df['date'] = df['date'].dt.strftime('%d-%b')
    
    # Crear el gráfico
    plt.figure(figsize=(5, 4))  # Tamaño de la figura en pulgadas
    plt.plot(df['date'], df['weight'], marker='o', linestyle='-', color=color)
    plt.title(f"GRÁFICA PESO '{user.upper()}' | {date} por {dias} días")
    plt.xlabel('FECHA')
    plt.ylabel('PESO (kg)')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Guardar la imagen en el mismo directorio que el script
    plt.tight_layout()
    plt.savefig('app_salud/GRAFOS/images/grafico_peso.png', dpi=100)  # Guardar la imagen en el directorio actual

  
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
        messagebox.showerror("Error", f"No se encontraron datos de pasos para el usuario: {user} en el rango de fechas especificado")
    
    # Convertir los datos en un DataFrame de pandas
    df = pd.DataFrame(rows, columns=['date', 'steps'])
    
    # Asegurarse de que la columna 'date' sea del tipo datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Formatear las fechas para mostrar solo día y mes
    df['date'] = df['date'].dt.strftime('%d-%b')
    
    # Crear el gráfico
    plt.figure(figsize=(5, 4))
    plt.plot(df['date'], df['steps'], marker='o', linestyle='-', color=color)
    plt.title(f"GRÁFICA PASOS '{user.upper()}' | {date} por {dias} días")
    plt.xlabel('FECHA')
    plt.ylabel('PASOS')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Mostrar el gráfico
    plt.tight_layout()
    



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
    plt.figure(figsize=(5, 4))
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
    plt.savefig(f'{directorio_destino}/pasos_grafico.png')  # Guardar la imagen en la ubicación especificada
    

def grafico_freq_card(user, date, dias, color):
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('app_salud/SGBD/database.db')
    cursor = conn.cursor()

    # Consulta para obtener los datos de frecuencia cardíaca del usuario en el rango de fechas
    consulta = """
    SELECT date, time, cardiac_frequency
    FROM cardiac_frequency
    WHERE user = ?
    AND date BETWEEN date(?) AND date(?, '+' || ? || ' days')
    ORDER BY date, time;
    """
    cursor.execute(consulta, (user, date, date, dias-1))
    rows = cursor.fetchall()
    
    # Cerrar la conexión a la base de datos
    conn.close()
    
    # Verificar si se obtuvieron datos
    if not rows:
        raise ValueError(f"No se encontraron datos de frecuencia cardíaca para el usuario: {user} en el rango de fechas especificado")
    
    # Convertir los datos en un DataFrame de pandas
    df = pd.DataFrame(rows, columns=['date', 'hora', 'cardiac_frequency'])
    
    # Asegurarse de que las columnas 'date' y 'hora' sean del tipo datetime
    df['date'] = pd.to_datetime(df['date'])
    df['hora'] = pd.to_datetime(df['hora'], errors='coerce').dt.time  # Convertir a formato hh:mm:ss, permitiendo valores incorrectos
    
    # Eliminar filas con valores de hora incorrectos
    df = df.dropna(subset=['hora'])
    
    # Crear una columna 'hora' como tipo timedelta para facilitar el gráfico
    df['hora'] = pd.to_timedelta(df['hora'].astype(str))
    
    # Sumar 'date' y 'hora' para obtener el datetime completo
    df['datetime'] = df['date'] + df['hora']
    
    # Formatear las fechas para mostrar solo día y mes
    df['date'] = df['date'].dt.strftime('%d-%b')
    
    # Crear el gráfico
    plt.figure(figsize=(5, 4))
    plt.plot(df['datetime'], df['cardiac_frequency'], marker='o', linestyle='-', color=color)
    plt.title(f"GRÁFICA FRECUENCIA CARDÍACA '{user.upper()}' | {date} por {dias} días")
    plt.xlabel('FECHA Y HORA')
    plt.ylabel('FRECUENCIA CARDÍACA')
    plt.grid(True)
    plt.xticks(df['datetime'], df['datetime'].dt.strftime('%d-%b %H:%M'))  # Mostrar fecha y hora en el eje x
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mejor visualización
    

    # Verificar si el directorio de destino existe, si no, créalo
    directorio_destino = 'app_salud/GRAFOS/grafos_images/freq_card'
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.savefig(f'{directorio_destino}/freq_card_grafico.png')  # Guardar la imagen en la ubicación especificada
    

def grafico_sueño(user, date, dias):
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('app_salud/SGBD/database.db')
    cursor = conn.cursor()
    
    # Consulta para obtener los datos de sueño del usuario en el rango de fechas
    consulta = """
    SELECT date, quality, duration, duration_deep_sleep, interruptions_counter
    FROM sleep
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
        raise ValueError(f"No se encontraron datos de sueño para el usuario: {user} en el rango de fechas especificado")
    
    # Convertir los datos en un DataFrame de pandas
    df = pd.DataFrame(rows, columns=['date', 'quality', 'duration', 'duration_deep_sleep', 'interruptions_counter'])
    
    # Crear la figura y los subgráficos
    fig, axs = plt.subplots(3, 1, figsize=(5, 4), sharex=True)
    
    # Graficar la frecuencia cardiaca en el primer subgráfico
    axs[0].plot(df['date'], df['quality'], marker='o', linestyle='-', color='red')
    axs[0].set_ylabel('FRECUENCIA CARDIACA')
    axs[0].grid(True)
    
    # Graficar el sueño total en el segundo subgráfico
    axs[1].plot(df['date'], df['duration'], marker='o', linestyle='-', color='blue')
    axs[1].set_ylabel('SUEÑO')
    axs[1].grid(True)
    
    # Graficar el sueño profundo en el tercer subgráfico
    axs[2].plot(df['date'], df['duration_deep_sleep'], marker='o', linestyle='-', color='navy')
    axs[2].set_ylabel('SUEÑO PROFUNDO')
    axs[2].grid(True)
    
    # Añadir título
    plt.suptitle(f"GRÁFICA SUEÑO '{user.upper()}' | {date} por {dias} días", y=0.95)


    # Ajustar diseño y guardar la imagen
    plt.tight_layout()
    directorio_destino = 'app_salud/GRAFOS/grafos_images/sueño'
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
    plt.savefig(f'{directorio_destino}/sueño_grafico.png')  # Guardar la imagen en la ubicación especificada


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
    fig, axs = plt.subplots(3, 1, figsize=(5, 4), sharex=True)
    
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
    plt.savefig(f'{directorio_destino}/entreno_grafico.png')  # Guardar la imagen en la ubicación especificada


def grafico_imc(user, peso, altura):
   
    imc = peso / (altura ** 2)
    bajo_peso = 18.5
    normal = 24.9
    sobrepeso = 29.9
    
    # Datos de referencia del IMC a nivel mundial (simulados)
    porcentajes = [0.15, 0.55, 0.25, 0.05]  # Porcentajes de Bajo Peso, Normal, Sobrepeso, Obeso
    
    etiquetas = ['Bajo Peso', 'Normal', 'Sobrepeso', 'Obeso']
    
    # Creamos el gráfico circular
    fig, ax = plt.subplots(figsize=(5, 4))
    wedges, _, _ = ax.pie(porcentajes, labels=etiquetas, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'orange', 'lightcoral'])
    plt.axis('equal')  # Aspecto igual asegura que el pastel se dibuje como un círculo
    plt.title('DISTRIBUCIÓN GLOBAL de IMC', fontsize=16, fontweight='bold')
    
    # Colocamos el peso y la altura del usuario más abajo y más a la derecha
    ax.text(0.98, 0.02, f'Peso: {peso} kg\nAltura: {altura} m', fontsize=10, ha='right', va='bottom', fontweight='bold', transform=ax.transAxes)
    
    # Colocamos un punto en el estado del usuario y una etiqueta 'TÚ' justo arriba y ligeramente separada
    angulo_estado_usuario = 90 - (imc - bajo_peso) * 90 / (sobrepeso - bajo_peso)
    x_punto = np.cos(np.deg2rad(angulo_estado_usuario))
    y_punto = np.sin(np.deg2rad(angulo_estado_usuario))
    ax.plot(x_punto, y_punto, marker='o', markersize=10, color='red')
    ax.text(x_punto, y_punto + 0.1, 'TÚ', fontsize=12, ha='center', va='bottom', fontweight='bold')
    

    directorio_destino = 'app_salud/GRAFOS/grafos_images/imc'
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
    plt.savefig(f'{directorio_destino}/imc_grafico.png')  # Guardar la imagen en la ubicación especificada