import requests
import datetime
import json
from collections import defaultdict
from config import API_KEY , BASE_URL_CLIMA_ACTUAL, BASE_URL_PRONOSTICO ,URL_AIRE
from src.ui.exporter import exportar_csv, exportar_json, exportar_pdf
from src.ui.visualizer import obtener_clima_actual_grafico, graficar_pronostico


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
        "Ubicación": f"{data['name']}, {data['sys']['country']}",
        "Clima": f"{descripcion.capitalize()} ({mensaje_clima})",
        "Temperatura": f"{temp}°C (sensación {data['main']['feels_like']}°C)",
        "Humedad": f"{humedad}%",
        "Presión": f"{presion} hPa ({mensaje_presion})",
        "Viento": f"{data['wind']['speed']} m/s dirección {data['wind']['deg']}°",
        "Amanecer": datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S"),
        "Atardecer": datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S"),
        "Última actualización": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
            "Fecha": fecha,
            "Temperatura mín": round(min(temps), 1),
            "Temperatura máx": round(max(temps), 1),
            "Descripción": descripcion_principal.capitalize(),
            "Promedio Humedad": round(sum(humedades) / len(humedades), 1),
            "Probabilidad de lluvia": round(sum(probabilidades_lluvia) / len(probabilidades_lluvia) * 100, 1)
        }
        pronostico_resumido.append(resumen_dia)

    resultado = {
        "Ciudad": data["city"]["name"],
        "País": data["city"]["country"],
        "Pronóstico 5 dias": pronostico_resumido,
        "Última actualización": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return pronostico_resumido


def calidadAire(ciudad):
    params_clima = {
        'q': ciudad,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'es'
    }

    resp_clima = requests.get(BASE_URL_CLIMA_ACTUAL, params=params_clima)
    data_clima = resp_clima.json()

    if resp_clima.status_code != 200 or "coord" not in data_clima:
        return {
            "error": f"No se pudo obtener las coordenadas de '{ciudad}'.",
            "status": data_clima.get("message", "Error desconocido")
        }

    lat = data_clima["coord"]["lat"]
    lon = data_clima["coord"]["lon"]

    params_aire = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY
    }

    resp_aire = requests.get(URL_AIRE, params=params_aire)
    data_aire = resp_aire.json()

    if resp_aire.status_code != 200 or "list" not in data_aire:
        return {
            "error": f"No se pudo obtener la calidad del aire en '{ciudad}'.",
            "status": data_aire.get("message", "Error desconocido")
        }

    indice = data_aire["list"][0]["main"]["aqi"]
    componentes = data_aire["list"][0]["components"]

    descripcion = {
        1: "Muy buena",
        2: "Buena",
        3: "Moderada",
        4: "Mala",
        5: "Muy mala"
    }

    mensaje = {
        1: "Excelente día para salir o hacer deporte al aire libre.",
        2: "Buena calidad del aire. Perfecto para pasear.",
        3: "Calidad del aire moderada. Si eres sensible, evita ejercicio intenso afuera.",
        4: "El aire no es saludable. Evita estar mucho tiempo al aire libre.",
        5: "Muy mala calidad del aire. Recomendable quedarse en el hogar."
    }

    resultado = {
        "Ciudad": data_clima["name"],
        "País": data_clima["sys"]["country"],
        "Coordenadas": {"lat": lat, "lon": lon},
        "Calidad de aire": {
            "Índice": indice,
            "Descripción": descripcion[indice],
            "Pronóstico": mensaje[indice],
            "Componentes": {
                "CO (monóxido de carbono)": componentes["co"],
                "NO₂ (dióxido de nitrógeno)": componentes["no2"],
                "O₃ (ozono)": componentes["o3"],
                "PM₂.₅ (partículas finas)": componentes["pm2_5"],
                "PM₁₀ (partículas gruesas)": componentes["pm10"]
            }
        },
        "Última actualización": datetime.datetime.now().strftime("%Y-%m-%d / %H:%M:%S")
    }

    return resultado

continuar= True
while continuar:
    print("-------------------MENÚ-------------------")
    ciudad = input("Ingrese la ciudad la cual desea consultar: ")
    decision = int(
        input("¿Qué desea ver? \n 1 --> Clima actual \n 2 --> Pronóstico \n 3 --> Calidad de aire \n 4 --> Salir  \n Por favor, introduzca su consulta: "))
    if decision == 1:
        print("Prueba")
        obtener_clima_actual_grafico(ciudad)
        print("Funciona")
        # print(json.dumps(clima, indent=4, ensure_ascii=False))
        """exportar_csv(clima, "clima")
        exportar_json(clima, "clima")
        exportar_pdf(clima, "clima")"""
    if decision == 2:
        pronostico = darPronosticos(ciudad)
        graficar_pronostico(pronostico, ciudad)
        print(json.dumps(pronostico, indent=4, ensure_ascii=False))
    if decision == 3:
        calidad = calidadAire(ciudad)
        print(json.dumps(calidad, indent=4, ensure_ascii=False))
    if decision == 4:
        print("¡Hasta pronto!")
        continuar= False



