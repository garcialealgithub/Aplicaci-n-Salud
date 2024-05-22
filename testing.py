import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
import requests
import ast

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Botón con Imagen")

        self.musculos = ["abdominales","abductores", "aductores", "biceps", "pantorrillas", "pecho", "antebrazos", "gluteos",
                    "isquiotibiales", "dorsales", "espalda inferior", "media espalda", "cuello", "cuadriceps", "trapezoide", "triceps"]
        self.seleccion = ttk.Combobox(self.root, values=self.musculos, state='readonly')
        self.seleccion.pack()

        self.seleccion.bind('<<ComboboxSelected>>', self.InfoEjercicios)

        self.muscles = {'abdominales': 'abdominals', 'abductores': 'abductors', 'aductores': 'adductors', 'biceps': 'biceps',
           'pantorrillas': 'calves', 'pecho': 'chest', 'antebrazos': 'forearms', 'gluteos': 'glutes', 'isquiotibiales': 'hamstrings',
           'dorsales': 'lats', 'espalda inferior': 'lower_back', 'media espalda': 'middle_back', 'cuello': 'neck',
           'cuadriceps': 'quadriceps', 'trapezoide': 'traps', 'triceps': 'triceps'}

    
    def InfoEjercicios(self, event):
        musc = self.seleccion.get()
        elec = self.muscles[musc]
        headers={'X-Api-Key': 'g2xoHUNZk0IS0LxgIGipfA==qpzPJy4SCD1SV9gg'}
        api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(elec) # Si no está, salta al error
        response = requests.get(api_url, headers)
        if response.status_code == requests.codes.ok:
            respuesta = ast.literal_eval(response.text)
            print(type(respuesta))
            print(respuesta)
        else:
            print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()