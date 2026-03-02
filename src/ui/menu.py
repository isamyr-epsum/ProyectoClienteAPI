"""
Interfaz gráfica con Tkinter - Menú de la aplicación
Autor: Todo el equipo
Sprint 2 - Febrero 2025

Implementa el menú principal y todos los submenús de la aplicación
"""

import tkinter as tk
from tkinter import messagebox


class AplicacionClima:
    def __init__(self, root):
        """Inicializa la ventana principal de la app"""
        self.root = root
        self.root.title("DataClima - Aplicación Meteorológica")
        self.root.geometry("700x600")

        # Intentar cargar imagen de fondo
        self.cargar_fondo()

        # Variable para guardar la última consulta
        self.ultima_consulta = None

        # Mostrar el menú principal
        self.mostrar_menu_principal()

    def cargar_fondo(self):
        """Carga la imagen de fondo si existe"""
        try:
            from PIL import Image, ImageTk

            # Cargar imagen
            imagen = Image.open("dataclima.jpg")

            # Redimensionar al tamaño de la ventana
            imagen = imagen.resize((700, 600), Image.Resampling.LANCZOS)

            # Convertir para usar en tkinter
            self.fondo_imagen = ImageTk.PhotoImage(imagen)

            # Crear label con la imagen de fondo
            self.label_fondo = tk.Label(self.root, image=self.fondo_imagen)
            self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

            print("✓ Imagen de fondo cargada")

        except FileNotFoundError:
            print("⚠ No se encontró 'dataclima.jpg' - usando color de fondo")
            self.root.configure(bg="#e3f2fd")
            self.label_fondo = None

        except ImportError:
            print("⚠ Pillow no instalado - usando color de fondo")
            self.root.configure(bg="#e3f2fd")
            self.label_fondo = None

        except Exception as e:
            print(f"⚠ Error al cargar imagen: {e}")
            self.root.configure(bg="#e3f2fd")
            self.label_fondo = None

    def limpiar_ventana(self):
        """Limpia todos los widgets pero mantiene el fondo"""
        for widget in self.root.winfo_children():
            # No eliminar el fondo
            if widget != self.label_fondo:
                widget.destroy()

    def recrear_fondo(self):
        """Vuelve a poner el fondo después de limpiar"""
        if self.label_fondo is not None and hasattr(self, 'fondo_imagen'):
            self.label_fondo = tk.Label(self.root, image=self.fondo_imagen)
            self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    def mostrar_menu_principal(self):
        """Muestra el menú principal con 4 opciones"""
        self.limpiar_ventana()
        self.recrear_fondo()

        # Nombre de la aplicación
        nombre_app = tk.Label(
            self.root,
            text="DATACLIMA",
            font=("Arial", 28, "bold"),
            fg="#1976D2"
        )
        nombre_app.pack(pady=15)

        # Subtítulo
        subtitulo = tk.Label(
            self.root,
            text="Consulta Meteorológica en Tiempo Real",
            font=("Arial", 12),
            fg="#424242"
        )
        subtitulo.pack(pady=5)

        # Título del menú
        titulo = tk.Label(
            self.root,
            text="MENÚ PRINCIPAL",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        # Frame para los botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        # Botón 1: Consultas
        tk.Button(
            frame_botones,
            text="1. Consultas",
            font=("Arial", 14),
            width=22,
            height=2,
            command=self.menu_consultas,
            bg="#4CAF50",
            fg="white",
            cursor="hand2",
            bd=0
        ).pack(pady=8)

        # Botón 2: Historial
        tk.Button(
            frame_botones,
            text="2. Historial",
            font=("Arial", 14),
            width=22,
            height=2,
            command=self.menu_historial,
            bg="#2196F3",
            fg="white",
            cursor="hand2",
            bd=0
        ).pack(pady=8)

        # Botón 3: Exportar datos
        tk.Button(
            frame_botones,
            text="3. Exportar datos",
            font=("Arial", 14),
            width=22,
            height=2,
            command=self.menu_exportar,
            bg="#FF9800",
            fg="white",
            cursor="hand2",
            bd=0
        ).pack(pady=8)

        # Botón 4: Salir
        tk.Button(
            frame_botones,
            text="4. Salir",
            font=("Arial", 14),
            width=22,
            height=2,
            command=self.salir,
            bg="#f44336",
            fg="white",
            cursor="hand2",
            bd=0
        ).pack(pady=8)

    def menu_consultas(self):
        """Submenú de consultas"""
        self.limpiar_ventana()
        self.recrear_fondo()

        tk.Label(
            self.root,
            text="CONSULTAS",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Opciones del submenú
        opciones = [
            ("1. Ver clima actual", self.ver_clima),
            ("2. Ver pronóstico 5 días", self.ver_pronostico),
            ("3. Ver calidad del aire", self.ver_calidad_aire),
            ("4. Volver al menú", self.mostrar_menu_principal)
        ]

        for texto, comando in opciones:
            tk.Button(
                frame,
                text=texto,
                font=("Arial", 12),
                width=28,
                height=2,
                command=comando,
                bg="#4CAF50",
                fg="white",
                cursor="hand2",
                bd=0
            ).pack(pady=8)

    def ver_clima(self):
        """Ventana para consultar clima actual"""
        self.limpiar_ventana()
        self.recrear_fondo()

        tk.Label(
            self.root,
            text="CONSULTAR CLIMA ACTUAL",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="Ingresa la ciudad:",
            font=("Arial", 12)
        ).pack(pady=10)

        # Campo de entrada
        entrada_ciudad = tk.Entry(self.root, font=("Arial", 14), width=30)
        entrada_ciudad.pack(pady=10)
        entrada_ciudad.focus()

        def consultar():
            ciudad = entrada_ciudad.get().strip()
            if not ciudad:
                messagebox.showwarning("Advertencia", "Debes ingresar una ciudad")
                return

            # ========== IMPLEMENTACIÓN ==========
            try:
                from src.api.weather_api import obtener_clima_actual
                from src.logic.validator import validar_ciudad, validar_clima_actual
                from src.logic.data_analyzer import analizar_datos
                from src.data.storage import guardar_historial
                from src.api.cache_manager import guardar_en_cache

                # 1. Validar ciudad
                valido, msg = validar_ciudad(ciudad)
                if not valido:
                    messagebox.showerror("Error de validación", msg)
                    return

                # 2. Obtener clima
                clima = obtener_clima_actual(ciudad)

                # 3. Validar datos recibidos
                valido, msg = validar_clima_actual(clima)
                if not valido:
                    messagebox.showerror("Error", msg)
                    return

                # 4. Mostrar resultado
                resultado = f"""
                            {clima['Ubicación']}
                            
                            {clima['Temperatura']}
                            {clima['Clima']}
                            Humedad: {clima['Humedad']}
                            Presión: {clima['Presión']}
                            Viento: {clima['Viento']}
                            
                            Amanecer: {clima['Amanecer']}
                            Atardecer: {clima['Atardecer']}
                            
                            {clima['Última actualización']}
                """
                messagebox.showinfo("Clima Actual", resultado)

                # 5. Guardar en caché e historial
                consulta = "Clima actual"
                guardar_en_cache(ciudad, consulta, clima)

                # 6. Analizar datos
                clima_analizado = analizar_datos(clima)
                guardar_historial(ciudad, consulta, clima_analizado)

                # 7. Guardar consulta
                self.ultima_consulta = {
                    "tipo": "clima",
                    "ciudad": ciudad,
                    "datos": clima,
                    "consulta": consulta
                }

            except Exception as e:
                messagebox.showerror("Error", f"Error al consultar: {str(e)}")
                return
            # ========== FIN IMPLEMENTACIÓN ==========

            # Preguntar si quiere gráfica
            self.preguntar_generar_grafica()

        tk.Button(
            self.root,
            text="Consultar",
            font=("Arial", 12),
            command=consultar,
            bg="#4CAF50",
            fg="white",
            width=15,
            cursor="hand2",
            bd=0
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Volver",
            font=("Arial", 10),
            command=self.menu_consultas,
            bg="#9E9E9E",
            fg="white",
            cursor="hand2",
            bd=0
        ).pack(pady=10)

    def ver_pronostico(self):
        """Ventana para ver pronóstico"""
        self.limpiar_ventana()
        self.recrear_fondo()

        tk.Label(
            self.root,
            text="PRONÓSTICO 5 DÍAS",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="Ingresa la ciudad:",
            font=("Arial", 12)
        ).pack(pady=10)

        entrada_ciudad = tk.Entry(self.root, font=("Arial", 14), width=30)
        entrada_ciudad.pack(pady=10)
        entrada_ciudad.focus()

        def consultar_pronostico():
            ciudad = entrada_ciudad.get().strip()
            if not ciudad:
                messagebox.showwarning("Advertencia", "Debes ingresar una ciudad")
                return

            # ========== IMPLEMENTACIÓN ==========
            try:
                from src.api.weather_api import darPronosticos
                from src.logic.validator import validar_ciudad, validar_pronostico
                from src.data.storage import guardar_historial
                from src.api.cache_manager import guardar_en_cache

                # 1. Validar ciudad
                valido, msg = validar_ciudad(ciudad)
                if not valido:
                    messagebox.showerror("Error de validación", msg)
                    return

                # 2. Obtener pronóstico
                pronostico = darPronosticos(ciudad)

                # 3. Validar datos
                valido, msg = validar_pronostico(pronostico)
                if not valido:
                    messagebox.showerror("Error", msg)
                    return

                # 4. Mostrar pronóstico
                resultado = f"Pronóstico 5 días - {pronostico['Ciudad']}, {pronostico['País']}\n\n"

                for dia in pronostico['Pronóstico 5 dias']:
                    resultado += f"{dia['Fecha']}\n"
                    resultado += f"{dia['Temperatura mín']}°C - {dia['Temperatura máx']}°C\n"
                    resultado += f"{dia['Descripción']}\n"
                    resultado += f"Humedad: {dia['Promedio Humedad']}%\n"
                    resultado += f"Lluvia: {dia['Probabilidad de lluvia']}%\n\n"

                resultado += f"{pronostico['Última actualización']}"

                messagebox.showinfo("Pronóstico 5 Días", resultado)

                # 5. Guardar en caché e historial
                consulta = "Pronostico 5 dias"
                guardar_en_cache(ciudad, consulta, pronostico)
                guardar_historial(ciudad, consulta, pronostico)

                # 6. Guardar consulta
                self.ultima_consulta = {
                    "tipo": "pronostico",
                    "ciudad": ciudad,
                    "datos": pronostico,
                    "consulta": consulta
                }

            except Exception as e:
                messagebox.showerror("Error", f"Error al consultar: {str(e)}")
                return
            # ========== FIN IMPLEMENTACIÓN ==========

            self.preguntar_generar_grafica()

        tk.Button(
            self.root,
            text="Consultar Pronóstico",
            font=("Arial", 12),
            command=consultar_pronostico,
            bg="#2196F3",
            fg="white",
            width=20,
            cursor="hand2",
            bd=0
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Volver",
            font=("Arial", 10),
            command=self.menu_consultas,
            bg="#9E9E9E",
            fg="white",
            cursor="hand2",
            bd=0
        ).pack(pady=10)

    def ver_calidad_aire(self):
        """Ventana para ver calidad del aire"""
        self.limpiar_ventana()
        self.recrear_fondo()

        tk.Label(
            self.root,
            text="CALIDAD DEL AIRE",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="Ingresa la ciudad:",
            font=("Arial", 12)
        ).pack(pady=10)

        entrada_ciudad = tk.Entry(self.root, font=("Arial", 14), width=30)
        entrada_ciudad.pack(pady=10)
        entrada_ciudad.focus()

        def consultar_aire():
            ciudad = entrada_ciudad.get().strip()
            if not ciudad:
                messagebox.showwarning("Advertencia", "Debes ingresar una ciudad")
                return

            #implementar
            try:
                from src.api.weather_api import calidadAire
                from src.logic.validator import validar_ciudad, validar_calidad_aire
                from src.data.storage import guardar_historial
                from src.api.cache_manager import guardar_en_cache

                # Validar ciudad
                valido, msg = validar_ciudad(ciudad)
                if not valido:
                    messagebox.showerror("Error de validación", msg)
                    return

                #Obtener calidad del aire
                calidad = calidadAire(ciudad)

                #Validar datos
                valido, msg = validar_calidad_aire(calidad)
                if not valido:
                    messagebox.showerror("Error", msg)
                    return

                #Mostrar resultado
                aire = calidad["Calidad de aire"]
                componentes = aire["Componentes"]

                resultado = f"""
                Calidad del Aire - {calidad['Ciudad']}, {calidad['País']}
                
                Índice: {aire['Índice']} - {aire['Descripción']}
                
                {aire['Pronóstico']}
                
                Componentes:
                   • CO: {componentes['CO (monóxido de carbono)']} μg/m³
                   • NO₂: {componentes['NO₂ (dióxido de nitrógeno)']} μg/m³
                   • O₃: {componentes['O₃ (ozono)']} μg/m³
                   • PM₂.₅: {componentes['PM₂.₅ (partículas finas)']} μg/m³
                   • PM₁₀: {componentes['PM₁₀ (partículas gruesas)']} μg/m³
                
                {calidad['Última actualización']}
                """
                messagebox.showinfo("Calidad del Aire", resultado)

                #Guardar en caché e historial
                consulta = "Calidad aire"
                guardar_en_cache(ciudad, consulta, calidad)
                guardar_historial(ciudad, consulta, calidad)

                #Guardar consulta
                self.ultima_consulta = {
                    "tipo": "aire",
                    "ciudad": ciudad,
                    "datos": calidad,
                    "consulta": consulta
                }

            except Exception as e:
                messagebox.showerror("Error", f"Error al consultar: {str(e)}")
                return
                #fin implementar codigo

            self.preguntar_generar_grafica()

        tk.Button(
            self.root,
            text="Consultar Calidad",
            font=("Arial", 12),
            command=consultar_aire,
            bg="#4CAF50",
            fg="white",
            width=18,
            cursor="hand2",
            bd=0
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Volver",
            font=("Arial", 10),
            command=self.menu_consultas,
            bg="#9E9E9E",
            fg="white",
            cursor="hand2",
            bd=0
        ).pack(pady=10)

    def preguntar_generar_grafica(self):
        """Pregunta si quiere generar gráfica"""
        respuesta = messagebox.askyesno(
            "Generar Gráfica",
            "¿Deseas generar una gráfica con estos datos?"
        )

        if respuesta:
            self.generar_grafica()
        else:
            self.preguntar_exportar()

    def generar_grafica(self):
        """Genera la gráfica"""
        try:
            from src.ui.visualizer import graficar_clima_actual, graficar_pronostico

            if self.ultima_consulta["tipo"] == "clima":
                # Extraer temperatura
                temp_str = self.ultima_consulta["datos"]["Temperatura"]
                temp = float(temp_str.split("°C")[0])
                ciudad = self.ultima_consulta["ciudad"]
                graficar_clima_actual(temp, ciudad)

            elif self.ultima_consulta["tipo"] == "pronostico":
                datos = self.ultima_consulta["datos"]
                ciudad = self.ultima_consulta["ciudad"]
                graficar_pronostico(datos, ciudad)

            else:
                messagebox.showinfo("Gráfica", "No hay gráfica disponible para calidad del aire")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar la gráfica: {str(e)}")
        # ========== FIN IMPLEMENTACIÓN ==========

        self.preguntar_exportar()

    def preguntar_exportar(self):
        """Pregunta si quiere exportar"""
        respuesta = messagebox.askyesno(
            "Exportar",
            "¿Deseas exportar estos datos?"
        )

        if respuesta:
            self.menu_exportar_formato()
        else:
            self.mostrar_menu_principal()

    def menu_exportar_formato(self):
        """Submenú para elegir formato de exportación"""
        self.limpiar_ventana()
        self.recrear_fondo()

        tk.Label(
            self.root,
            text="EXPORTAR DATOS",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="Selecciona el formato:",
            font=("Arial", 12)
        ).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        opciones = [
            ("1. JSON", lambda: self.exportar("JSON")),
            ("2. PDF", lambda: self.exportar("PDF")),
            ("3. CSV", lambda: self.exportar("CSV")),
            ("4. Volver al menú", self.mostrar_menu_principal)
        ]

        for texto, comando in opciones:
            tk.Button(
                frame,
                text=texto,
                font=("Arial", 12),
                width=22,
                height=2,
                command=comando,
                bg="#FF9800",
                fg="white",
                cursor="hand2",
                bd=0
            ).pack(pady=8)

    def exportar(self, formato):
        """Exporta los datos en el formato elegido"""

        try:
            from src.ui.exporter import exportar_json, exportar_csv, exportar_pdf

            if self.ultima_consulta is None:
                messagebox.showwarning("Advertencia", "No hay datos para exportar")
                self.mostrar_menu_principal()
                return

            # Obtener datos
            consulta = self.ultima_consulta["consulta"]
            ciudad = self.ultima_consulta["ciudad"]
            datos = self.ultima_consulta["datos"]

            # Exportar según formato
            if formato == "JSON":
                exportar_json(consulta, ciudad, datos)
            elif formato == "CSV":
                exportar_csv(consulta, ciudad, datos)
            elif formato == "PDF":
                exportar_pdf(consulta, ciudad, datos)

            messagebox.showinfo("Éxito", f"Datos exportados en formato {formato}")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar: {str(e)}")


        self.mostrar_menu_principal()

    def menu_historial(self):
        """Submenú de historial"""
        self.limpiar_ventana()
        self.recrear_fondo()

        tk.Label(
            self.root,
            text="HISTORIAL",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        opciones = [
            ("1. Ver historial", self.ver_historial),
            ("2. Ver estadísticas", self.ver_estadisticas),
            ("3. Eliminar historial", self.eliminar_historial),
            ("4. Volver al menú", self.mostrar_menu_principal)
        ]

        for texto, comando in opciones:
            tk.Button(
                frame,
                text=texto,
                font=("Arial", 12),
                width=28,
                height=2,
                command=comando,
                bg="#2196F3",
                fg="white",
                cursor="hand2",
                bd=0
            ).pack(pady=8)

    def ver_historial(self):
        """Muestra el historial"""

        try:
            from src.data.storage import cargar_historial

            historial = cargar_historial()

            if not historial or len(historial) == 0:
                messagebox.showinfo("Historial", "No hay consultas guardadas")
                self.menu_historial()
                return

            # Mostrar últimas 10
            resultado = "📋 HISTORIAL (últimas 10 consultas)\n\n"
            for i, consulta in enumerate(historial[-10:], 1):
                resultado += f"{i}. {consulta.get('ciudad', 'Sin ciudad')}\n"
                resultado += f"   Tipo: {consulta.get('consulta', 'Sin tipo')}\n"
                resultado += f"   Fecha: {consulta.get('fecha', 'Sin fecha')}\n\n"

            messagebox.showinfo("Historial", resultado)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el historial: {str(e)}")
        # ========== FIN IMPLEMENTACIÓN ==========

        self.menu_historial()

    def ver_estadisticas(self):
        """Muestra estadísticas del historial"""
        try:
            from src.data.storage import cargar_historial
            from src.logic.data_analyzer import calcular_estadisticas

            historial = cargar_historial()

            if not historial or len(historial) == 0:
                messagebox.showinfo("Estadísticas", "No hay datos para analizar")
                self.menu_historial()
                return

            stats = calcular_estadisticas(historial)

            resultado = f"""
            ESTADÍSTICAS DEL HISTORIAL
            
            Total consultas: {stats['total_consultas']}
            
            Temperaturas:
               • Media: {stats['temperatura_media']}°C
               • Máxima: {stats['temperatura_maxima']}°C
               • Mínima: {stats['temperatura_minima']}°C
            
            Humedad media: {stats['humedad_media']}%
            
            Ciudades consultadas: {len(stats['ciudades_consultadas'])}
               Ciudad más consultada: {stats['ciudad_mas_consultada']}
            """
            messagebox.showinfo("Estadísticas", resultado)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron calcular estadísticas: {str(e)}")
        # ========== FIN IMPLEMENTACIÓN ==========

        self.menu_historial()

    def eliminar_historial(self):
        """Elimina el historial"""
        respuesta = messagebox.askyesno(
            "Confirmar",
            "¿Estás seguro de eliminar todo el historial?"
        )

        if respuesta:
            # ========== IMPLEMENTACIÓN ==========
            try:
                from src.data.storage import limpiar_historial

                limpiar_historial()
                messagebox.showinfo("Éxito", "Historial eliminado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar: {str(e)}")
            # ========== FIN IMPLEMENTACIÓN ==========

        self.menu_historial()

    def menu_exportar(self):
        """Menú de exportar datos"""
        self.menu_exportar_formato()

    def salir(self):
        """Cierra la aplicación"""
        respuesta = messagebox.askyesno("Salir", "¿Estás seguro de salir?")
        if respuesta:
            self.root.quit()


# Ejecutar la aplicación
def mostrar_menu_principal():
    root = tk.Tk()
    AplicacionClima(root)
    root.mainloop()


if __name__ == "__main__":
    mostrar_menu_principal()