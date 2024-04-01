import tkinter as tk
from tkinter import filedialog
from lista_maquetas import ListaMaquetas
from archivo import leer_archivo_xml
import graphviz

class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Menú Principal")
        self.ventana.configure(bg="#B4D4FF") 
        self.ventana.geometry("400x290")
        self.lista_maquetas = ListaMaquetas()
        self.crear_interfaz()

    def crear_interfaz(self):
        # Label de Bienvenido
        self.label_bienvenido = tk.Label(self.ventana, text="Bienvenido", bg="#B4D4FF", font=("Verdana", 20))
        self.label_bienvenido.pack(pady=20)

        # Label de Subir archivo
        self.label_archivo = tk.Label(self.ventana, text="Para resolver maquetas\ndebes abrir el archivo XML primero", bg="#B4D4FF", font=("Verdana", 12))
        self.label_archivo.pack(pady=10)

        # Contenedor para los botones
        self.frame_botones = tk.Frame(self.ventana, bg="#B4D4FF")
        self.frame_botones.pack(pady=10)

        # Botones
        self.boton_abrir = tk.Button(self.frame_botones, text="Abrir archivo", command=self.abrir_archivo, width=15)
        self.boton_abrir.pack(side=tk.LEFT, padx=10)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.salir, width=15)
        self.boton_salir.pack(side=tk.LEFT, padx=10)

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivo XML", "*.xml")])
        if archivo:  # Se verifica si se seleccionó un archivo
            self.lista_maquetas = leer_archivo_xml(archivo)
            self.archivo_leido_correctamente()

    def archivo_leido_correctamente(self):
        # Función para mostrar el mensaje de archivo leído correctamente
        self.label_archivo_leido = tk.Label(self.ventana, text="Archivo leído correctamente", bg="#B4D4FF", font=("Verdana", 12))
        self.label_archivo_leido.pack(pady=10)
        self.boton_gestionar = tk.Button(self.frame_botones, text="Gestionar Maquetas", command=self.gestionar_maquetas, width=15)
        self.boton_gestionar.pack(side=tk.LEFT, padx=10)

        #pasar las maquetas en orden alfabetico
        self.lista_maquetas.ordenar_alfabeticamente()
    def gestionar_maquetas(self):
        # Función para abrir la ventana de gestión de maquetas
        if self.lista_maquetas:
            ventana_gestion_maquetas = tk.Toplevel(self.ventana)
            ventana_gestion_maquetas.title("Gestionar Maquetas")
            ventana_gestion_maquetas.configure(bg="#B4D4FF")
            ventana_gestion_maquetas.geometry("300x210")

            # Contenedor para organizar elementos
            frame_contenedor = tk.Frame(ventana_gestion_maquetas, bg="#B4D4FF")
            frame_contenedor.pack(pady=10)

            # Labels
            label_gestionMaquetas = tk.Label(frame_contenedor, text="Selecciona la acción que \n deseas realizar", bg="#B4D4FF", font=("Verdana", 16))
            label_gestionMaquetas.pack(anchor="w", padx=10)

            # Botones
            boton_listado = tk.Button(frame_contenedor, text="Ver listado", command=self.ver_maquetas, width=20)
            boton_listado.pack(side=tk.RIGHT, padx=10, pady=5)
            boton_ver_maquetas = tk.Button(frame_contenedor, text="Ver graficamente", command=self.ver_graficamente, width=20)
            boton_ver_maquetas.pack(side=tk.RIGHT, padx=10, pady=5)

        else:
            print("No se ha cargado ninguna maqueta.")       

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
            objetivo_actual = maq.objetivos_cabeza
            while objetivo_actual:
                text_area.insert(tk.END, f"  Nombre: {objetivo_actual.nombre}, Fila: {objetivo_actual.fila}, Columna: {objetivo_actual.columna}\n")
                objetivo_actual = objetivo_actual.siguiente
            text_area.insert(tk.END, f"Estructura: {maq.estructura}\n\n")
            nodo_actual = nodo_actual.siguiente

    def salir(self):
        self.ventana.quit()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = VentanaPrincipal(ventana)
    ventana.mainloop()
