class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices (substations)
        self.graph = []  # List to store edges (transmission lines)

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))  # Add an edge to the graph
