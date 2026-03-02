"""
Módulo de exportación de datos
Permite exportar datos meteorológicos en formatos JSON, CSV y PDF
"""

import json
import csv
from pathlib import Path
from fpdf import FPDF


def exportar_json(consulta, ciudad, datos):
    """
    Exporta datos en formato JSON

    Parámetros:
        consulta (str): Tipo de consulta (ej: "Clima actual")
        ciudad (str): Nombre de la ciudad
        datos (dict): Datos a exportar
    """
    try:
        # Crear nombre de archivo
        consulta_limpia = consulta.lower().replace(" ", "_")
        ciudad_limpia = ciudad.lower().replace(" ", "_")
        nombre_archivo = f"{consulta_limpia}_{ciudad_limpia}.json"

        # Guardar archivo
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

        print(f"Archivo guardado: {nombre_archivo}")

    except Exception as e:
        print(f"Error al guardar JSON: {e}")
        raise


def exportar_csv(consulta, ciudad, datos):
    """
    Exporta datos en formato CSV

    Parámetros:
        consulta (str): Tipo de consulta
        ciudad (str): Nombre de la ciudad
        datos (dict o list): Datos a exportar
    """
    try:
        # Crear nombre de archivo
        consulta_limpia = consulta.lower().replace(" ", "_")
        ciudad_limpia = ciudad.lower().replace(" ", "_")
        nombre_archivo = f"{consulta_limpia}_{ciudad_limpia}.csv"

        # Si datos es un diccionario, convertir a lista
        if isinstance(datos, dict):
            # Aplanar el diccionario para CSV
            datos_planos = aplanar_diccionario(datos)
            datos_lista = [datos_planos]
        else:
            datos_lista = datos

        if not datos_lista:
            print("No hay datos para exportar")
            return

        # Guardar archivo
        with open(nombre_archivo, "w", newline='', encoding="utf-8") as f:
            campos = list(datos_lista[0].keys())
            escritor = csv.DictWriter(f, fieldnames=campos, delimiter=';')
            escritor.writeheader()

            for fila in datos_lista:
                escritor.writerow(fila)

        print(f"Archivo guardado: {nombre_archivo}")

    except Exception as e:
        print(f"Error al guardar CSV: {e}")
        raise


def exportar_pdf(consulta, ciudad, datos):
    """
    Exporta datos en formato PDF

    Parámetros:
        consulta (str): Tipo de consulta
        ciudad (str): Nombre de la ciudad
        datos (dict): Datos a exportar
    """
    try:
        # Crear nombre de archivo
        consulta_limpia = consulta.lower().replace(" ", "_")
        ciudad_limpia = ciudad.lower().replace(" ", "_")
        nombre_archivo = f"{consulta_limpia}_{ciudad_limpia}.pdf"

        # Crear PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Título
        pdf.set_font("helvetica", "B", 16)
        pdf.cell(0, 10, f"{consulta} - {ciudad}", ln=True, align="C")
        pdf.ln(5)

        # Contenido
        pdf.set_font("helvetica", "", 11)

        # Procesar datos
        if isinstance(datos, dict):
            escribir_dict_en_pdf(pdf, datos)
        elif isinstance(datos, list):
            for item in datos:
                escribir_dict_en_pdf(pdf, item)
                pdf.ln(3)

        # Guardar archivo
        pdf.output(nombre_archivo)
        print(f"Archivo guardado: {nombre_archivo}")

    except Exception as e:
        print(f"Error al guardar PDF: {e}")
        raise


