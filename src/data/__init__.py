""" El Módulo DATA -  la Capa de Almacenamiento

Las Responsabilidades son:
1. Gestión de caché local
2. Historial de consultas
3. Exportación de datos (JSON, CSV, PDF)
"""
from .storage import guardar_historial, cargar_historial, limpiar_historial, storage_main