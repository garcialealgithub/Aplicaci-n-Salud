from tkinter import *
import app_salud.SGBD.verifications as v
from tkinter import messagebox
import app_salud.mainWindow as mW
import app_salud.change_password as cp

import tkinter as tk
from tkinter import Frame, Label, Button, CENTER, Toplevel, messagebox

class grapConfig(cp.UserActions):
    def __init__(self, user, password, color, root, title):
        super().__init__(user, password, color, root, "Color configuration")
        
        self.selected_color = None  # Variable para almacenar el color seleccionado
        
        self.frame = Frame(self.root, width=300, height=400)
        self.frame.place(x=0, y=0)
        
        self.verifytext = Label(self.frame, text="Choose color", font=("Arial", 16))
        self.verifytext.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        # Diccionario para convertir nombres de colores a valores RGB
        self.color_dict = {
            'Red': (255, 0, 0),
            'Green': (0, 255, 0),
            'Blue': (0, 0, 255),
            'Yellow': (255, 255, 0),
            'Orange': (255, 165, 0)
        }

        # Añadir botones para cada color
        for idx, (color_name, color_value) in enumerate(self.color_dict.items()):
            btn = Button(self.frame, text=color_name, font=("Arial", 14), bg=self.rgb_to_hex(color_value), command=lambda c=color_value: self.choose_color(c))
            btn.place(relx=0.5, rely=0.4 + idx * 0.1, anchor=CENTER)
        
        backtoMain = Button(self.frame, text="Back", font=("Arial", 14), command=self.backtomain)
        backtoMain.place(relx=0.5, rely=0.9, anchor=CENTER)
    
    def rgb_to_hex(self, rgb):
        return '#{:02x}{:02x}{:02x}'.format(*rgb)
    
    def choose_color(self, color):
        self.color = self.rgb_to_hex(color)
        messagebox.showinfo("Color seleccionado", f"Selected color: {self.color}")
        self.backtomain()
    
    def backtomain(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        mW.MainWindow(self.user, self.password, self.color, new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)