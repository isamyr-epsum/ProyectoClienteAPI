import json
import csv
from pathlib import Path

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
    if isinstance(datos, dict):
        datos = [datos]
    try:
        with open(nombre_archivo + ".csv", "w", newline='', encoding="utf-8") as f:
            campos = list(datos[0].keys())
            escribirCSV = csv.DictWriter(f, fieldnames=campos, delimiter=';')
            escribirCSV.writeheader()
            for fila in datos:
                escribirCSV.writerow(fila)
        print(f"Se ha guardado el archivo en formato CSV: {nombre_archivo}.csv")
    except Exception as e:
        print(f"Error al guardar CSV: {e}")

def exportar_pdf(datos, nombre_archivo):
    if not datos:
        print("No hay datos para crear el PDF")
        return

    if isinstance(datos, dict):
        datos = [datos]

    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        pdf.set_font("helvetica", "B", 14)
        pdf.cell(0, 10, "Reporte", ln=True, align="C")
        pdf.ln(5)
        pdf.set_font("helvetica", "", 12)

        for fila in datos:
            for clave, valor in fila.items():

                if isinstance(valor, dict):
                    valor = json.dumps(valor, ensure_ascii=False, indent=2)
                pdf.set_x(10)
                pdf.multi_cell(0, 8, f"{clave}: {valor}")
            pdf.ln(4)
        pdf.output(nombre_archivo + ".pdf")
        print(f"Se ha guardado el archivo en formato PDF: {nombre_archivo}.pdf")

    except Exception as e:
        print(f"Error al generar el PDF: {e}")

def cargar_todos_log_json():
    carpeta = Path("cache")
    datos = []
    for archivo in carpeta.glob("*.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos.append(json.load(f))
        except Exception as e:
            print(f"Error leyendo {archivo.name}: {e}")
    return datos

def exporter_main():
    continuar = True
    while continuar:
        datos = cargar_todos_log_json()
        nombreArchivo = "historial_completo"
        print("Opciones a exportar")
        opcion = int(input("1. JSON \n 2. CSV \n 3. PDF \n 4. Volver al menú principal \n Opcion: "))
        if opcion == 1:
            exportar_json(datos, nombreArchivo)
        if opcion == 2:
            exportar_csv(datos, nombreArchivo)
        if opcion == 3:
            exportar_pdf(datos, nombreArchivo)
        if opcion == 4:
            print("Volviendo al menú")
            continuar = False

def exporter_main_consulta(accion, ciudad, datos):
    continuar = True
    while continuar:
        accion = accion.lower().replace(" ", "_")
        nombreArchivo = f"{accion}_{ciudad.lower()}"
        print("Opciones a exportar")
        opcion = int(input("1. JSON \n 2. CSV \n 3. PDF \n 4. Volver al menú principal \n Opcion: "))
        if opcion == 1:
            exportar_json(datos, nombreArchivo)
        if opcion == 2:
            exportar_csv(datos, nombreArchivo)
        if opcion == 3:
            exportar_pdf(datos, nombreArchivo)
        if opcion == 4:
            print("Volviendo al menú")
            continuar = False
