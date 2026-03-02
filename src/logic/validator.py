def validar_ciudad(ciudad):

    if not ciudad or ciudad.strip() == "":
        return False, "El nombre de la ciudad está vacío"

    ciudad = ciudad.strip()

    if len(ciudad) < 2:
        return False, "El nombre es demasiado corto"

    if len(ciudad) > 50:
        return False, "El nombre es demasiado largo"

    if ciudad.isdigit():
        return False, "El nombre no puede ser solo números"

    return True, "Ciudad válida"


def validar_temperatura(temp_str):
    try:
        # Separo por °C para quedarme solo con el número para las estadísticas
        # Ejemplo: "18.5°C" → ["18.5", ""] → tomo "18.5"
        temp = float(temp_str.split("°C")[0])

        if temp < -60 or temp > 60:
            return False, None

        return True, temp

    except (ValueError, IndexError):
        return False, None


def validar_humedad(humedad_str):
    try:
        # Quito el símbolo % y convierto a número para las estadísticas
        # Ejemplo: "65%" → "65" → 65.0
        humedad = float(humedad_str.replace("%", ""))

        if humedad < 0 or humedad > 100:
            return False, None

        return True, humedad

    except ValueError:
        return False, None


def validar_clima_actual(datos):
    if "error" in datos:
        return False, f"Error de API: {datos.get('status', 'Desconocido')}"

    campos_necesarios = ["Ubicación", "Temperatura", "Humedad", "Clima"]

    for campo in campos_necesarios:
        if campo not in datos:
            return False, f"Falta el campo: {campo}"

    temp_valida, temp = validar_temperatura(datos["Temperatura"])
    if not temp_valida:
        return False, "Temperatura con formato incorrecto"

    hum_valida, hum = validar_humedad(datos["Humedad"])
    if not hum_valida:
        return False, "Humedad con formato incorrecto"

    return True, "Datos válidos"


def validar_pronostico(datos):
    if "error" in datos:
        return False, f"Error de API: {datos.get('status', 'Desconocido')}"

    if "Pronóstico 5 dias" not in datos:
        return False, "Falta el pronóstico"

    pronostico = datos["Pronóstico 5 dias"]

    if len(pronostico) == 0:
        return False, "El pronóstico está vacío"

    for dia in pronostico:
        # Verificar campos básicos
        if "Fecha" not in dia:
            return False, "Falta fecha en el pronóstico"
        # Y temperaturas mínima y máxima

        if "Temperatura mín" not in dia or "Temperatura máx" not in dia:
            return False, "Faltan temperaturas en el pronóstico"

        # La mínima no puede ser mayor que la máxima (lógica básica)
        if dia["Temperatura mín"] > dia["Temperatura máx"]:
            return False, f"Error en temperaturas del día {dia['Fecha']}"

    return True, "Pronóstico válido"


def validar_calidad_aire(datos):

    # Si hay error
    if "error" in datos:
        return False, f"Error de API: {datos.get('status', 'Desconocido')}"

    if "Calidad de aire" not in datos:
        return False, "Falta información de calidad del aire"

    calidad = datos["Calidad de aire"]

    if "Índice" not in calidad:
        return False, "Falta el índice de calidad"

    indice = calidad["Índice"]

    if indice < 1 or indice > 5:
        return False, f"Índice fuera de rango: {indice}"

    return True, "Calidad del aire válida"