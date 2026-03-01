"""Consulta Meteorológica
Punto de entrada principal del programa """

from src.api import weather_main
from src.data import storage_main
from src.ui import mostrar_menu_principal, obtener_opcion_usuario, exporter_main

"""
Autores: Lucas, Isamir, Josue y Adrian DAW (2026) EPSUM
Fecha: Febrero 2026
"""

def main():

    print("Aplicación de Clima")
    print("Versión 0.2 - Sprint 2")

while True:
    mostrar_menu_principal()
    opcion = obtener_opcion_usuario()

    if opcion == "4":
        print("\nGracias por su visita!")
        break
    elif opcion == "1":
        weather_main()
    elif opcion == "2":
        storage_main()
    elif opcion == "3":
        exporter_main()
    else:
        print("\nLa opción no es valida. Intenta de nuevo!")

main()