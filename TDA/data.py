class VerticesData:
    def __init__(self, nombre, objeto):
        self.nombre = nombre
        self.objeto = objeto

    def ObtenerVertice(self):
        return self.nombre

    def ObtenerObjeto(self):
        return self.objeto