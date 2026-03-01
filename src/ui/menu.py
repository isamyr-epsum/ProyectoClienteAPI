"""
mostrar menú principal, capturar entrada del usuario, gestionar navegación entre opciones

"""

"""
Interfaz gráfica con Tkinter - Menú de la aplicación
Autor: Todo el equipo
Sprint 2 - Febrero 2025

Implementa el menú principal y todos los submenús de la aplicación
"""

import tkinter as tk
from tkinter import messagebox

def mostrar_menu_principal():
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

            # mostrar el menú principal
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
                print("No se encontró 'dataclima.png' - usando color de fondo")
                self.root.configure(bg="#e3f2fd")
                self.label_fondo = None

            except ImportError:
                print("Pillow no instalado - usando color de fondo")
                print("Instala con: pip install Pillow")
                self.root.configure(bg="#e3f2fd")
                self.label_fondo = None

            except Exception as e:
                print(f"Error al cargar imagen: {e}")
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
                fg="#1976D2",

            )
            nombre_app.pack(pady=15)

            # Subtítulo
            subtitulo = tk.Label(
                self.root,
                text="Consulta Meteorológica en Tiempo Real",
                font=("Arial", 12),
                fg="#424242",
                bg="white",
                padx=10,
                pady=3
            )
            subtitulo.pack(pady=5)

            # Título del menú
            titulo = tk.Label(
                self.root,
                text="MENÚ PRINCIPAL",
                font=("Arial", 18, "bold"),
                bg="#f0f0f0"
            )
            titulo.pack(pady=15)

            # Frame para los botones
            frame_botones = tk.Frame(self.root, bg="#f0f0f0")
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
                cursor="hand2"
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
                cursor="hand2"
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
                cursor="hand2"
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
                cursor="hand2"
            ).pack(pady=8)

        def menu_consultas(self):
            """Submenú de consultas"""
            self.limpiar_ventana()
            self.recrear_fondo()

            tk.Label(
                self.root,
                text="CONSULTAS",
                font=("Arial", 18, "bold"),
                bg="#f0f0f0"
            ).pack(pady=20)

            frame = tk.Frame(self.root, bg="#f0f0f0")
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
                    cursor="hand2"
                ).pack(pady=8)

        def ver_clima(self):
            """Ventana para consultar clima actual"""
            self.limpiar_ventana()
            self.recrear_fondo()

            tk.Label(
                self.root,
                text="CONSULTAR CLIMA ACTUAL",
                font=("Arial", 16, "bold"),
                bg="#f0f0f0"
            ).pack(pady=20)

            tk.Label(
                self.root,
                text="Ingresa la ciudad:",
                font=("Arial", 12),
                bg="#f0f0f0"
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

                # Aquí se llamaría a weather_api.obtener_clima_actual(ciudad)
                messagebox.showinfo("Resultado", f"Consultando clima de {ciudad}...\n(Conectar con weather_api.py)")

                # Guardar consulta
                self.ultima_consulta = {"tipo": "clima", "ciudad": ciudad}

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
                cursor="hand2"
            ).pack(pady=20)

            tk.Button(
                self.root,
                text="Volver",
                font=("Arial", 10),
                command=self.menu_consultas,
                bg="#9E9E9E",
                fg="white",
                cursor="hand2"
            ).pack(pady=10)

        def ver_pronostico(self):
            """Ventana para ver pronóstico"""
            self.limpiar_ventana()
            self.recrear_fondo()

            tk.Label(
                self.root,
                text="PRONÓSTICO 5 DÍAS",
                font=("Arial", 16, "bold"),
                bg="#f0f0f0"
            ).pack(pady=20)

            tk.Label(
                self.root,
                text="Ingresa la ciudad:",
                font=("Arial", 12),
                bg="#f0f0f0"
            ).pack(pady=10)

            entrada_ciudad = tk.Entry(self.root, font=("Arial", 14), width=30)
            entrada_ciudad.pack(pady=10)
            entrada_ciudad.focus()

            def consultar_pronostico():
                ciudad = entrada_ciudad.get().strip()
                if not ciudad:
                    messagebox.showwarning("Advertencia", "Debes ingresar una ciudad")
                    return

                # Aquí se llamaría a weather_api.darPronosticos(ciudad)
                messagebox.showinfo("Resultado", f"Consultando pronóstico de {ciudad}...\n(Conectar con weather_api.py)")

                self.ultima_consulta = {"tipo": "pronostico", "ciudad": ciudad}
                self.preguntar_generar_grafica()

            tk.Button(
                self.root,
                text="Consultar Pronóstico",
                font=("Arial", 12),
                command=consultar_pronostico,
                bg="#2196F3",
                fg="white",
                width=20,
                cursor="hand2"
            ).pack(pady=20)

            tk.Button(
                self.root,
                text="Volver",
                font=("Arial", 10),
                command=self.menu_consultas,
                bg="#9E9E9E",
                fg="white",
                cursor="hand2"
            ).pack(pady=10)

        def ver_calidad_aire(self):
            """Ventana para ver calidad del aire"""
            self.limpiar_ventana()
            self.recrear_fondo()

            tk.Label(
                self.root,
                text="CALIDAD DEL AIRE",
                font=("Arial", 16, "bold"),
                bg="#f0f0f0"
            ).pack(pady=20)

            tk.Label(
                self.root,
                text="Ingresa la ciudad:",
                font=("Arial", 12),
                bg="#f0f0f0"
            ).pack(pady=10)

            entrada_ciudad = tk.Entry(self.root, font=("Arial", 14), width=30)
            entrada_ciudad.pack(pady=10)
            entrada_ciudad.focus()

            def consultar_aire():
                ciudad = entrada_ciudad.get().strip()
                if not ciudad:
                    messagebox.showwarning("Advertencia", "Debes ingresar una ciudad")
                    return

                # Aquí se llamaría a weather_api.calidadAire(ciudad)
                messagebox.showinfo("Resultado",
                                    f"Consultando calidad del aire en {ciudad}...\n(Conectar con weather_api.py)")

                self.ultima_consulta = {"tipo": "aire", "ciudad": ciudad}
                self.preguntar_generar_grafica()

            tk.Button(
                self.root,
                text="Consultar Calidad",
                font=("Arial", 12),
                command=consultar_aire,
                bg="#4CAF50",
                fg="white",
                width=18,
                cursor="hand2"
            ).pack(pady=20)

            tk.Button(
                self.root,
                text="Volver",
                font=("Arial", 10),
                command=self.menu_consultas,
                bg="#9E9E9E",
                fg="white",
                cursor="hand2"
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
            messagebox.showinfo(
                "Gráfica",
                "Generando gráfica...\n(Aquí se llamaría a visualizer.py)"
            )
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
                font=("Arial", 16, "bold"),
                bg="#f0f0f0"
            ).pack(pady=20)

            tk.Label(
                self.root,
                text="Selecciona el formato:",
                font=("Arial", 12),
                bg="#f0f0f0"
            ).pack(pady=10)

            frame = tk.Frame(self.root, bg="#f0f0f0")
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
                    cursor="hand2"
                ).pack(pady=8)

        def exportar(self, formato):
            """Exporta los datos en el formato elegido"""
            messagebox.showinfo(
                "Exportar",
                f"Exportando en formato {formato}...\n(Aquí se llamaría a exporter.py)"
            )
            self.mostrar_menu_principal()

        def menu_historial(self):
            """Submenú de historial"""
            self.limpiar_ventana()
            self.recrear_fondo()

            tk.Label(
                self.root,
                text="HISTORIAL",
                font=("Arial", 18, "bold"),
                bg="#f0f0f0"
            ).pack(pady=20)

            frame = tk.Frame(self.root, bg="#f0f0f0")
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
                    cursor="hand2"
                ).pack(pady=8)

        def ver_historial(self):
            """Muestra el historial"""
            messagebox.showinfo(
                "Historial",
                "Aquí se mostraría el historial\n(Conectar con storage.py)"
            )
            self.menu_historial()

        def ver_estadisticas(self):
            """Muestra estadísticas del historial"""
            messagebox.showinfo(
                "Estadísticas",
                "Aquí se mostrarían estadísticas\n(Conectar con data_analyzer.calcular_estadisticas())"
            )
            self.menu_historial()

        def eliminar_historial(self):
            """Elimina el historial"""
            respuesta = messagebox.askyesno(
                "Confirmar",
                "¿Estás seguro de eliminar todo el historial?"
            )
            if respuesta:
                messagebox.showinfo("Historial", "Historial eliminado")
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
    if __name__ == "__main__":
        root = tk.Tk()
        app = AplicacionClima(root)
        root.mainloop()