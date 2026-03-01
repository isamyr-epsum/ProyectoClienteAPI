"""hhjhjhjhjhAplicación de Consulta Meteorológica
Punto de entrada principal del programa """
import json
import os
from time import sleep

# from src.api import guardar_en_cache, obtener_de_cache, weather_main
from src.api import weather_main
# from src.data import guardar_historial, storage_main
from src.data import storage_main
from src.logic import analizar_datos, calcular_estadisticas
from src.ui import mostrar_menu_principal, obtener_opcion_usuario, exporter_main

"""
PRUEBA LUCAS
Autores: Lucas, Isamir, Josue y Adrian DAW (2026) EPSUM
Fecha: Febrero 2026
"""

#Función principal de la aplicación
def main():

    print("Aplicación de Clima")
    print("Versión 0.1 - Sprint 1") # crear versiones, para controlar logros y errores que puedan surgir

while True:
    mostrar_menu_principal()
    opcion = obtener_opcion_usuario()

    if opcion == "4":
        print("\nGracias por su visita!")
        break
    elif opcion == "1":
        weather_main()
        # resultado = weather_main()
        # print("Este es el resultado en JSON")
        # print(resultado)
        # print("Estos son los datos de resultado")
        # print(resultado["datos"])
        # print("Analizamos los datos")
        # resultadoAnalizador = analizar_datos(resultado["datos"])
        # print("Mostramos los datos analizados")
        # print(resultadoAnalizador)
        # ciudad = resultado["ciudad"]
        # accion = resultado["consulta"]
        # datos = resultado["datos"]
        # # guardar_historial(ciudad, accion, datos)
        # historial = []
        # with open("historial.txt", "r", encoding="utf-8") as f:
        #     for consulta in f:
        #         historial.append(json.loads(consulta))
        # estadisticas = calcular_estadisticas(historial)
        # print("Estadísticas del historial")
        # print(estadisticas)
        # print("Guardamos en cache")
        # guardar_en_cache(ciudad, accion, resultadoAnalizador)
        # print("Obtenemos en cache")
        # obtener_de_cache(ciudad)
    elif opcion == "2":
        storage_main()
    elif opcion == "3":
        exporter_main()
    else:
        print("\nLa opción no es valida. Intenta de nuevo!")

#Ejecutar el programa
main()