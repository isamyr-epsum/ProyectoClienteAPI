"""
Módulo UI (interfaz de Usuario)- Capa de Presentación (Aqui es donde se mete lo visual)
Hará;
1. Interfaz de línea de comandos (CLI)
2. Generación de gráficas
3. Exportación de reportes visuales
"""
from .exporter import exportar_csv, exportar_pdf, exportar_json, exporter_main, exporter_main_consulta
from .menu import mostrar_menu_principal, obtener_opcion_usuario
from .visualizer import graficar_clima_actual, graficar_pronostico