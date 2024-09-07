import networkx as nx
import matplotlib.pyplot as plt


def visualize_input_graph(edges):
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw(
        G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Input Graph")
    plt.show()


if __name__ == "__main__":
    num_edges = int(input("Enter the number of edges: "))

    print("Enter each edge in the format: Source Destination Cost")
    edges = []
    for _ in range(num_edges):
        edge = input().strip().split()
        u, v, w = map(int, edge)
        edges.append((u, v, w))

    visualize_input_graph(edges)
