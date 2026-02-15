"""
mostrar menú principal, capturar entrada del usuario, gestionar navegación entre opciones
"""


def mostrar_menu_principal():
    """PRIMERA PROPUESTA DE MOSTRAR EL MENU"""

    print("\n"+ "========================================")
    print(" APLICACIÓN DE CONSULTA METEOROLÓGICA")
    print("1. Consultar clima actual")
    print("2. Consultar pronóstico")
    print("3. Ver historial")
    print("4. Exportar datos")
    print("5. Salir")


# capturar la opcion selecciona por el usuario, retorna la opcion elegida
def obtener_opcion_usuario():
  #continuar validación en Sprint 2
    return input("Selecciona una opción: ")