import datetime

#guarda historial de consultas
#recupera datos históricos
#gestiona archivos locales

#guarda una consulta en el historial
def guardar_historial(ciudad, accion, datos):
# def guardar_historial():
    ahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    msg = f"Consulto en {ciudad} {accion} ({datos}ºC) - {ahora}"
    with open("historial.txt", "w", encoding="utf-8") as f:
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