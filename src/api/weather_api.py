"""
- realizar peticiones HTTP a la API
- gestionar autenticación
- manejo de errores de conexión
"""

#Añadir imports necesarios
import requests
import datetime
import json
from collections import defaultdict

API_KEY = "a24cf1baa02349b165a1f6206bf525bc"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def obtener_clima_actual(ciudad):
    params={
        'q': ciudad,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'es',
    }
    response = requests.get(BASE_URL, params=params)
    data=response.json()

    if response.status_code != 200:
        return {"error": f"No se pudo obtener el clima para '{ciudad}'.",
                "status": data.get("message", "Error desconocido")}

    descripcion = data["weather"][0]["description"]
    presion = data["main"]["pressure"]
    humedad = data["main"]["humidity"]
    temp = data["main"]["temp"]

    if "lluvia" in descripcion:
        mensaje_clima = " Lleva paraguas, está lloviendo."
    elif "nubes" in descripcion:
        mensaje_clima = "El cielo está nublado, pero tranquilo."
    elif "cielo claro" in descripcion:
        mensaje_clima = " Día despejado, aprovecha el sol."
    else:
        mensaje_clima = f"Clima actual: {descripcion}."

    if presion < 1000:
        mensaje_presion = "Presión baja: posible lluvia o tormenta."
    elif presion > 1020:
        mensaje_presion = "Presión alta: tiempo estable y despejado."
    else:
        mensaje_presion = "Presión normal."

    resultado = {
        "ubicación": f"{data['name']}, {data['sys']['country']}",
        "clima": f"{descripcion.capitalize()} ({mensaje_clima})",
        "temperatura": f"{temp}°C (sensación {data['main']['feels_like']}°C)",
        "humedad": f"{humedad}%",
        "presión": f"{presion} hPa ({mensaje_presion})",
        "viento": f"{data['wind']['speed']} m/s dirección {data['wind']['deg']}°",
        "amanecer": datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S"),
        "atardecer": datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S"),
        "última_actualización": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return resultado

def darPronosticos(ciudad):
    pass
def calidadAire(ciudad):
    pass

ciudad = input("Ingrese la ciudad: ")
clima = obtener_clima_actual(ciudad)
print(json.dumps(clima, indent=4, ensure_ascii=False))


