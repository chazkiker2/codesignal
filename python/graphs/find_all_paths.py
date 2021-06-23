"""
You are given a directed acyclic graph_02 (DAG) that contains N nodes.

Write a function that can find all the possible paths from node 0 to node N - 1. You can return the path in any order.

graph_02[a] is a list of all nodes b for which the edge a -> b exists.

Example:
Graph illustration

Input: graph_02 = [[1, 2],[3],[3],[4],[]]
Output: [[0,1,3,4], [0,2,3,4]]
Note: The results must be returned in sorted order. You can use any built-in sort method on the results array at the end of your function before returning.

[execution time limit] 4 seconds (py3)

[input] array.array.integer graph_02

[output] array.array.integer


"""


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __repr__(self):
        return f"G({self.value})"


def create_graph(graph):
    nodes = [GraphNode(i) for i in range(len(graph))]
    for i in range(len(graph)):
        nodes[i].edges = list(map(lambda i: nodes[i], graph[i]))

    return nodes


def find_paths(graph):
    if not graph:
        return []

    all_paths = []
    nodes = create_graph(graph)

    def traverse(node, path):
        path.append(node.value)
        if len(node.edges) < 1:
            all_paths.append(path)
        for edge in node.edges:
            traverse(edge, path.copy())

    traverse(nodes[0], [])
    return all_paths


def tester(func, dic):
    def inner_tester(name, tup):
        input, expected = tup
        actual = func(input)

        print("////////////////////////////")
        print(f"TESTING {name}")
        print(f"input={input}, \nexpected={expected}, \nactual={actual}")
        print(f"passed={actual == expected}")
        print("---------------------")

    for k, v in dic.items():
        inner_tester(k, v)


if __name__ == '__main__':
    test_case_dict = {
        "test_case_1": ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
        "test_case_2": ([[4, 3, 1], [3, 2, 4], [3], [4], []],
                        [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]])

    }
    tester(find_paths, test_case_dict)
