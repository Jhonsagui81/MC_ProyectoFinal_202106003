class Verice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaNodos = []

    def ObtenerVertice(self):
        return self.nombre

    def insertar(self, nodo):
        self.listaNodos.append(nodo)

    def imprimit(self):
        for ews in self.listaNodos:
            print("pasa algo?")
            print("el nodo "+str(self.nombre)+" tiene relaciones son con: "+str(ews.ObtenerVertice()))

    def cantida_relaciones(self):
        numero = len(self.listaNodos)
        return numero

    def vertices_nodo(self, id):
        texto = self.listaNodos[id].ObtenerVertice()
        return texto

    def busca_nodofinal(self, camino_seguir, nodo_final, lista_arista):
        if self.listaNodos[camino_seguir].ObtenerVertice() == nodo_final:
            lista_arista.append(self.listaNodos[camino_seguir].ObtenerVertice())
            return True
        else:
            lista_arista.append(self.listaNodos[camino_seguir].ObtenerVertice())
            rep = self.listaNodos[camino_seguir].cantida_relaciones()
            for se in range(rep):
                #posiblemente nueva lista y hacer lista de lista
                #o hacer concatenacion por comas en todos los caminos
                estado = self.listaNodos[camino_seguir].busca_nodofinal(se, nodo_final, lista_arista)
