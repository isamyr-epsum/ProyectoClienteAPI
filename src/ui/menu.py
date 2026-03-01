"""
mostrar menú principal, capturar entrada del usuario, gestionar navegación entre opciones



def mostrar_menu_principal():PRIMERA PROPUESTA DE MOSTRAR EL MENU

    print("\n"+ "========================================")
    print(" APLICACIÓN DE CONSULTA METEOROLÓGICA")
    print("1. Consultar clima actual")
    print("2. Consultar pronóstico")
    print("3. Ver historial")
    print("4. Exportar datos")
    print("5. Salir")


# capturar la opcion selecciona por el usuario, retorna la opcion elegida
def obtener_opcion_usuario():
  #continuar validación en Sprint 2
    return input("Selecciona una opción: ")

"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json


class AplicacionClima:
    def __init__(self, root):
        """Inicializa la ventana principal"""
        self.root = root
        self.root.title("Aplicación de Consulta Meteorológica")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")

        # Variable para almacenar datos de la última consulta
        self.ultima_consulta = None

        # Mostrar menú principal
        self.mostrar_menu_principal()

    def limpiar_ventana(self):
        """Limpia todos los widgets de la ventana"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_menu_principal(self):
        """Muestra el menú principal con 4 opciones"""
        self.limpiar_ventana()

        # Título
        titulo = tk.Label(
            self.root,
            text="MENÚ PRINCIPAL",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0"
        )
        titulo.pack(pady=30)

        # Frame para los botones
        frame_botones = tk.Frame(self.root, bg="#f0f0f0")
        frame_botones.pack(pady=20)

        # Botón 1: Consultas
        btn_consultas = tk.Button(
            frame_botones,
            text="1. Consultas",
            font=("Arial", 14),
            width=20,
            height=2,
            command=self.menu_consultas,
            bg="#4CAF50",
            fg="white",
            cursor="hand2"
        )
        btn_consultas.pack(pady=10)

        # Botón 2: Historial
        btn_historial = tk.Button(
            frame_botones,
            text="2. Historial",
            font=("Arial", 14),
            width=20,
            height=2,
            command=self.menu_historial,
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        )
        btn_historial.pack(pady=10)

        # Botón 3: Exportar datos cache
        btn_exportar = tk.Button(
            frame_botones,
            text="3. Exportar datos cache",
            font=("Arial", 14),
            width=20,
            height=2,
            command=self.menu_exportar,
            bg="#FF9800",
            fg="white",
            cursor="hand2"
        )
        btn_exportar.pack(pady=10)

        # Botón 4: Salir
        btn_salir = tk.Button(
            frame_botones,
            text="4. Salir",
            font=("Arial", 14),
            width=20,
            height=2,
            command=self.salir,
            bg="#f44336",
            fg="white",
            cursor="hand2"
        )
        btn_salir.pack(pady=10)

    def menu_consultas(self):
        """Submenú de consultas"""
        self.limpiar_ventana()

        # Título
        titulo = tk.Label(
            self.root,
            text="CONSULTAS",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0"
        )
        titulo.pack(pady=20)

        # Frame para opciones
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(pady=10)

        # Opciones
        opciones = [
            ("1. Ver clima", self.ver_clima),
            ("2. Ver pronóstico", self.ver_pronostico),
            ("3. Ver calidad aire", self.ver_calidad_aire),
            ("4. Volver al menú", self.mostrar_menu_principal)
        ]

        for texto, comando in opciones:
            btn = tk.Button(
                frame,
                text=texto,
                font=("Arial", 12),
                width=25,
                height=2,
                command=comando,
                bg="#4CAF50",
                fg="white",
                cursor="hand2"
            )
            btn.pack(pady=8)

    def ver_clima(self):
        """Ventana para ver clima actual"""
        self.limpiar_ventana()

        titulo = tk.Label(
            self.root,
            text="CONSULTAR CLIMA ACTUAL",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        )
        titulo.pack(pady=20)

        # Input ciudad
        tk.Label(self.root, text="Ingresa la ciudad:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

        entrada_ciudad = tk.Entry(self.root, font=("Arial", 14), width=30)
        entrada_ciudad.pack(pady=10)
        entrada_ciudad.focus()

        # Botón consultar
        def consultar():
            ciudad = entrada_ciudad.get().strip()
            if not ciudad:
                messagebox.showwarning("Advertencia", "Debes ingresar una ciudad")
                return

            # Aquí llamarías a tu función de weather_api.py
            # Por ahora simulo datos
            resultado = f"Clima de {ciudad}:\nTemperatura: 18°C\nHumedad: 65%\nEstado: Despejado"
            self.ultima_consulta = {"tipo": "clima", "ciudad": ciudad, "datos": resultado}

            # Preguntar si quiere generar gráfica
            self.preguntar_generar_grafica()

        btn_consultar = tk.Button(
            self.root,
            text="Consultar",
            font=("Arial", 12),
            command=consultar,
            bg="#4CAF50",
            fg="white",
            width=15,
            cursor="hand2"
        )
        btn_consultar.pack(pady=20)

        # Botón volver
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

        titulo = tk.Label(
            self.root,
            text="PRONÓSTICO 5 DÍAS",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        )
        titulo.pack(pady=20)

        tk.Label(self.root, text="Ingresa la ciudad:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

        entrada_ciudad = tk.Entry(self.root, font=("Arial", 14), width=30)
        entrada_ciudad.pack(pady=10)
        entrada_ciudad.focus()

        def consultar_pronostico():
            ciudad = entrada_ciudad.get().strip()
            if not ciudad:
                messagebox.showwarning("Advertencia", "Debes ingresar una ciudad")
                return

            # Aquí llamarías a weather_api.darPronosticos()
            resultado = f"Pronóstico de {ciudad} (5 días)\n\nDatos simulados..."
            self.ultima_consulta = {"tipo": "pronostico", "ciudad": ciudad, "datos": resultado}

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

        titulo = tk.Label(
            self.root,
            text="CALIDAD DEL AIRE",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        )
        titulo.pack(pady=20)

        tk.Label(self.root, text="Ingresa la ciudad:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

        entrada_ciudad = tk.Entry(self.root, font=("Arial", 14), width=30)
        entrada_ciudad.pack(pady=10)
        entrada_ciudad.focus()

        def consultar_aire():
            ciudad = entrada_ciudad.get().strip()
            if not ciudad:
                messagebox.showwarning("Advertencia", "Debes ingresar una ciudad")
                return

            # Aquí llamarías a weather_api.calidadAire()
            resultado = f"Calidad del aire en {ciudad}:\nÍndice: 2 (Buena)\n\nDatos simulados..."
            self.ultima_consulta = {"tipo": "aire", "ciudad": ciudad, "datos": resultado}

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
        """Genera la gráfica (simulado)"""
        messagebox.showinfo("Gráfica", "Generando gráfica...\n(Aquí llamarías a visualizer.py)")
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

        titulo = tk.Label(
            self.root,
            text="EXPORTAR DATOS",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        )
        titulo.pack(pady=20)

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
                width=20,
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
            f"Exportando datos en formato {formato}...\n(Aquí llamarías a exporter.py)"
        )
        self.mostrar_menu_principal()

    def menu_historial(self):
        """Submenú de historial"""
        self.limpiar_ventana()

        titulo = tk.Label(
            self.root,
            text="HISTORIAL",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0"
        )
        titulo.pack(pady=20)

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(pady=10)

        opciones = [
            ("1. Ver historial", self.ver_historial),
            ("2. Ver estadísticas del historial", self.ver_estadisticas),
            ("3. Eliminar historial", self.eliminar_historial),
            ("4. Volver al menú", self.mostrar_menu_principal)
        ]

        for texto, comando in opciones:
            tk.Button(
                frame,
                text=texto,
                font=("Arial", 12),
                width=30,
                height=2,
                command=comando,
                bg="#2196F3",
                fg="white",
                cursor="hand2"
            ).pack(pady=8)

    def ver_historial(self):
        """Muestra el historial"""
        messagebox.showinfo("Historial", "Aquí se mostraría el historial guardado\n(storage.py)")
        self.menu_historial()

    def ver_estadisticas(self):
        """Muestra estadísticas del historial"""
        messagebox.showinfo(
            "Estadísticas",
            "Aquí se mostrarían estadísticas\n(data_analyzer.calcular_estadisticas())"
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
        """Menú de exportar datos cache"""
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