"""
Archivo principal de la aplicación DataClima
Autor: Equipo (Isamir, Lucas, Josue, Adrian)
Sprint 2 - Febrero 2025

Punto de entrada de la aplicación
"""

import tkinter as tk

from src.data import storage_main
from src.api import weather_main
from src.ui import exporter_main


def main():
    while True:
        print("--- MENU PRINCIPAL ---")
        print("1 - Consultar")
        print("2 - Historial")
        print("3 - Exportar")
        print("4 - Salir")
        opcion = input("Escoga una opción -- > ")
        if opcion == "1":
            weather_main()
        if opcion == "2":
            storage_main()
        if opcion == "3":
            exporter_main()
        if opcion == "4":
            print("Adios")
            break

main()

# if __name__ == "__main__":
#     # Crear la ventana principal
#     # root = tk.Tk ()
#     mostrar_menu_principal()
#     # Iniciar la aplicación
#     # app = mostrar_menu_principal()
#     # app.mainloop()
#
#     # Ejecutar el loop de la interfaz
#     # root.mainloop()