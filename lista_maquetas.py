class NodoMaqueta:
    def __init__(self, maqueta=None):
        self.maqueta = maqueta
        self.siguiente = None
        self.anterior = None

class ListaMaquetas:
    def __init__(self):
        self.cabeza = None

    def agregar_maq(self, maqueta):
        nuevo_nodo = NodoMaqueta(maqueta)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def ordenar_alfabeticamente(self):
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            while siguiente:
                if actual.maqueta.nombre > siguiente.maqueta.nombre:
                    temp = actual.maqueta
                    actual.maqueta = siguiente.maqueta
                    siguiente.maqueta = temp
                siguiente = siguiente.siguiente
            actual = actual.siguiente

