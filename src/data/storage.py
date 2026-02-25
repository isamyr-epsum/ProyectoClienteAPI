
#guarda historial de consultas
#recupera datos históricos
#gestiona archivos locales


#guarda una consulta en el historial
# def guardar_historial(ciudad, datos):
def guardar_historial():
    msg = "Linea 0"
    with open("historial.txt", "w", encoding="utf-8") as f:
        f.write(msg + "\n")
    for x in range(10):
        msg = f"Linea {x}\n"
        with open("historial.txt", "a", encoding="utf-8") as f:
            f.write(msg)


# carga el historia de consultas guardas
def cargar_historial():
    # sprint 2
    pass

#elimina el historial de consultas
def limpiar_historial():
    #Sprint 2
    pass