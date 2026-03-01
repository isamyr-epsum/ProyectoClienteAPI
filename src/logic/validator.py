"""
autor: Lucas
"""
""" La funcion validar ciudad comprueba que el nombre de ciudad sea válido
    recibe parámetros: ciudad (str): Nombre de la ciudad a validary retorna: tupla: (es_valido, mensaje)
   """
def validar_ciudad(ciudad):
    #  Primero compruebo que el usuario escribió algo
    # Valida que el nombre de ciudad sea correcto antes de consultar la API
    if not ciudad or ciudad.strip() == "":
        return False, "El nombre de la ciudad está vacío"

    # Limpiar espacios principios y alfinal
    ciudad = ciudad.strip()

    # Debe tener al menos 2 letras
    if len(ciudad) < 2:
        return False, "El nombre es demasiado corto"

    # No mas de 50 caracteres (limite razonable)
    if len(ciudad) > 50:
        return False, "El nombre es demasiado largo"

    # No puede ser solo numeros ej_ 123: no es valido
    if ciudad.isdigit():
        return False, "El nombre no puede ser solo números"

    return True, "Ciudad válida"


def validar_temperatura(temp_str):
    """
    - Extrae el numero de temperatura y verifica que este en un rango lógico
    Validar extrae y valida la temperatura de un string, recibe parámetros:
        temp_str (str): String con temperatura (ej: "15.5°C")
        retorna: tupla: (es_valido, temperatura_float)
         EJEMPLO: La API devuelve "18.5°C" como texto, necesito convertirlo a numero
        y verificar que sea una temperatura razonable
    """
    try:
        # Separo por °C para quedarme solo con el número
        # Ejemplo: "18.5°C" → ["18.5", ""] → tomo "18.5"
        temp = float(temp_str.split("°C")[0])

        # Verifico que sea una temperatura posible en la Tierra
        # -60°C (Antártida) hasta 60°C (desiertos más calientes)
        if temp < -60 or temp > 60:
            return False, None

        return True, temp

    except (ValueError, IndexError):
        # Si no puedo convertir a número, es inválida
        return False, None


def validar_humedad(humedad_str):
    """
    - Extrae el porcentaje de humedad y verifica que esté entre 0% y 100%
    Extrae y valida la humedad de un string, recibe los parametros :
        humedad_str (str): String con humedad (ej: "65%") y retorna: tupla: (es_valido, humedad_float)
    """
    try:
        # Quito el símbolo % y convierto a numero
        # Ejemplo: "65%" → "65" → 65.0
        humedad = float(humedad_str.replace("%", ""))

        # Si falla la conversión, es inválida
        if humedad < 0 or humedad > 100:
            return False, None

        return True, humedad

    except ValueError:
        return False, None


def validar_clima_actual(datos):
    """
    - Verifica que los datos del clima de la API sean correctos
    Valida los datos del clima actual recibidos de la API, recibe parámetros:
        datos (dict): Diccionario con datos del clima y retornará: tupla: (es_valido, mensaje)
    Antes de procesar los datos con data_analyzer.py, verifico que tengan todos los campos necesarios y en formato correcto
    """
    # Si la API devolvio un error, los datos no son válidos
    if "error" in datos:
        return False, f"Error de API: {datos.get('status', 'Desconocido')}"

    # Verificar los campos obligatorios
    campos_necesarios = ["ubicación", "temperatura", "humedad", "clima"]

    for campo in campos_necesarios:
        if campo not in datos:
            return False, f"Falta el campo: {campo}"

    # Validar temperatura
    temp_valida, temp = validar_temperatura(datos["temperatura"])
    if not temp_valida:
        return False, "Temperatura con formato incorrecto"

    # Validar humedad
    hum_valida, hum = validar_humedad(datos["humedad"])
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

    # Debe tener pronostico de 5 dias
    if "pronostico_5_dias" not in datos:
        return False, "Falta el pronóstico"

    pronostico = datos["pronostico_5_dias"]

    # Verificar que haya al menos un día
    if len(pronostico) == 0:
        return False, "El pronóstico está vacío"

    # Validar cada dia del pronóstico
    for dia in pronostico:
        # Verificar campos básicos
        if "fecha" not in dia:
            return False, "Falta fecha en el pronóstico"
        # Y temperaturas mínima y máxima

        if "temperatura_min" not in dia or "temperatura_max" not in dia:
            return False, "Faltan temperaturas en el pronóstico"

        # La mínima no puede ser mayor que la máxima (lógica básica)
        if dia["temperatura_min"] > dia["temperatura_max"]:
            return False, f"Error en temperaturas del día {dia['fecha']}"

    return True, "Pronóstico válido"


def validar_calidad_aire(datos):
    """ Valida los datos de calidad del aire
        recibe parámetros: datos (dict): Diccionario con calidad del aire
        y retorna: tupla: (es_valido, mensaje)
    """
    # Si hay error
    if "error" in datos:
        return False, f"Error de API: {datos.get('status', 'Desconocido')}"

    # Debe tener información de calidad del aire
    if "calidad_aire" not in datos:
        return False, "Falta información de calidad del aire"

    calidad = datos["calidad_aire"]

    # Verificar que haya un índice
    if "indice" not in calidad:
        return False, "Falta el índice de calidad"

    indice = calidad["indice"]

    # El índice APi debe estar entre 1 y 5
    if indice < 1 or indice > 5:
        return False, f"Índice fuera de rango: {indice}"

    return True, "Calidad del aire válida"


# Funcion de prueba
if __name__ == "__main__":
    # pruebas básicas
    print("=== Pruebas de validación ===\n")

    # probar validación de ciudad
    print("--Validacion de la ciudades---")
    valido, msg = validar_ciudad("Madrid")
    print(f"Madrid: {valido} - {msg}")

    valido, msg = validar_ciudad("")
    print(f"Vacío: {valido} - {msg}")

    valido, msg = validar_ciudad("123")
    print(f"Solo números: {valido} - {msg}")

    valido, msg = validar_ciudad("M")
    print(f"Demasiado Corto: {valido} - {msg}")


    # probar validación de temperatura
    print("---Validadcion de temperaturas---")
    valido, temp = validar_temperatura("15.5°C")
    print(f"Temperatura: {valido} - {temp}")

    valido, temp = validar_temperatura("100°C")
    print(f"100°C - Fuera de rango: {valido} - Valor: {temp}")


    #probar validacion de humedad
    print("---Validacion de Humedad---")
    valido, hum = validar_humedad("65%")
    print(f"65%: {valido} -Valor {hum}")

    valido, hum = validar_humedad("150%")
    print(f"150% - Fuera de rango {valido} -Valor {hum}")