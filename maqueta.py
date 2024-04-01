class NodoObjetivo:
    def __init__(self, nombre=None, fila=None, columna=None):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.siguiente = None
        self.anterior = None

class Maqueta:
    def __init__(self, nombre, filas, columnas, entrada, objetivos, estructura):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.entrada = entrada
        self.estructura = estructura
        self.objetivos_cabeza = None  # Cabeza de la lista de objetivos

    def agregar_objetivo(self, nombre, fila, columna):
        nuevo_objetivo = NodoObjetivo(nombre, fila, columna)
        if not self.objetivos_cabeza:
            self.objetivos_cabeza = nuevo_objetivo
        else:
            actual = self.objetivos_cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_objetivo
            nuevo_objetivo.anterior = actual