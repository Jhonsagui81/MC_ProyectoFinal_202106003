import sys
from PyQt5.QtWidgets import *
import networkx as nx
import matplotlib.pyplot as plt

class GraphEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.graph = nx.Graph()

        self.canvas = None
        self.node_positions = {}

        vbox = QVBoxLayout()

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Nodo:"))
        self.node_spinbox = QSpinBox()
        self.node_spinbox.setRange(1, 100)
        hbox.addWidget(self.node_spinbox)
        hbox.addWidget(QLabel("X:"))
        self.x_spinbox = QSpinBox()
        self.x_spinbox.setRange(0, 1000)
        hbox.addWidget(self.x_spinbox)
        hbox.addWidget(QLabel("Y:"))
        self.y_spinbox = QSpinBox()
        self.y_spinbox.setRange(0, 1000)
        hbox.addWidget(self.y_spinbox)
        self.add_node_button = QPushButton("Agregar nodo")
        self.add_node_button.clicked.connect(self.add_node)
        hbox.addWidget(self.add_node_button)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Nodo 1:"))
        self.start_spinbox = QSpinBox()
        self.start_spinbox.setRange(1, 100)
        hbox.addWidget(self.start_spinbox)
        hbox.addWidget(QLabel("Nodo 2:"))
        self.end_spinbox = QSpinBox()
        self.end_spinbox.setRange(1, 100)
        hbox.addWidget(self.end_spinbox)
        self.find_path_button = QPushButton("Encontrar camino")
        self.find_path_button.clicked.connect(self.find_path)
        hbox.addWidget(self.find_path_button)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle("Editor de grafo")

    def add_node(self):
        node = self.node_spinbox.value()
        x = self.x_spinbox.value()
        y = self.y_spinbox.value()

        self.graph.add_node(node)
        self.node_positions[node] = (x, y)

        self.draw_graph()

    def draw_graph(self):
        if self.canvas is None:
            self.canvas = plt.figure().canvas

        self.canvas.axes.clear()

        pos = nx.spring_layout(self.graph, pos=self.node_positions, fixed=self.node_positions.keys())

        nx.draw(self.graph, pos, with_labels=True, ax=self.canvas.axes)

        self.canvas.draw()

    def find_path(self):
        start_node = self.start_spinbox.value()
        end_node = self.end_spinbox.value()

        if not nx.is_connected(self.graph):
            QMessageBox.warning(self, "Error", "El grafo no es conexo")
            return

        paths = nx.all_simple_paths(self.graph, start_node, end_node)

        QMessageBox.information(self, "Caminos", "\n".join(str(path) for path in paths))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = GraphEditor()
    editor.show()
    sys.exit(app.exec_())
