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

    def CaminoOptimo(self, nodoInicial, nodoFinal):
        Auxiliar = self.Inicio
        resultado = []
        
        while Auxiliar != None:
            if Auxiliar.ObtenerVertice() == nodoInicial:
                caminos = Auxiliar.ObtenerObjeto().cantida_relaciones()
                print("la cantidad de caminos: "+ str(caminos))
                for i in range(caminos):
                    print("esta analizando el camino: "+str(i))
                    lista_vertices = []
                    estado = Auxiliar.ObtenerObjeto().busca_nodofinal(i, nodoFinal, lista_vertices)
                    if estado:
                        resultado.append(lista_vertices)
            Auxiliar = Auxiliar.Siguiente
                #pendiente4
                #esta funcion deberia retornar una lista con los nombres de los vertices que recorrio para encontrar el nodo final

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


    def bfs_todos_caminos_1(self, grafo, inicio, final):
        visitados = set()
        cola = deque([(inicio, [inicio])])
        caminos = []
        while cola:
            (nodo_actual, camino_actual) = cola.popleft()
            if nodo_actual == final:
                caminos.append(camino_actual)
            else:
                for vecino in grafo[nodo_actual]:
                    if vecino not in visitados:
                        visitados.add(vecino)
                        cola.append((vecino, camino_actual + [vecino]))
        caminos.sort(key=len)
        longitud_camino_mas_corto = len(caminos[0])
        caminos_cortos = [camino for camino in caminos if len(camino) > longitud_camino_mas_corto]
        if len(caminos_cortos) > 0: 
            return caminos_cortos[0]
        else:
            messagebox.showwarning("Camino simple 1", "No existe otro camino para este grado")
            return caminos_cortos


    def bfs_todos_caminos_2(self, grafo, inicio, final):
        visitados = set()
        cola = deque([(inicio, [inicio])])
        caminos = []
        while cola:
            (nodo_actual, camino_actual) = cola.popleft()
            if nodo_actual == final:
                caminos.append(camino_actual)
            else:
                for vecino in grafo[nodo_actual]:
                    if vecino not in visitados:
                        visitados.add(vecino)
                        cola.append((vecino, camino_actual + [vecino]))
        caminos.sort(key=len)
        longitud_camino_mas_corto = len(caminos[0])
        caminos_cortos = [camino for camino in caminos if len(camino) > longitud_camino_mas_corto]
        if len(caminos_cortos) > 1:
            return caminos_cortos[1]
        else:
            messagebox.showwarning("Camino simple 2", "No existe otro camino para este grado")
            return caminos_cortos



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



    def crear_dot(self, grafo, lista_corto):
        texto = ''
        
        Auxiliar = self.Inicio
        texto = "graph mi_grafo {\n"
        while Auxiliar != None:
            cont_corto = 0
            texto += "\t"+str(Auxiliar.ObtenerVertice())+"\n"
            camin = Auxiliar.ObtenerObjeto().cantida_relaciones()
            #Aqui deboo armar el camino de rojos
            if Auxiliar.ObtenerVertice() == lista_corto[cont_corto]:
                #Recorro los posibles caminos de cada vertice 
                cont_corto += 1
                for i in range(camin):
                    if Auxiliar.ObtenerObjeto().vertices_nodo(i) == lista_corto[cont_corto]:
                        cont_corto += 1
                        texto += "\t"+str(Auxiliar.ObtenerVertice())+"--"+str(lista_corto[cont_corto])
                        break
                #verificar nuevos vertices
                #aux = self.inicio

            else:
                for i in range(camin):
                    texto += "\t"+str(Auxiliar.ObtenerVertice())+"--"+str(Auxiliar.ObtenerObjeto().vertices_nodo(i))