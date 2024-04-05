import tkinter as tk
from tkinter import filedialog, messagebox
from lista_maquetas import ListaMaquetas
from archivo import leer_archivo_xml
from graphviz import Digraph
import os
from xml.etree import ElementTree as ET
from maqueta import Maqueta

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

        # Botón cargar otro archivo
        self.boton_cargar_otro = tk.Button(self.ventana, text="Cargar otro archivo", command=self.abrir_archivo, width=15)
        self.boton_cargar_otro.pack(pady=10)

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
    
    def mostrar_opcion_cargar_otro(self):
        # Mostrar opción para cargar otro archivo
        self.boton_cargar_otro = tk.Button(self.ventana, text="Cargar otro archivo", command=self.abrir_archivo, width=15)
        self.boton_cargar_otro.pack(pady=10)

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

    def parsear_archivo_xml(self, archivo):
        lista_maquetas = ListaMaquetas()
        tree = ET.parse(archivo)
        root = tree.getroot()
        for maqueta_xml in root.findall('maquetas/maqueta'):
            nombre = maqueta_xml.find('nombre').text.strip()
            filas = int(maqueta_xml.find('filas').text.strip())
            columnas = int(maqueta_xml.find('columnas').text.strip())
            entrada = (
                int(maqueta_xml.find('entrada/fila').text.strip()),
                int(maqueta_xml.find('entrada/columna').text.strip())
            )
            estructura = maqueta_xml.find('estructura').text.strip()
            maqueta = Maqueta(nombre, filas, columnas, entrada, estructura)
            objetivos_xml = maqueta_xml.find('objetivos')
            for objetivo_xml in objetivos_xml.findall('objetivo'):
                nombre_obj = objetivo_xml.find('nombre').text.strip()
                fila_obj = int(objetivo_xml.find('fila').text.strip())
                col_obj = int(objetivo_xml.find('columna').text.strip())
                maqueta.agregar_objetivo(nombre_obj, fila_obj, col_obj)
            lista_maquetas.agregar_maq(maqueta)
        return lista_maquetas

    def generate_table(self, patron_data, R, C, cell_width, cell_height):
        table = ""
        for i in range(R):
            table += "<TR>"
            for j in range(C):
                color = '#FFFFFF' if patron_data[i * C + j] == '-' else '#000000'
                table += f'<TD WIDTH="{cell_width}px" HEIGHT="{cell_height}px" BGCOLOR="{color}" BORDER="0"></TD>'
            table += "</TR>"
        return table

    def ver_graficamente(self):
        cell_width = 30  # Ancho de celda 
        cell_height = 26  # Alto de celda 
        maqueta_actual = self.lista_maquetas.cabeza
        while maqueta_actual:
            maqueta = maqueta_actual.maqueta
            patron_data = maqueta.estructura.replace('*', 'B').replace('-', '-')
            R, C = maqueta.filas, maqueta.columnas
            dot = Digraph(comment='Patrón')
            dot.node('tab', label=f'<<TABLE>{self.generate_table(patron_data, R, C, cell_width, cell_height)}</TABLE>>', shape='none')
            dot.render(f'{maqueta.nombre}_patron', format='png', cleanup=True)
            print(f"El patrón de la maqueta {maqueta.nombre} se ha mostrado gráficamente.")
            maqueta_actual = maqueta_actual.siguiente

    def mostrar_ayuda(self):
        pass

    def salir(self):
        self.ventana.quit()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaPrincipal(ventana)
    ventana.mainloop()