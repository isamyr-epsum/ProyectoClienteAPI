""""
    Autor: Lucas
    Comentarios para segun Sprint:

    Data analyzer.py procesa los datos que vienen de la API y los converte en informacion Util.
    Calcula estadisticas del historial de consultas
"""
def analizar_datos(datos_clima):
    """

    """
    # verificar primero si hay error en los datos
    if "error" in datos_clima:
        return {"error": "No se puede analizar los datos"}

    # como la temperatura viene en un formato necesito quitar °C y convertir a número.
    try:
        temp_str = datos_clima["temperatura"].split("°C")[0]
        temperatura = float(temp_str) # convierto en numero decimal
    except:
        temperatura = None #si falla guardo NONE para manejarlo despues

    # HUMEDAD: Lo mismo extraemos % y convertir a número)
    try:
        humedad = float(datos_clima["humedad"].replace("%", ""))
    except:
        humedad = None

    # clasificar la temperatura para que sea mas facil de leer
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

    # Clasificar la humedad
    if humedad is not None:
        if humedad < 30:
            nivel_humedad = "Seco"
        elif humedad < 60:
            nivel_humedad = "Normal"
        else:
            nivel_humedad = "Húmedo"
    else:
        nivel_humedad = "Desconocido"

    # Creamos un diccionario con todos los datos del analisis procesado
    # Esto es lo que despues se mostrara al usario o se exportará
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
Analiza todas las consutas guardadas y sacamos ESTADISTICAS GENERALES
RECIBE: list contodas las consultas anteriores y retorna un diccionario: Temperaturas medias/ media, humedad media etc

"""

def calcular_estadisticas(historial):

    # si no hay datos guardados no puedo calcular nada
    if not historial or len(historial) == 0:
        return {"error": "No hay datos en el historial"}

    # voy guardando cada consulta que hay guardada en : temperaturas, humedades y ciudades
    # de todas las consultas en listas separadas
    temperaturas = []
    humedades = []
    ciudades = []

    #reccorer cada consulta que hay guardada
    for consulta in historial:
        # cada consulta tiene un diccionario de datos con la info del climpa
        datos = consulta.get("datos", {})

        #intentar extraer la temperatura
        try:
            temp_str = datos["Temperatura"].split("°C")[0]
            temp = float(temp_str)
            temperaturas.append(temp) #añado a lista
        except:
            pass # si falla ignoro y sigo con la seguiente

        #Humedad: lo mismo
        try:
            hum = float(datos["Humedad"].replace("%", ""))
            humedades.append(hum)
        except:
            pass

        #Guardo que ciudad se consultó
        ciudad = consulta.get("ciudad", "")
        if ciudad:
            ciudades.append(ciudad)

    #  Calcular las estadisticas con todas las temperaturas recopiladas
    if len(temperaturas) > 0:
        #promedio: sumo todas y divido
        temp_media = round(sum(temperaturas) / len(temperaturas), 1)
        temp_max = max(temperaturas)
        temp_min = min(temperaturas)
    else:
        # Si no hay temperaturas, pongo None
        temp_media = None
        temp_max = None
        temp_min = None
    # Calcular humedad promedio
    if len(humedades) > 0:
        humedad_media = round(sum(humedades) / len(humedades), 1)
    else:
        humedad_media = None

    # Saco lista de ciudades únicas (SIN REPETIR)
    ciudades_unicas = list(set(ciudades))

    # Diccionario final con todas las estadísticas
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