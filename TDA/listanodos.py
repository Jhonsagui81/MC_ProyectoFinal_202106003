from TDA.Nodo import NodoVertice
from collections import deque
from tkinter import messagebox


class ListaVertices:
    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.limite = 0

    def Insertar(self, nombre, objeto):
        NuevoNodo = NodoVertice(nombre, objeto)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.limite += 1
            print("Inserto correcto en if")
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
            self.limite += 1
            print("Inserto correcto en else")

    def Busqueda(self, nombre, Relacion):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerVertice() == nombre:
                Aux = self.Inicio
                print("encontrado")
                while Aux != None:
                    if Aux.ObtenerVertice() == Relacion:
                        Auxiliar.ObtenerObjeto().insertar(Aux.ObtenerObjeto())
                        Aux.ObtenerObjeto().insertar(Auxiliar.ObtenerObjeto())
                        print("asignado objeto")
                        Auxiliar.ObtenerObjeto().imprimit()
                        break
                    Aux = Aux.Siguiente
            Auxiliar = Auxiliar.Siguiente

    def ImprimirOne(self, vertice):
        # self.Inicio.ObtenerObjeto().imprimit()
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Auxiliar.ObtenerObjeto().imprimit()
            Auxiliar = Auxiliar.Siguiente


    def crear_diccionario(self):
        Auxiliar = self.Inicio
        grafo = {}
        while Auxiliar != None:
            lista_vecinos = []
            caminos = Auxiliar.ObtenerObjeto().cantida_relaciones()

            for i in range(caminos):
                lista_vecinos.append(Auxiliar.ObtenerObjeto().vertices_nodo(i))
            grafo[str(Auxiliar.ObtenerVertice())] = lista_vecinos
            Auxiliar = Auxiliar.Siguiente
        return grafo


    def camino_corto(self, grafo, inicio, final):
        visitados = set()
        cola = deque([(inicio, [inicio])])
        while cola:
            (nodo_actual, camino_actual) = cola.popleft()
            if nodo_actual == final:
                return camino_actual
            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino_actual + [vecino]))
        return None


    def dfs_dos_caminos_no_cortos(self, grafo, inicio, final, camino_actual=None, caminos=None):
        if camino_actual is None:
            camino_actual = [inicio]
        if caminos is None:
            caminos = []
        if inicio == final:
            caminos.append(camino_actual)
        else:
            for vecino in grafo[inicio]:
                if vecino not in camino_actual:
                    self.dfs_dos_caminos_no_cortos(grafo, vecino, final, camino_actual + [vecino], caminos)

        # ordenar la lista de caminos por longitud
        caminos.sort(key=len)
        # devolver los dos caminos que no son el más corto
        return caminos[1:3]
