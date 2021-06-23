class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __repr__(self):
        return f"Node({self.value})"


def create_graph(graph):
    nodes = []
    for i in range(len(graph)):
        node = GraphNode(i)
        nodes.append(node)
    for i in range(len(graph)):
        nodes[i].edges = list(map(lambda i: nodes[i], graph[i]))
        print(nodes[i].edges)
    return nodes


def traversal(node, path, out_matrix):
    path.append(node.value)
    if len(node.edges) < 1:
        out_matrix.append(path)
    for edge in node.edges:
        traversal(edge, path.copy(), out_matrix)


def find_paths(graph):
    all_paths = []

    if not graph:
        return []

    nodes = create_graph(graph)
    print(f"nodes={nodes}")

    traversal(nodes[0], [], all_paths)
    return all_paths

if __name__ == '__main__':
    print(find_paths([[1, 2], [3], [3], []]))
    print(find_paths([[4, 3, 1], [3, 2, 4], [3], [4], []]))
    print(find_paths([[1], []]))
