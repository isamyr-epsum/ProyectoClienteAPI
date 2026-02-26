"""Este es el archivo de configuración del proyecto
Contendrá las claves API y configuraciones generales del proeycto

# IMPORTANTE: Este archivo NO se sube a Git (está en .gitignore)
Cada desarrollador debe tener su propia clave API de OpenWeatherMap (por consultar)
"""

# API Configuration

API_KEY = "TU_CLAVE_API_AQUI"  # Obtener en: https://openweathermap.org/api
API_BASE_URL = "https://api.openweathermap.org/data/2.5"

# Configuración de caché
CACHE_ENABLED = True
CACHE_DURATION_MINUTES = 10

# Configuración de exportación
DEFAULT_EXPORT_FORMAT = "JSON"  # JSON, CSV, PDF