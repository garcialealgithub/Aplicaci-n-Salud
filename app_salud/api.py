import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
import requests
import ast


musculos = ["abdominales","abductores", "aductores", "biceps", "pantorrillas", "pecho", "antebrazos", "gluteos",
            "isquiotibiales", "dorsales", "espalda inferior", "media espalda", "cuello", "cuadriceps", "trapezoide", "triceps"]

muscles = {'abdominales': 'abdominals', 'abductores': 'abductors', 'aductores': 'adductors', 'biceps': 'biceps',
           'pantorrillas': 'calves', 'pecho': 'chest', 'antebrazos': 'forearms', 'gluteos': 'glutes', 'isquiotibiales': 'hamstrings',
           'dorsales': 'lats', 'espalda inferior': 'lower_back', 'media espalda': 'middle_back', 'cuello': 'neck',
           'cuadriceps': 'quadriceps', 'trapezoide': 'traps', 'triceps': 'triceps'}


def concrete_exercise(diccionarios, posicion):
    concreto = {}
    for i in range(len(diccionarios)):
        if i == posicion:
            concreto = diccionarios[i]
            return concreto

def InfoEjercicios(musc):
    musc = muscles[musc]
    headers={'X-Api-Key': 'g2xoHUNZk0IS0LxgIGipfA==qpzPJy4SCD1SV9gg'}
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(musc) # Si no está, salta al error
    response = requests.get(api_url, headers)
    if response.status_code == requests.codes.ok:
        respuesta = ast.literal_eval(response.text)
        return respuesta
    else:
        print("Error:", response.status_code, response.text)

def nombresEjercicios(respuesta):
    respuesta = respuesta
    nombres = []
    for i in range(len(respuesta)):
        nombres.append(respuesta[i]['name'])
    return nombres