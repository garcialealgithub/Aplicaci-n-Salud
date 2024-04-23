from tkinter import *

root = Tk()
root.title("Inicio de sesión")
root.geometry("400x500")
root.resizable(0,0)
imagen = PhotoImage(file = "background.jpeg")

# Con Label y la opción image, puedes mostrar una imagen en el widget:
background = Label(image = imagen, text = "Imagen S.O de fondo")


background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
root.mainloop()