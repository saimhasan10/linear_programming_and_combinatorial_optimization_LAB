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

    # Determine the number of distinct vertices
    vertices = set()
    for u, v, w in edges:
        vertices.add(u)
        vertices.add(v)
    num_vertices = len(vertices)

    # Create the graph with the correct number of vertices
    graph = Graph(num_vertices)

    # Add edges to the graph
    for u, v, w in edges:
        graph.add_edge(u, v, w)

    # Find the Minimum Spanning Tree using Kruskal's algorithm
    mst_edges_kruskal = kruskal_mst(graph)

    # Output the MST edges with original vertex numbering
    print("Optimal Power Grid Layout:")
    for u, v, w in mst_edges_kruskal:
        print(f"({u}, {v}, {w})")

    # Visualize the optimal power grid layout
    visualize_mst(mst_edges_kruskal)


if __name__ == "__main__":
    main()
