class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = []


def createGraph(graph):
    nodes = []
    for i in range(len(graph)):
        node = GraphNode(i)  # initialize all provided nodes
        nodes.append(node)
    for i in range(len(graph)):
        # make edges be the neighboring node, not the index. Make the map be a list so you can work with it
        nodes[i].edges = list(map(lambda i: nodes[i], graph[i]))
        # node.edges = graph[i]   # create edges based on provided graph data --- this points to the index of the neighbor
    return nodes


def traversal(node, path, out_Matrix):
    path.append(node.value)  # keep track of where you are
    # if you got to the end (no more neighbors):
    if len(node.edges) < 1:
        # ... then add your path list to the matrix
        out_Matrix.append(path)
    for edge in node.edges:  # find neighbors
        # each neighbor needs their own copy of path so we can keep track of different routes
        traversal(edge, path.copy(), out_Matrix)


def cs_find_all_paths_from_a_to_b(graph):
    out_Matrix = []
    if graph == []:  # if you are passed an empty graph:
        return []
    # Use input to create graph from adjacency matrix (missing trailing zeros)
    nodes = createGraph(graph)
    traversal(nodes[0], [], out_Matrix)  # visit 0 node to start
    return out_Matrix


def find_paths_a_to_b_antony(graph):
    x = []
    if graph == []:
        return []

    def node_path(n, path):
        new_path = path + [n]
        for i in graph[n]:
            node_path(i, new_path)

        if n == len(graph) - 1:
            x.append(new_path)

        return x

    return node_path(0, [])


print(cs_find_all_paths_from_a_to_b([[1, 2], [3], [3], []]))
print(cs_find_all_paths_from_a_to_b([[4, 3, 1], [3, 2, 4], [3], [4], []]))
print(cs_find_all_paths_from_a_to_b([[1], []]))
