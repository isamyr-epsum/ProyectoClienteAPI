""" El Módulo LOGIC - Capa de Lógica de Negocio
Sus responsabilidades son :
1. Procesamiento de datos meteorológicos
2. Análisis y cálculos estadísticos
3. Validación de datos
"""
from .data_analyzer import analizar_datos, calcular_estadisticas
from .validator import validar_humedad, validar_pronostico, validar_temperatura, validar_ciudad, validar_calidad_aire, validar_clima_actual