"""Este es el archivo de configuración del proyecto
Contendrá las claves API y configuraciones generales del proeycto

# IMPORTANTE: Este archivo NO se sube a Git (está en .gitignore)
Cada desarrollador debe tener su propia clave API de OpenWeatherMap (por consultar)

LO SUBIMOS PARA USAR LA MISMA API KEY Y TENER LAS URLS
"""

# API Configuration

API_KEY = "a24cf1baa02349b165a1f6206bf525bc"  # Obtener en: https://openweathermap.org/api
BASE_URL_CLIMA_ACTUAL = "https://api.openweathermap.org/data/2.5/weather"
BASE_URL_PRONOSTICO = "https://api.openweathermap.org/data/2.5/forecast"
URL_AIRE = "https://api.openweathermap.org/data/2.5/air_pollution"