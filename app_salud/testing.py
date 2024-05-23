import matplotlib.pyplot as plt
import numpy as np
import os

def grafico_imc_circular_con_punto(user, peso, altura):
    """
    Calcula el índice de masa corporal (IMC) dado el peso en kilogramos y la altura en metros, 
    y representa el resultado en un gráfico circular con un punto en el estado del usuario.
    
    Args:
        peso (float): El peso de la persona en kilogramos.
        altura (float): La altura de la persona en metros.
    """
    imc = peso / (altura ** 2)
    bajo_peso = 18.5
    normal = 24.9
    sobrepeso = 29.9
    
    # Datos de referencia del IMC a nivel mundial (simulados)
    porcentajes = [0.15, 0.55, 0.25, 0.05]  # Porcentajes de Bajo Peso, Normal, Sobrepeso, Obeso
    
    etiquetas = ['Bajo Peso', 'Normal', 'Sobrepeso', 'Obeso']
    
    # Creamos el gráfico circular
    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, _, _ = ax.pie(porcentajes, labels=etiquetas, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'orange', 'lightcoral'])
    plt.axis('equal')  # Aspecto igual asegura que el pastel se dibuje como un círculo
    plt.title('Distribución Global de IMC', fontsize=16, fontweight='bold')
    
    # Colocamos el peso y la altura del usuario más abajo y más a la derecha
    ax.text(0.98, 0.02, f'Peso: {peso} kg\nAltura: {altura} m', fontsize=10, ha='right', va='bottom', fontweight='bold', transform=ax.transAxes)
    
    # Colocamos un punto en el estado del usuario y una etiqueta 'TÚ' justo arriba y ligeramente separada
    angulo_estado_usuario = 90 - (imc - bajo_peso) * 90 / (sobrepeso - bajo_peso)
    x_punto = np.cos(np.deg2rad(angulo_estado_usuario))
    y_punto = np.sin(np.deg2rad(angulo_estado_usuario))
    ax.plot(x_punto, y_punto, marker='o', markersize=10, color='red')
    ax.text(x_punto, y_punto + 0.1, 'TÚ', fontsize=12, ha='center', va='bottom', fontweight='bold')
    plt.gcf().canvas.set_window_title('IMC')
    

    directorio_destino = 'app_salud/GRAFOS/grafos_images/imc'
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
    plt.savefig(f'{directorio_destino}/imc_{user}.png')  # Guardar la imagen en la ubicación especificada


# Ejemplo de uso
peso_usuario = 70  # en kilogramos
altura_usuario = 1.75  # en metros

grafico_imc_circular_con_punto(peso_usuario, altura_usuario)
