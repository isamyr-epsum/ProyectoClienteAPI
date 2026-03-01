import datetime
import json

from src.logic import calcular_estadisticas


#guarda historial de consultas
#recupera datos históricos
#gestiona archivos locales

#guarda una consulta en el historial
def guardar_historial(ciudad, accion, datos):
    # ahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # if decision == 1:
    #     temperatura = datos["temperatura"]
        # msg = f"Consulto en {ciudad} {accion} ({temperatura}) - {ahora}"
    consulta = {
        "ciudad": ciudad,
        "consulta": accion,
        "datos": datos,
    }
    consulta = json.dumps(consulta)
    # elif decision == 2:
    #     dates = []
    #     temperatura_media = []
    #     for fecha in datos["pronostico_5_dias"]:
    #         dates.append(fecha["fecha"])
    #         media = (fecha["temperatura_max"] + fecha["temperatura_min"])/2
    #         temperatura_media.append(round(media, 2))
    #
    #     lineas_pronostico = []
    #     for fecha, temp in zip(dates, temperatura_media):
    #         linea = f"{fecha} -> {temp}ºC"
    #         lineas_pronostico.append(linea)
    #
    #     bloque_pronostico = "\n".join(lineas_pronostico)
    #
    #     msg = (f"Consulto en {ciudad} {accion}:\n"
    #            f"{bloque_pronostico}\n"
    #            f"{ahora}")
    # elif decision == 3:
    #     # calidadAire = datos["calidad_aire"]["mensaje"]
    #     # msg = f"Consulto en {ciudad} {accion} ({calidadAire}) - {ahora}"
    #     consulta = {
    #         "ciudad": ciudad,
    #         "accion": accion,
    #         "datos": datos,
    #     }

    with open("historial.txt", "a", encoding="utf-8") as f:
        f.write(consulta + "\n")


# carga el historia de consultas guardas
def cargar_historial():
    print("Historial completo")
    with open("historial.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line = json.loads(line)
            print(json.dumps(line, indent=4, ensure_ascii=False))

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

def storage_main():
    continuar = True
    while continuar:
        print("Menú del historial")
        opcion = int(input("Que acción desea hacer \n 1. Ver historial \n 2. Ver estadísticas del historial \n 3. Eliminar historial \n 4. Volver al menú principal \n Opcion: "))
        if opcion == 1:
            cargar_historial()
        if opcion == 2:
            historial = []
            with open("historial.txt", "r", encoding="utf-8") as f:
                for consulta in f:
                    historial.append(json.loads(consulta))
            estadisticas = calcular_estadisticas(historial)
            print("Estadísticas del historial")
            print(estadisticas)
        if opcion == 3:
            limpiar_historial()
        if opcion == 4:
            print("Volviendo al menú")
            continuar = False