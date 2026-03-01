"""
Módulo API - Capa de Acceso a Datos

El directorio API tendrá lo siguiente:
1. Comunicar con OpenWeatherMap API
2. El sistema de caché para optimizar consultas
3. Formateo de datos JSON recibidos
"""
from .cache_manager import guardar_en_cache, obtener_de_cache
from .weather_api import weather_main