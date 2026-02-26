import datetime

#guarda historial de consultas
#recupera datos históricos
#gestiona archivos locales

#guarda una consulta en el historial
def guardar_historial(decision, ciudad, accion, datos):
# def guardar_historial():
    ahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if decision == 1:
        msg = f"Consulto en {ciudad} {accion} ({datos}) - {ahora}"
    elif decision == 2:
        fechas, temperaturas = datos

        lineas_pronostico = []
        for fecha, temp in zip(fechas, temperaturas):
            linea = f"{fecha} -> {temp}ºC"
            lineas_pronostico.append(linea)

        bloque_pronostico = "\n".join(lineas_pronostico)

        msg = (f"Consulto en {ciudad} {accion}:\n"
               f"{bloque_pronostico}\n"
               f"{ahora}")
    elif decision == 3:
        msg = f"Consulto en {ciudad} {accion} ({datos}) - {ahora}"

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
# TODO HECHO
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