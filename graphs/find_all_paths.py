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


def create_graph(graph):
    nodes = [GraphNode(i) for i in range(len(graph))]
    for i in range(len(graph)):
        nodes[i].edges = list(map(lambda i: nodes[i], graph[i]))
        print(nodes[i].edges)
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


def get_children(graph):
    family = {}

    for i, layer in enumerate(graph):
        family[i] = [node for node in layer]

    return family


def find_all_paths(graph):
    if not graph:
        return []

    all_paths = []

    n = len(graph)
    if n == 1:
        return graph

    visited = []
    family = get_children(graph)

    def inner_util():
        path = [0]
        for node in family:
            print(node, family[node])

            # while len(family[node]) > 0:
            node_to_get = path[-1]
            if len(family[node_to_get]) > 0:
                path.append(family[node_to_get].pop(0))
                # path.append(family[node].pop())
                # family[node].remove(0)
            # path.append(family[node][0])

        return path if path != [0] else None

    # for i in range(len(graph)):
    while len(family[0]) > 0:
        visited.append(inner_util())

    return visited


def find_all_paths_3(graph):
    # if not graph:
    #     return []
    #
    # n = len(graph)
    # if n == 1:
    #     return graph

    visited = []
    family = get_children(graph)
    print(family)
    paths = [[0] for _ in range(len(graph))]

    current_node = 0
    next_i = 0
    while len(family[current_node]) > next_i:
        paths[next_i].append(family[current_node][next_i])
        current_node = family[current_node][next_i]
    # for key in family:
    #
    #     for i in range(len(family[key])):
    #         if len(paths) > i:
    #             paths[i].append(family[key][i])
    #         else:
    #             paths.append([])

    return paths

    # for i in range(len(family)):
    #     for j in range(len(family[i])):
    #         print(f"i={i},j={j}: el={family[i][j]}")
    #         if j < len(paths):
    #             paths[j].append(family[i][j])
    #         else:
    #             paths.append([])
    #             paths[j].append(family[i][j])
    #         #     paths[i].append
    # return paths
    # visited_nodes = set()
    # paths = []
    #
    # for node in family:
    #     count = 0
    #     while len(family[node]) > count:
    #         path = [node]

    # def get_next(node):
    #     # nonlocal visited_nodes
    #     if not family[node]:
    #         return
    #
    #     paths.append(family[node])  # path.append(family[node][0])
    #
    #     for next in family[node]:
    #         get_next(next)
    #
    #     return paths

    # get_next(0)
    # return paths

    # def inner_util():
    #     path = [0]
    #     for node in family:
    #         print(node, family[node])
    #
    #         # while len(family[node]) > 0:
    #         node_to_get = path[-1]
    #         if len(family[node_to_get]) > 0:
    #             path.append(family[node_to_get].pop(0))
    #             # path.append(family[node].pop())
    #             # family[node].remove(0)
    #         # path.append(family[node][0])
    #
    #     return path if path != [0] else None
    #
    # # for i in range(len(graph)):
    # while len(family[0]) > 0:
    #     visited.append(inner_util())

    # return visited


# paths = []
# def paths_util(graph, start, end, visited, path):
#     print(f"{start}, {end}, {visited}, {path}")
#     visited[start] = True
#     path.append(start)
#     if start == end:
#         print(path)
#         # paths.append(path)
#         # paths.append(path)
#     else:
#         for i in graph[start]:
#             if not visited[i]:
#                 paths_util(graph, i, end, visited, path)
#
#     # path.pop()
#     visited[start] = False


# def find_all_paths_2(graph):
#     visited = [False for _ in graph]
#     path = []
#     paths_util(graph, 0, len(graph), visited, path)
#     return path


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
    # tester(find_all_paths, test_case_dict)
    # tester(find_all_paths_2, test_case_dict)
    tester(find_paths, test_case_dict)

    # for k, v in test_case_dict.items():
    #     tester(k, v, find_all_paths)
