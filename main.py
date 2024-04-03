import tkinter as tk
from tkinter import filedialog
from lista_maquetas import ListaMaquetas
from archivo import leer_archivo_xml
import graphviz
import os

class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Menú Principal")
        self.ventana.configure(bg="#B4D4FF") 
        self.ventana.geometry("400x400")
        self.lista_maquetas = ListaMaquetas()
        self.directorio_proyecto = os.getcwd()
        self.archivo_leido = False
        self.crear_interfaz()

    def crear_interfaz(self):
        # Label de Bienvenido
        self.label_bienvenido = tk.Label(self.ventana, text="Bienvenido", bg="#B4D4FF", font=("Verdana", 20))
        self.label_bienvenido.pack(pady=20)

        # Botón para abrir archivo
        self.boton_abrir = tk.Button(self.ventana, text="Abrir archivo", command=self.abrir_archivo, width=15)
        self.boton_abrir.pack(pady=10)

        # Label para archivo leído correctamente
        self.label_archivo_leido = tk.Label(self.ventana, text="", bg="#B4D4FF", font=("Verdana", 12))
        self.label_archivo_leido.pack(pady=10)

        # Label para gestionar maquetas
        self.label_gestion_maquetas = tk.Label(self.ventana, text="Gestionar Maquetas", bg="#B4D4FF", font=("Verdana", 12))
        self.label_gestion_maquetas.pack(pady=10)

        # Selector de opciones
        self.selector_opciones = tk.StringVar()
        self.selector_opciones.set("Seleccionar") 
        opciones = ["Ver gráficamente", "Ver listado"]
        self.menu_selector = tk.OptionMenu(self.ventana, self.selector_opciones, *opciones, command=self.gestionar_maquetas)
        self.menu_selector.config(width=15)
        self.menu_selector.pack(pady=5)

        # Botón de ayuda
        self.boton_ayuda = tk.Button(self.ventana, text="Ayuda", command=self.mostrar_ayuda, width=15)
        self.boton_ayuda.pack(pady=10)

        # Botón para salir
        self.boton_salir = tk.Button(self.ventana, text="Salir", command=self.salir, width=15)
        self.boton_salir.pack(pady=10)

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivo XML", "*.xml")])
        if archivo:  # Se verifica si se seleccionó un archivo
            self.lista_maquetas = leer_archivo_xml(archivo)
            self.lista_maquetas.ordenar_alfabeticamente()  # Ordenar las maquetas alfabéticamente
            self.archivo_leido_correctamente()

    def archivo_leido_correctamente(self):
        # Función para mostrar el mensaje de archivo leído correctamente
        self.label_archivo_leido.config(text="Archivo leído correctamente")
        self.archivo_leido = True

    def gestionar_maquetas(self, event=None):
        if not self.archivo_leido:
            tk.messagebox.showwarning("Error", "No se ha ingresado ningún archivo.")
            return

        opcion = self.selector_opciones.get()
        if opcion == "Ver gráficamente":
            self.ver_graficamente()
        elif opcion == "Ver listado":
            self.ver_maquetas()

    def ver_maquetas(self):
        ventana_listado_maquetas = tk.Toplevel(self.ventana)
        ventana_listado_maquetas.title("Listado de Maquetas")
        ventana_listado_maquetas.configure(bg="#B4D4FF")
        ventana_listado_maquetas.geometry("400x400")

        text_area = tk.Text(ventana_listado_maquetas, width=50, height=20)
        text_area.pack(pady=10)

        nodo_actual = self.lista_maquetas.cabeza
        while nodo_actual:
            maq = nodo_actual.maqueta
            text_area.insert(tk.END, f"Nombre: {maq.nombre}\n")
            text_area.insert(tk.END, f"Filas: {maq.filas}\n")
            text_area.insert(tk.END, f"Columnas: {maq.columnas}\n")
            text_area.insert(tk.END, f"Entrada: {maq.entrada}\n")
            text_area.insert(tk.END, "Objetivos:\n")
            objetivo_actual = maq.primer_objetivo  # Comenzar desde el primer objetivo
            while objetivo_actual:
                text_area.insert(tk.END, f"  Nombre: {objetivo_actual.nombre}, Fila: {objetivo_actual.fila}, Columna: {objetivo_actual.columna}\n")
                objetivo_actual = objetivo_actual.siguiente  # Avanzar al siguiente objetivo
            text_area.insert(tk.END, f"Estructura: {maq.estructura}\n\n")
            nodo_actual = nodo_actual.siguiente

    def ver_graficamente(self):
        pass

    def mostrar_ayuda(self):
        pass

    def salir(self):
        self.ventana.quit()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaPrincipal(ventana)
    ventana.mainloop()