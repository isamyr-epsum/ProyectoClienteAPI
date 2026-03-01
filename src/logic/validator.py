"""
- validar formato de nombres de ciudades
- verificar integridad de datos recibidos de la API
- comprobar rangos válidos (temperaturas, humedad, etc.)

"""
""" La funcion validar ciudad comprueba que el nombre de ciudad sea válido
    recibe parámetros: ciudad (str): Nombre de la ciudad a validary retorna: tupla: (es_valido, mensaje)
   """
def validar_ciudad(ciudad):
    # Verificar que no esté vacía
    if not ciudad or ciudad.strip() == "":
        return False, "El nombre de la ciudad está vacío"

    # Limpiar espacios
    ciudad = ciudad.strip()

    # Debe tener al menos 2 caracteres
    if len(ciudad) < 2:
        return False, "El nombre es demasiado corto"

    # No más de 50 caracteres (límite razonable)
    if len(ciudad) > 50:
        return False, "El nombre es demasiado largo"

    # No puede ser solo números
    if ciudad.isdigit():
        return False, "El nombre no puede ser solo números"

    return True, "Ciudad válida"


def validar_temperatura(temp_str):
    """
    Validar extrae y valida la temperatura de un string, recibe parámetros:
        temp_str (str): String con temperatura (ej: "15.5°C")
        retorna: tupla: (es_valido, temperatura_float)
    """
    try:
        # Quitar el símbolo de grados y extraer número
        temp = float(temp_str.split("°C")[0])

        # Verificar rango razonable (-60°C a 60°C)
        if temp < -60 or temp > 60:
            return False, None

        return True, temp

    except (ValueError, IndexError):
        return False, None


def validar_humedad(humedad_str):
    """
    Extrae y valida la humedad de un string, recibe los parametros :
        humedad_str (str): String con humedad (ej: "65%") y retorna: tupla: (es_valido, humedad_float)
    """
    try:
        # Quitar el símbolo % y extraer número
        humedad = float(humedad_str.replace("%", ""))

        # La humedad debe estar entre 0 y 100
        if humedad < 0 or humedad > 100:
            return False, None

        return True, humedad

    except ValueError:
        return False, None


def validar_clima_actual(datos):
    """
    Valida los datos del clima actual recibidos de la API, recibe parámetros:
        datos (dict): Diccionario con datos del clima y retornará: tupla: (es_valido, mensaje)
    """
    # Si hay error en la respuesta
    if "error" in datos:
        return False, f"Error de API: {datos.get('status', 'Desconocido')}"

    # Verificar campos obligatorios
    campos_necesarios = ["Ubicación", "Temperatura", "Humedad", "Clima"]

    for campo in campos_necesarios:
        if campo not in datos:
            return False, f"Falta el campo: {campo}"

    # Validar temperatura
    temp_valida, temp = validar_temperatura(datos["Temperatura"])
    if not temp_valida:
        return False, "Temperatura con formato incorrecto"

    # Validar humedad
    hum_valida, hum = validar_humedad(datos["Humedad"])
    if not hum_valida:
        return False, "Humedad con formato incorrecto"

    return True, "Datos válidos"


def validar_pronostico(datos):
    """
    Valida los datos del pronóstico recibidos de la API, recibe parámetros:
        datos (dict): Diccionario con pronóstico y retorna: tupla: (es_valido, mensaje)
    """
    # Si hay error
    if "error" in datos:
        return False, f"Error de API: {datos.get('status', 'Desconocido')}"

    # Debe tener pronóstico de 5 días
    if "Pronóstico 5 dias" not in datos:
        return False, "Falta el pronóstico"

    pronostico = datos["Pronóstico 5 dias"]

    # Verificar que haya al menos un día
    if len(pronostico) == 0:
        return False, "El pronóstico está vacío"

    # Validar cada día del pronóstico
    for dia in pronostico:
        # Verificar campos básicos
        if "Fecha" not in dia:
            return False, "Falta fecha en el pronóstico"

        if "Temperatura mín" not in dia or "Temperatura máx" not in dia:
            return False, "Faltan temperaturas en el pronóstico"

        # La temperatura mínima debe ser menor que la máxima
        if dia["Temperatura mín"] > dia["Temperatura máx"]:
            return False, f"Error en temperaturas del día {dia['Fecha']}"

    return True, "Pronóstico válido"


def validar_calidad_aire(datos):
    """ Valida los datos de calidad del aire recibe parámetros:
        datos (dict): Diccionario con calidad del aire
        y retorna: tupla: (es_valido, mensaje)
    """
    # Si hay error
    if "error" in datos:
        return False, f"Error de API: {datos.get('status', 'Desconocido')}"

    # Debe tener información de calidad del aire
    if "calidad_aire" not in datos:
        return False, "Falta información de calidad del aire"

    calidad = datos["calidad_aire"]

    # Verificar índice
    if "indice" not in calidad:
        return False, "Falta el índice de calidad"

    indice = calidad["indice"]

    # El índice debe estar entre 1 y 5
    if indice < 1 or indice > 5:
        return False, f"Índice fuera de rango: {indice}"

    return True, "Calidad del aire válida"


# Función de prueba (puedes descomentar para probar)
if __name__ == "__main__":
    # Pruebas básicas
    print("=== Pruebas de validación ===")

    # Probar validación de ciudad
    valido, msg = validar_ciudad("Madrid")
    print(f"Madrid: {valido} - {msg}")

    valido, msg = validar_ciudad("")
    print(f"Vacío: {valido} - {msg}")

    valido, msg = validar_ciudad("123")
    print(f"Solo números: {valido} - {msg}")

    # Probar validación de temperatura
    valido, temp = validar_temperatura("15.5°C")
    print(f"Temperatura: {valido} - {temp}")