def escribir_dict_en_pdf(pdf, datos, nivel=0):
    """
    Escribe un diccionario en el PDF de forma recursiva

    Parámetros:
        pdf: Objeto FPDF
        datos: Diccionario con datos
        nivel: Nivel de indentación
    """
    margen_izquierdo = 10 + (nivel * 5)  # Indentación progresiva

    for clave, valor in datos.items():
        # Convertir clave y valor a string
        clave_str = str(clave)

        if isinstance(valor, dict):
            # Si es un diccionario anidado
            pdf.set_font("helvetica", "B", 10)
            pdf.set_x(margen_izquierdo)
            pdf.multi_cell(0, 6, f"{clave_str}:", align='L')
            pdf.set_font("helvetica", "", 9)
            escribir_dict_en_pdf(pdf, valor, nivel + 1)

        elif isinstance(valor, list):
            # Si es una lista
            pdf.set_font("helvetica", "B", 10)
            pdf.set_x(margen_izquierdo)
            pdf.multi_cell(0, 6, f"{clave_str}:", align='L')
            pdf.set_font("helvetica", "", 9)

            for i, item in enumerate(valor):
                if isinstance(item, dict):
                    pdf.set_x(margen_izquierdo + 5)
                    pdf.set_font("helvetica", "B", 9)
                    pdf.multi_cell(0, 5, f"Item {i + 1}:", align='L')
                    pdf.set_font("helvetica", "", 9)
                    escribir_dict_en_pdf(pdf, item, nivel + 1)
                else:
                    item_str = str(item)
                    # Limitar longitud del texto
                    if len(item_str) > 80:
                        item_str = item_str[:80] + "..."
                    pdf.set_x(margen_izquierdo + 5)
                    pdf.multi_cell(0, 5, f"- {item_str}", align='L')
        else:
            # Valor simple
            valor_str = str(valor)
            # Limitar longitud del texto
            if len(valor_str) > 100:
                valor_str = valor_str[:100] + "..."

            texto = f"{clave_str}: {valor_str}"
            pdf.set_x(margen_izquierdo)
            pdf.set_font("helvetica", "", 9)
            pdf.multi_cell(0, 5, texto, align='L')

def aplanar_diccionario(datos, prefijo=''):
    """
    Aplana un diccionario anidado para CSV

    Parámetros:
        datos (dict): Diccionario a aplanar
        prefijo (str): Prefijo para las claves

    Retorna:
        dict: Diccionario aplanado
    """
    resultado = {}

    for clave, valor in datos.items():
        nueva_clave = f"{prefijo}{clave}" if prefijo else clave

        if isinstance(valor, dict):
            # Recursivo para diccionarios anidados
            resultado.update(aplanar_diccionario(valor, f"{nueva_clave}_"))
        elif isinstance(valor, list):
            # Convertir listas a string
            resultado[nueva_clave] = str(valor)
        else:
            resultado[nueva_clave] = valor

    return resultado


# Funciones originales para compatibilidad con consola

def cargar_todos_log_json():
    """Carga todos los archivos JSON del caché"""
    carpeta = Path("cache")
    datos = []

    if not carpeta.exists():
        return datos

    for archivo in carpeta.glob("*.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos.append(json.load(f))
        except Exception as e:
            print(f"Error leyendo {archivo.name}: {e}")

    return datos


def exporter_main():
    """Menú para exportar historial completo (versión consola)"""
    continuar = True
    while continuar:
        datos = cargar_todos_log_json()

        print("Opciones a exportar")
        opcion = int(input("1. JSON \n2. CSV \n3. PDF \n4. Volver al menú principal \nOpción: "))

        if opcion == 1:
            exportar_json("Historial", "completo", datos)
        elif opcion == 2:
            exportar_csv("Historial", "completo", datos)
        elif opcion == 3:
            exportar_pdf("Historial", "completo", datos)
        elif opcion == 4:
            print("Volviendo al menú")
            continuar = False


def exporter_main_consulta(accion, ciudad, datos):
    """Menú para exportar una consulta específica (versión consola)"""
    continuar = True
    while continuar:
        print("Opciones a exportar")
        opcion = int(input("1. JSON \n2. CSV \n3. PDF \n4. Volver al menú principal \nOpción: "))

        if opcion == 1:
            exportar_json(accion, ciudad, datos)
        elif opcion == 2:
            exportar_csv(accion, ciudad, datos)
        elif opcion == 3:
            exportar_pdf(accion, ciudad, datos)
        elif opcion == 4:
            print("Volviendo al menú")
            continuar = False