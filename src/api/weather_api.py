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
BASE_URL_CLIMA_ACTUAL = "https://api.openweathermap.org/data/2.5/weather",
BASE_URL_PRONOSTICO= "https://api.openweathermap.org/data/2.5/forecast"

def obtener_clima_actual(ciudad):
    params={
        'q': ciudad,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'es',
    }
    response = requests.get(BASE_URL_CLIMA_ACTUAL, params=params)
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
    params = {
        'q': ciudad,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'es'
    }

    response = requests.get(BASE_URL_PRONOSTICO, params=params)
    data = response.json()

    if response.status_code != 200 or "list" not in data:
        return {
            "error": f"No se pudo obtener el pronóstico para '{ciudad}'.",
            "status": data.get("message", "Respuesta inválida del servidor"),
            "codigo": data.get("cod", "sin código")
        }

    pronostico_por_dia = defaultdict(list)
    for entrada in data["list"]:
        fecha = entrada["dt_txt"].split(" ")[0]
        pronostico_por_dia[fecha].append(entrada)

    pronostico_resumido = []

    for fecha, entradas in list(pronostico_por_dia.items())[:5]:
        temps = [e["main"]["temp"] for e in entradas]
        humedades = [e["main"]["humidity"] for e in entradas]
        probabilidades_lluvia = [e.get("pop", 0) for e in entradas]
        descripciones = [e["weather"][0]["description"] for e in entradas]

        descripcion_principal = max(set(descripciones), key=descripciones.count)

        resumen_dia = {
            "fecha": fecha,
            "temperatura_min": round(min(temps), 1),
            "temperatura_max": round(max(temps), 1),
            "descripcion": descripcion_principal.capitalize(),
            "humedad_promedio": round(sum(humedades) / len(humedades), 1),
            "probabilidad_lluvia": round(sum(probabilidades_lluvia) / len(probabilidades_lluvia) * 100, 1)
        }
        pronostico_resumido.append(resumen_dia)

    resultado = {
        "ciudad": data["city"]["name"],
        "pais": data["city"]["country"],
        "pronostico_5_dias": pronostico_resumido,
        "última_actualización": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return resultado



def calidadAire(ciudad):
    pass


ciudad = input("Ingrese la ciudad: ")
pronostico =darPronosticos(ciudad)

print(json.dumps(pronostico, indent=4, ensure_ascii=False))

"""
ciudad = input("Ingrese la ciudad: ")
clima = obtener_clima_actual(ciudad)
print(json.dumps(clima, indent=4, ensure_ascii=False))
"""

