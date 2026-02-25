"""
- realizar peticiones HTTP a la API
- gestionar autenticación
- manejo de errores de conexión
"""
import requests
from config import API_KEY, API_BASE_URL


#Añadir imports necesarios

# Esta funcion tiene como proposito obtener el clima actual de una ciudad, return-> dict: datos en formato JSON
def obtener_clima_actual(ciudad):

    params = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }

    respuesta = requests.get(API_BASE_URL, params=params)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        temperatura = datos["main"]["temp"]
        descripcion = datos["weather"][0]["description"]
        humedad = datos["main"]["humidity"]

        print(f"Clima en {ciudad}")
        print(f"Temperatura: {temperatura}")
        print(f"Descripcion: {descripcion}")
        print(f"Humedad: {humedad}")

    else:
        print("Error:", respuesta.status_code)
        print(respuesta.text)

    # TODO: Implementar en Sprint 2
    print(f"Consultando clima de: {ciudad}")