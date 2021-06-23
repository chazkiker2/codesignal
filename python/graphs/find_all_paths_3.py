class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __repr__(self):
        return f"Vertex({self.value})"


def traverse(node, path, out_matrix):
    path.append(node.value)
    if len(node.edges) < 1:
        out_matrix.append(path)
    for edge in node.edges:
        traverse(edge, path.copy(), out_matrix)


def find_paths(graph):
    all_paths = []

    if not graph:
        return []

    # initialize a vertex with the value of index for each index in graph
    nodes = [Vertex(i) for i in range(len(graph))]

    # for each node, sublist in a joined iteration of nodes and graph
    for node, graph_sublist in zip(nodes, graph):
        node.edges = [nodes[index] for index in graph_sublist]

    traverse(nodes[0], [], all_paths)
    return all_paths


if __name__ == '__main__':
    print(find_paths([[1, 2], [3], [3], []]))  # -> [[0, 1, 3] [0, 2, 3]]
    print(find_paths(
        [[4, 3, 1], [3, 2, 4], [3], [4], []]))  # -> [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    print(find_paths([[1], []]))  # -> [[0, 1]]
