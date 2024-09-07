import networkx as nx
import matplotlib.pyplot as plt


def visualize_mst(mst_edges):
    """
    Visualize the Minimum Spanning Tree (MST) for the optimized power grid layout.
    """
    G = nx.Graph()
    for u, v, w in mst_edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)  # Layout for visualization
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw(
        G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10
    )

    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Optimal Power Grid Layout (Kruskal's MST)")
    plt.show()
