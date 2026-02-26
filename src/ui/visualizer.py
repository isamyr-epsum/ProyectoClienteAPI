import requests
from config import API_KEY, BASE_URL_CLIMA_ACTUAL, BASE_URL_PRONOSTICO, URL_AIRE

def obtener_clima_actual(ciudad):
    parametros = {'q': ciudad, 'appid': API_KEY, 'units': 'metric', 'lang': 'es'}
    try:
        respuesta = requests.get(BASE_URL_CLIMA_ACTUAL, params=parametros)
        datos = respuesta.json()
        if respuesta.status_code != 200:
            return {"error": f"No se pudo obtener el clima para '{ciudad}'.",
                    "estado": datos.get("message", "Error desconocido")}
    except:
        return {"error": "No se pudo conectar a la API."}

    descripcion = datos["weather"][0]["description"]
    presion = datos["main"]["pressure"]
    humedad = datos["main"]["humidity"]
    temperatura = datos["main"]["temp"]

    resultado = {
        "ubicacion": f"{datos['name']}, {datos['sys']['country']}",
        "clima": descripcion.capitalize(),
        "temperatura": round(temperatura,1),
        "humedad": humedad,
    }