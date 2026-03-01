"""
- exportar los datos en formato JSON
- exportar los datos en formato CSV
- generar los reportes en PDF
"""

# exporta datos en formato json,
def exportar_json(datos, nombre_archivo):
    # Sprint 2
    pass

#Exportar datos en formato CSV
def exportar_csv(datos, nombre_archivo):
    #sprint 2
    pass

#exportar y generar reporte en pdf
def exportar_pdf(datos, nombre_archivo):
    #Sprint 2
    pass

def exporter_main():
    continuar = True
    while continuar:
        print("Opciones a exportar")
        opcion = int(input("1. JSON \n 2. CSV \n 3. PDF \n 4. Volver al menú principal \n Opcion: "))
        if opcion == 1:
            exportar_json()
        if opcion == 2:
            exportar_csv()
        if opcion == 3:
            exportar_pdf()
        if opcion == 4:
            print("Volviendo al menú")
            continuar = False