"""hhjhjhjhjhAplicación de Consulta Meteorológica
Punto de entrada principal del programa """
from src.api.weather_api import obtener_clima_actual
from src.ui.visualizer import obtener_clima_actual_grafico
"""
Autores: Lucas, Isamir, Josue y Adrian DAW (2026) EPSUM
Fecha: Febrero 2026
"""
from src.ui.menu import mostrar_menu_principal, obtener_opcion_usuario

def main():

    print("Aplicación de Clima")
    print("Versión 0.1 - Sprint 1")

while True:
    mostrar_menu_principal()
    opcion = obtener_opcion_usuario()

    if opcion == "5":
        print("\nGracias por su visita!")
        break
    elif opcion == "1":
        ciudad = input("Ingrese ciudad: ")
        obtener_clima_actual_grafico(ciudad)
    elif opcion == "2":
        print("\nAguarde: funcion pendiente - sprint 2!")
    elif opcion == "3":
        print("\nAguarde: funcion pendiente - sprint 2!")
    elif opcion == "4":
        print("\nAguarde: funcion pendiente - sprint 2!")
    else:
        print("\nLa opción no es valida. Intenta de nuevo!")

main()