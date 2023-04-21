import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío
G = nx.Graph()

# Agregar nodos y aristas
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Dibujar el grafo
nx.draw(G, with_labels=True)
plt.show()

# Verificar que el grafo sea conexo
if not nx.is_connected(G):
    print("El grafo no es conexo")
else:
    # Pedir al usuario que seleccione los nodos inicial y final
    start_node = int(input("Ingrese el nodo inicial: "))
    end_node = int(input("Ingrese el nodo final: "))

    # Encontrar todos los caminos simples entre los nodos seleccionados
    paths = nx.all_simple_paths(G, start_node, end_node)

    # Imprimir los caminos encontrados
    for path in paths:
        print(path)
