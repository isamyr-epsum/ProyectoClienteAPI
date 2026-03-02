def analizar_datos(datos_clima):

    if "error" in datos_clima:
        return {"error": "No se puede analizar los datos"}

    # como la temperatura viene en un formato necesito quitar °C y convertir a número.
    try:
        temp_str = datos_clima["Temperatura"].split("°C")[0]
        temperatura = float(temp_str) # convierto en numero decimal
    except:
        temperatura = None #si falla guardo NONE para manejarlo despues

    # con humedad lo mismo extraemos % y convertir a número)
    try:
        humedad = float(datos_clima["Humedad"].replace("%", ""))
    except:
        humedad = None

    if temperatura is not None:
        if temperatura < 10:
            sensacion = "Frío"
        elif temperatura < 20:
            sensacion = "Templado"
        elif temperatura < 30:
            sensacion = "Cálido"
        else:
            sensacion = "Caluroso"
    else:
        sensacion = "Desconocido"

    if humedad is not None:
        if humedad < 30:
            nivel_humedad = "Seco"
        elif humedad < 60:
            nivel_humedad = "Normal"
        else:
            nivel_humedad = "Húmedo"
    else:
        nivel_humedad = "Desconocido"

    analisis = {
        "ubicacion": datos_clima.get("Ubicación", "Desconocida"),
        "temperatura": temperatura,
        "sensacion_termica": sensacion,
        "humedad": humedad,
        "nivel_humedad": nivel_humedad,
        "descripcion_clima": datos_clima.get("Clima", ""),
        "presion": datos_clima.get("Presión", ""),
        "viento": datos_clima.get("Viento", "")
    }

    return analisis

def calcular_estadisticas(historial):

    if not historial or len(historial) == 0:
        return {"error": "No hay datos en el historial"}

    temperaturas = []
    humedades = []
    ciudades = []

    for consulta in historial:
        datos = consulta.get("datos", {})

        try:
            temp_str = datos["temperatura"]
            temp = float(temp_str)
            temperaturas.append(temp)
        except:
            pass

        try:
            hum = datos["humedad"]
            humedades.append(hum)
        except:
            pass

        ciudad = consulta.get("ciudad", "")
        if ciudad:
            ciudades.append(ciudad)

    if len(temperaturas) > 0:
        #promedio: sumo todas y divido
        temp_media = round(sum(temperaturas) / len(temperaturas), 1)
        temp_max = max(temperaturas)
        temp_min = min(temperaturas)
    else:
        temp_media = None
        temp_max = None
        temp_min = None

    if len(humedades) > 0:
        humedad_media = round(sum(humedades) / len(humedades), 1)
    else:
        humedad_media = None

    ciudades_unicas = list(set(ciudades))

    estadisticas = {
        "total_consultas": len(historial),
        "temperatura_media": temp_media,
        "temperatura_maxima": temp_max,
        "temperatura_minima": temp_min,
        "humedad_media": humedad_media,
        "ciudades_consultadas": ciudades_unicas,
        "ciudad_mas_consultada": max(set(ciudades), key=ciudades.count) if ciudades else None
    }

    return estadisticas