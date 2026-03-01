"""
mostrar menú principal, capturar entrada del usuario, gestionar navegación entre opciones
"""

# AL FINAL
def mostrar_menu_principal():
    """PRIMERA PROPUESTA DE MOSTRAR EL MENU"""

    print("\n"+ "========================================")
    print(" APLICACIÓN DE CONSULTA METEOROLÓGICA")
    print("1. Consultar")
    print("2. Historial")
    print("3. Exportar datos")
    print("4. Salir")


# capturar la opcion selecciona por el usuario, retorna la opcion elegida
def obtener_opcion_usuario():
  #continuar validación en Sprint 2
    return input("Selecciona una opción: ")