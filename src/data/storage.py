import datetime

#guarda historial de consultas
#recupera datos históricos
#gestiona archivos locales

#guarda una consulta en el historial
def guardar_historial(decision, ciudad, accion, datos):
    ahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if decision == 1:
        temperatura = datos["temperatura"]
        msg = f"Consulto en {ciudad} {accion} ({temperatura}) - {ahora}"
    elif decision == 2:
        dates = []
        temperatura_media = []
        for fecha in datos["pronostico_5_dias"]:
            dates.append(fecha["fecha"])
            media = (fecha["temperatura_max"] + fecha["temperatura_min"])/2
            temperatura_media.append(round(media, 2))

        lineas_pronostico = []
        for fecha, temp in zip(dates, temperatura_media):
            linea = f"{fecha} -> {temp}ºC"
            lineas_pronostico.append(linea)

        bloque_pronostico = "\n".join(lineas_pronostico)

        msg = (f"Consulto en {ciudad} {accion}:\n"
               f"{bloque_pronostico}\n"
               f"{ahora}")
    elif decision == 3:
        calidadAire = datos["calidad_aire"]["mensaje"]
        msg = f"Consulto en {ciudad} {accion} ({calidadAire}) - {ahora}"

    with open("historial.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")


# carga el historia de consultas guardas
def cargar_historial():
    print("hola")
    with open("historial.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            print(line)

#elimina el historial de consultas
def limpiar_historial():
    print("Limpiando todo el historial")
    with open("historial.txt", "w", encoding="utf-8") as f:
        f.write("")
    print("Historial eliminado")
    print("Abriendo historial eliminado")
    with open("historial.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
    print("No hay historial")