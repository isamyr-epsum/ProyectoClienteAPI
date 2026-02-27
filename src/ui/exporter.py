import json
import csv
from fpdf import FPDF


def exportar_json(datos, nombre_archivo):
    try:
        with open(nombre_archivo + ".json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"Se ha guardado el archivo en formato JSON: {nombre_archivo}.json")
    except:
        print("Error al guardar JSON")


def exportar_csv(datos, nombre_archivo):
    if not datos:
        print("No hay datos para crear el CSV")
        return
    try:
        with open(nombre_archivo + ".csv", "w", newline='', encoding="utf-8") as f:
            campos = list(datos[0].keys())
            escribirCSV = csv.DictWriter(f, fieldnames=campos)
            escribirCSV.writeheader()
            for fila in datos:
                escribirCSV.writerow(fila)
        print(f"Se ha guardado el archivo en formato CSV: {nombre_archivo}.csv")
    except:
        print("Error al guardar CSV")

#exportar y generar reporte en pdf
def exportar_pdf(datos, nombre_archivo):
    #Sprint 2
    pass