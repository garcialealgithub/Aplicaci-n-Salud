from tkinter import *
import app_salud.SGBD.verifications as v
from tkinter import messagebox
import app_salud.mainWindow as mW
import app_salud.change_password as cp

import tkinter as tk
from tkinter import Frame, Label, Button, CENTER, Toplevel, messagebox

class grapConfig(cp.UserActions):
    def __init__(self, user, password, color, root, title):
        super().__init__(user, password, color, root, "Configuración de color")
        
        self.selected_color = None  # Variable para almacenar el color seleccionado
        
        self.frame = Frame(self.root, width=300, height=400)
        self.frame.place(x=0, y=0)
        
        self.verifytext = Label(self.frame, text="Elige color", font=("Arial", 16))
        self.verifytext.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        # Añadir botones para cada color
        colors = ['Rojo', 'Verde', 'Azul', 'Amarillo', 'Naranja']
        for idx, color in enumerate(colors):
            btn = Button(self.frame, text=color, font=("Arial", 14), command=lambda c=color: self.choose_color(c))
            btn.place(relx=0.5, rely=0.4 + idx * 0.1, anchor=CENTER)
        
        backtoMain = Button(self.frame, text="Volver", font=("Arial", 14), command=self.backtomain)
        backtoMain.place(relx=0.5, rely=0.9, anchor=CENTER)
    
    def choose_color(self, color):
        self.color = color
        messagebox.showinfo("Color seleccionado", f"Has seleccionado el color: {color}")
        self.backtomain()
    
    def backtomain(self):
        
        self.root.withdraw()
        new_root = Toplevel(self.root)
        mW.MainWindow(self.user, self.password, self.color, new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
        

