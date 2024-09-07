def find(parent, i):
    """
    Find the root of the set containing element i using path compression.
    """
    if parent[i] != i:
        parent[i] = find(parent, parent[i])  # Path compression
    return parent[i]


def union(parent, rank, x, y):
    """
    Union two sets represented by x and y using union by rank.
    """
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1


def kruskal_mst(graph):
    """
    Implements Kruskal's algorithm to find the MST for optimizing the power grid layout.
    """
    result = []  # Store the resultant MST
    i, e = 0, 0  # i is the index for sorted edges, e is the index for result[]
    sorted_graph = sorted(graph.graph, key=lambda item: item[2])  # Sort edges by weight
    parent = list(
        range(graph.V + 1)
    )  # Initialize parent array for union-find, assuming vertices start from 1
    rank = [0] * (graph.V + 1)  # Initialize rank array for union-find

    # Iterate through all edges in sorted order
    while e < graph.V - 1 and i < len(sorted_graph):
        u, v, w = sorted_graph[i]
        i += 1

        # Find root of sets containing u and v
        x = find(parent, u)
        y = find(parent, v)

        # If u and v are not in the same set, add edge to result
        if x != y:
            e += 1
            result.append((u, v, w))
            # Union the sets of u and v
            union(parent, rank, x, y)

    return result
