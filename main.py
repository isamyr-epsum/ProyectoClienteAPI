"""hhjhjhjhjhAplicación de Consulta Meteorológica
Punto de entrada principal del programa """
from time import sleep

from src.api.cache_manager import guardar_en_cache, obtener_de_cache
from src.api.weather_api import weather_main
from src.data.storage import guardar_historial, cargar_historial, limpiar_historial

"""
PRUEBA LUCAS
Autores: Lucas, Isamir, Josue y Adrian DAW (2026) EPSUM
Fecha: Febrero 2026
"""
from src.ui.menu import mostrar_menu_principal, obtener_opcion_usuario

#Función principal de la aplicación
def main():

    print("Aplicación de Clima")
    print("Versión 0.1 - Sprint 1") # crear versiones, para controlar logros y errores que puedan surgir

while True:
    mostrar_menu_principal()
    opcion = obtener_opcion_usuario()

    if opcion == "5":
        print("\nGracias por su visita!")
        break
    elif opcion == "1":
        resultado = weather_main()
        print("Este es el resultado en JSON")
        print(resultado)
        decision = resultado["decision"]
        ciudad = resultado["ciudad"]
        accion = resultado["accion"]
        datos = resultado["datos"]
        guardar_historial(decision,ciudad, accion, datos)
        print("Guardamos en cache")
        guardar_en_cache(ciudad, datos)
        print("Obtenemos en cache")
        obtener_de_cache(ciudad)
    elif opcion == "2":
        print("\nAguarde: funcion pendiente - sprint 2!")
    elif opcion == "3":
        guardar_historial("Madrid", "la temperatura actual", 18)
        sleep(3)
        cargar_historial()
        sleep(2)
        # limpiar_historial()
    elif opcion == "4":
        print("\nAguarde: funcion pendiente - sprint 2!")
    else:
        print("\nLa opción no es valida. Intenta de nuevo!")

#Ejecutar el programa
main()