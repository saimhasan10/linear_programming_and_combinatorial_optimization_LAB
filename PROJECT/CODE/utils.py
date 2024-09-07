def parse_input(data):
    """
    Parse input data into a list of edges.
    """
    edges = []
    for line in data:
        u, v, w = map(int, line.split())
        edges.append((u, v, w))
    return edges
