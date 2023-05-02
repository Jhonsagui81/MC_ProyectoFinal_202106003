from TDA.data import VerticesData

class NodoVertice:
    def __init__(self, nombre, objeto):
        self.Vertice = VerticesData(nombre, objeto)
        self.Siguiente = None

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
    def ObtenerVertice(self):
        return self.Vertice.ObtenerVertice()
    def ObtenerObjeto(self):
        return self.Vertice.ObtenerObjeto()
    
        