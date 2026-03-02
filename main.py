"""
Archivo principal de la aplicación DataClima Con Tkinter
Autor: Equipo (Isamir, Lucas, Josue, Adrian)
Sprint 2 - Febrero 2025
"""

import tkinter as tk
from src.ui.menu import AplicacionClima


def main():
    """Inicia la aplicación con interfaz gráfica"""

    print("=" * 50)
    print(" DATACLIMA - Aplicación Meteorológica")
    print("=" * 50)
    print("\nIniciando interfaz gráfica...\n")

    # Creamos ventana
    root = tk.Tk()

    # Iniciar aplicación
    app = AplicacionClima(root)

    # Ejecutar
    root.mainloop()

    print("\nAplicación cerrada. Hasta pronto!!")


if __name__ == "__main__":
    main()