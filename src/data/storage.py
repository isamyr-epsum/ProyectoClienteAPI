import json

from src.logic import calcular_estadisticas

def guardar_historial(ciudad, accion, datos):
    consulta = {
        "ciudad": ciudad,
        "consulta": accion,
        "datos": datos,
    }
    consulta = json.dumps(consulta)

    with open("historial.txt", "a", encoding="utf-8") as f:
        f.write(consulta + "\n")

def cargar_historial():

    with open("historial.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                data = json.loads(line)
                print(json.dumps(data, indent=4, ensure_ascii=False))
            except json.JSONDecodeError as e:
                print(f"\nError en línea {i}")
                print(f"Contenido: {line}")
                print(f"Error: {e}")
                break

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