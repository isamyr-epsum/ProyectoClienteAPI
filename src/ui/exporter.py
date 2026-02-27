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
        pdf.add_page()
        pdf.set_font("helvetica", "B", 14)
        pdf.cell(0, 10, "Reporte", ln=True, align="C")
        pdf.set_font("helvetica", "", 12)
        for fila in datos:
            for clave, valor in fila.items():
                if isinstance(valor, dict):
                    valor = json.dumps(valor, ensure_ascii=False)
                pdf.cell(0, 8, f"{clave}: {valor}", ln=True)
            pdf.ln(2)
        pdf.output(nombre_archivo + ".pdf")
        print(f"Se ha guardado el archivo en formato PDF: {nombre_archivo}.pdf")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")
