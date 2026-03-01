def analizar_datos(datos_clima):
    # Si hay error en los datos
    if "error" in datos_clima:
        return {"error": "No se pudieron analizar los datos"}

    try:
        temp_str = datos_clima["Temperatura"].split("°C")[0]
        temperatura = float(temp_str)
    except:
        temperatura = None

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

    # Crear el diccionario con el análisis
    analisis = {
        "Ubicacion": datos_clima.get("Ubicación", "Desconocida"),
        "Temperatura": temperatura,
        "Sensacion termica": sensacion,
        "Humedad": humedad,
        "Nivel de humedad": nivel_humedad,
        "Descripcion clima": datos_clima.get("clima", ""),
        "Presion": datos_clima.get("Presión", ""),
        "Viento": datos_clima.get("Viento", "")
    }

    return analisis

def calcular_estadisticas(historial):

    if not historial or len(historial) == 0:
        return {"error": "No hay datos en el historial"}

    # Recopilar todas las temperaturas del historial
    temperaturas = []
    humedades = []
    ciudades = []

    for consulta in historial:

        # Extraer datos de cada consulta
        datos = consulta.get("datos", {})

        try:
            temp_str = datos["temperatura"].split("°C")[0]
            temp = float(temp_str)
            temperaturas.append(temp)
        except:
            pass

        try:
            hum = float(datos["humedad"].replace("%", ""))
            humedades.append(hum)
        except:
            pass

        ciudad = consulta.get("ciudad", "")
        if ciudad:
            ciudades.append(ciudad)

    # Calcular estadísticas
    if len(temperaturas) > 0:
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

    # Contar cuántas veces se consultó cada ciudad
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