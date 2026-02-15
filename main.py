"""Aplicación de Consulta Meteorológica
Punto de entrada principal del programa """

"""
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
        print("\n Aguarde: funcion pendiente - sprint 2!")
    elif opcion == "2":
        print("\nAguarde: funcion pendiente - sprint 2!")
    elif opcion == "3":
        print("\nAguarde: funcion pendiente - sprint 2!")
    elif opcion == "4":
        print("\nAguarde: funcion pendiente - sprint 2!")
    else:
        print("\nLa opción no es valida. Intenta de nuevo!")

#Ejecutar el programa
main()