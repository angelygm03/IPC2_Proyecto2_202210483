class NodoObjetivo:
    def __init__(self, nombre=None, fila=None, columna=None):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.siguiente = None
        self.anterior = None

class Maqueta:
    def __init__(self, nombre, filas, columnas, entrada, estructura):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.entrada = entrada
        self.estructura = estructura
        self.primer_objetivo = None
        self.ultimo_objetivo = None

    def agregar_objetivo(self, nombre, fila, columna):
        nuevo_objetivo = NodoObjetivo(nombre, fila, columna)
        if not self.primer_objetivo:
            self.primer_objetivo = nuevo_objetivo
            self.ultimo_objetivo = nuevo_objetivo
        else:
            nuevo_objetivo.anterior = self.ultimo_objetivo
            self.ultimo_objetivo.siguiente = nuevo_objetivo
            self.ultimo_objetivo = nuevo_objetivo