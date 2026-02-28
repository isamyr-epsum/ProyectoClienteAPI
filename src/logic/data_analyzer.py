"""" procesar datos JSON de la API,
- calcular estadísticas (temp. media, máxima, mínima)
- detectar patrones y tendencias
"""

"""
    toma los datos que devuelve la API (que vienen como strings con simbolos), 
    los convierte a números, y los clasifica en categorías como 'Frío', 'Templado', 'Calido'."
"""
def analizar_datos(datos_clima):
    """
    Analiza los datos meteorológicos recibidos de la API
    Parámetros: datos_clima (dict): Datos en formato JSON de la API
    Retorna: dict: Estadísticas procesadas
    """
    # Si hay error en los datos
    if "error" in datos_clima:
        return {"error": "No se pudieron analizar los datos"}

    # Extraer temperatura (quitar °C y convertir a número)
    try:
        temp_str = datos_clima["temperatura"].split("°C")[0]
        temperatura = float(temp_str)
    except:
        temperatura = None

    # Extraer humedad (quitar % y convertir a número)
    try:
        humedad = float(datos_clima["humedad"].replace("%", ""))
    except:
        humedad = None

    # Clasificar la temperatura
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

    # Clasificar humedad
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
        "ubicacion": datos_clima.get("ubicación", "Desconocida"),
        "temperatura": temperatura,
        "sensacion_termica": sensacion,
        "humedad": humedad,
        "nivel_humedad": nivel_humedad,
        "descripcion_clima": datos_clima.get("clima", ""),
        "presion": datos_clima.get("presión", ""),
        "viento": datos_clima.get("viento", "")
    }

    return analisis



"""
recorre todo el historial de consultas guardadas, extrae las temperaturas y humedades, 
y calcula la media, máxima y mínima. También cuenta qué ciudad se consultó más veces.
"""

def calcular_estadisticas(historial):
    """
    Calcula estadísticas de un historial de datos meteorológicos
    Parametros: historial (list): Lista de consultas anteriores
    Retorna:  dict: Estadísticas calculadas (temp media, máxima, mínima, etc.)
    """
    # Si el historial está vacío
    if not historial or len(historial) == 0:
        return {"error": "No hay datos en el historial"}

    # Recopilar todas las temperaturas del historial
    temperaturas = []
    humedades = []
    ciudades = []

    for consulta in historial:
        # Extraer datos de cada consulta
        datos = consulta.get("datos", {})

        # Extraer temperatura
        try:
            temp_str = datos["temperatura"].split("°C")[0]
            temp = float(temp_str)
            temperaturas.append(temp)
        except:
            pass

        # Extraer humedad
        try:
            hum = float(datos["humedad"].replace("%", ""))
            humedades.append(hum)
        except:
            pass

        # Guardar ciudad consultada
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

    # Crear diccionario con estadísticas
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