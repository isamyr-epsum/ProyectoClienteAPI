"""
- guardar respuestas de la API en caché
- recuperar datos cacheados si están vigentes
- evitar llamadas innecesarias a la API
"""
import json
#Anadir imports necesarios
import os.path
import time

CACHE_DIR = 'cache'

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# Esta funcion guarda los datos meteorologicos en la cache. ciudad:STRING y DATOS a cachear: dict
def guardar_en_cache(ciudad, datos, tiempo_max=20):
    archivo = os.path.join(CACHE_DIR, f"{ciudad.lower()}.json")
    contenido = {
        "tiempo": time.time(),
        "tiempo_max": tiempo_max,
        "datos": datos,
    }

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(contenido, f, ensure_ascii=False, indent=4)

# recueperar datos , retornar datos cacheados o NONE si no existen
def obtener_de_cache(ciudad):
    archivo = os.path.join(CACHE_DIR, f"{ciudad.lower()}.json")
    if not os.path.exists(archivo):
        print("No hay archivo")
        return None

    with open(archivo, "r", encoding="utf-8") as f:
        contenido = json.load(f)

    tiempo = contenido.get("tiempo")
    tiempo_max = contenido.get("tiempo_max", 20)

    if time.time() - tiempo < tiempo_max:
        datos = contenido.get("datos")
        print(datos)
    else:
        os.remove(archivo)

    return None