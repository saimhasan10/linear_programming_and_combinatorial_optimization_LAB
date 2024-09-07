from graph import Graph
from algorithms import kruskal_mst
from visualization import visualize_mst
from utils import parse_input


def main():
    # Prompt user for the number of transmission lines (edges)
    num_edges = int(input("Enter the number of transmission lines (edges): "))

    # Collect details of each transmission line from the user
    print("Enter each transmission line in the format: Source Destination Cost")
    data = []
    for _ in range(num_edges):
        edge = input()
        data.append(edge)

    # Parse the input data to create edges list
    edges = parse_input(data)

    # Adjust the vertex indices to be zero-based
    adjusted_edges = [(u - 1, v - 1, w) for u, v, w in edges]

    # Determine the number of substations (vertices)
    vertices = set()
    for edge in adjusted_edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    V = len(vertices)

    # Create the graph with the collected data
    graph = Graph(V)
    for u, v, w in adjusted_edges:
        graph.add_edge(u, v, w)

    # Find the Minimum Spanning Tree using Kruskal's algorithm
    mst_edges_kruskal = kruskal_mst(graph)
    print("Optimal Power Grid Layout: ", mst_edges_kruskal)

    # Visualize the optimal power grid layout
    visualize_mst(mst_edges_kruskal)


if __name__ == "__main__":
    main()
