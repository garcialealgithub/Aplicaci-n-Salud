import app_salud.api as api
import requests


respuesta = api.InfoEjercicios('abdominales', None)
print(respuesta)