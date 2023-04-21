import pygame
import networkx as nx

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

class GraphEditor:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Editor de grafo")

        self.graph = nx.Graph()
        self.node_positions = {}

        self.font = pygame.font.SysFont(None, 24)

        self.node_size = 20
        self.node_color = GREEN
        self.selected_node_color = RED
        self.edge_color = GRAY

        self.selected_node = None

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.validate_graph_and_ask_for_nodes()
                    return

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        node = self.add_node(pos)
                        if node is not None:
                            if self.selected_node is not None:
                                self.add_edge(self.selected_node, node)
                                self.selected_node = None
                            else:
                                self.selected_node = node

            self.screen.fill(WHITE)
            self.draw_graph()
            pygame.display.flip()

    def validate_graph_and_ask_for_nodes(self):
        if not nx.is_connected(self.graph):
            print("El grafo no es conexo")
            self.run()
        else:
            print("El grafo es conexo")
            self.ask_for_nodes()

    def ask_for_nodes(self):
        # Aquí puedes agregar una ventana emergente que solicite al usuario
        # ingresar el nodo inicial y el nodo final
        pass

    def add_node(self, pos):
        for node, position in self.node_positions.items():
            if self.distance(pos, position) < self.node_size:
                return node

        node = len(self.node_positions) + 1
        self.node_positions[node] = pos
        self.graph.add_node(node)

        return node

    def add_edge(self, node1, node2):
        self.graph.add_edge(node1, node2)

    def draw_graph(self):
        for node, position in self.node_positions.items():
            color = self.selected_node_color if node == self.selected_node else self.node_color
            pygame.draw.circle(self.screen, color, position, self.node_size)

            text_surface = self.font.render(str(node), True, BLACK)
            text_rect = text_surface.get_rect(center=position)
            self.screen.blit(text_surface, text_rect)

        for edge in self.graph.edges:
            position1 = self.node_positions[edge[0]]
            position2 = self.node_positions[edge[1]]
            pygame.draw.line(self.screen, self.edge_color, position1, position2, 2)

    def distance(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

if __name__ == '__main__':
    editor = GraphEditor()
    editor.run()
    editor.validate_graph_and_ask_for_nodes()
