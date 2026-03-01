import requests
from config import API_KEY, BASE_URL_CLIMA_ACTUAL, BASE_URL_PRONOSTICO
import datetime
from collections import defaultdict
import matplotlib.pyplot as plt


def obtener_clima_actual_grafico(ciudad):
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
        "Ubicación": f"{datos['name']}, {datos['sys']['country']}",
        "Clima": descripcion.capitalize(),
        "Temperatura": round(temperatura, 1),
        "Humedad": humedad,
        "Presión": presion,
        "Última actualización": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    graficar_clima_actual(resultado["Temperatura"], ciudad)
    return resultado

def pronostico_5_dias(ciudad):
    parametros = {
        'q': ciudad,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'es'
    }
    try:
        respuesta = requests.get(BASE_URL_PRONOSTICO, params=parametros)
        datos = respuesta.json()
        if respuesta.status_code != 200 or "list" not in datos:
            return {"error": f"No se pudo obtener el pronóstico de '{ciudad}'."}
    except requests.RequestException:
        return {"error": "No se pudo conectar a la API."}

    pronostico_por_dia = defaultdict(list)
    for entrada in datos["list"]:
        fecha = entrada["dt_txt"].split(" ")[0]
        pronostico_por_dia[fecha].append(entrada)

    resumen_pronostico = []

    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    hoy = datetime.date.today()

    for i, (fecha, entradas) in enumerate(list(pronostico_por_dia.items())[:5]):

        dia_nombre = dias_semana[(hoy.weekday() + i) % 7]

        temperaturas = []
        humedades = []
        lluvias = []
        descripciones = []

        for e in entradas:
            temperaturas.append(e["main"]["temp"])
            humedades.append(e["main"]["humidity"])
            lluvias.append(e.get("pop", 0))
            descripciones.append(e["weather"][0]["description"])

        temp_min = round(min(temperaturas), 1)
        temp_max = round(max(temperaturas), 1)
        humedad_media = round(sum(humedades)/len(humedades), 1)
        prob_lluvia = round(sum(lluvias)/len(lluvias)*100, 1)
        descripcion_principal = max(set(descripciones), key=descripciones.count)

        resumen_pronostico.append({
            "dia": dia_nombre,
            "temperatura_min": temp_min,
            "temperatura_max": temp_max,
            "humedad_promedio": humedad_media,
            "probabilidad_lluvia": prob_lluvia,
            "descripcion": descripcion_principal.capitalize()
        })
    return resumen_pronostico

def graficar_clima_actual(temperatura, ciudad):

    plt.figure(figsize=(4, 6))
    plt.bar([ciudad], [temperatura], color='orange')
    plt.title("Temperatura actual")
    plt.ylabel("°C")
    plt.ylim(0, max(50, temperatura + 10))
    plt.show()

def graficar_pronostico(pronostico, ciudad):
    print(pronostico)

    dias = []
    temp_max = []
    temp_min = []
    humedad = []
    lluvia = []

    for p in pronostico:
        dias.append(p["Fecha"])
        temp_max.append(p["Temperatura máx"])
        temp_min.append(p["Temperatura mín"])
        humedad.append(p["Promedio Humedad"])
        lluvia.append(p["Probabilidad de lluvia"])

    plt.figure(figsize=(10, 6))
    plt.plot(dias, temp_max, marker='o', color='red', label='Temp máx (°C)')
    plt.plot(dias, temp_min, marker='o', color='blue', label='Temp mín (°C)')
    plt.plot(dias, humedad, marker='s', color='green', label='Humedad (%)')
    plt.plot(dias, lluvia, marker='^', color='purple', label='Probabilidad lluvia (%)')

    plt.title(f"Pronóstico de {ciudad} en los próximos 5 días")
    plt.ylabel("Valores")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
