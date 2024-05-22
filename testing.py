import tkinter as tk
from tkinter import PhotoImage

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Botón con Imagen")

        # Cargar la imagen (asegúrate de que la imagen esté en el mismo directorio que tu script)
        self.imagen = PhotoImage(file="app_salud/images/configuration.png")

        # Crear el botón con la imagen
        self.boton_con_imagen = tk.Button(self.root, image=self.imagen, command=self.accion_boton)
        self.boton_con_imagen.place(x=50, y=50)

    def accion_boton(self):
        print("¡Botón con imagen presionado!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()