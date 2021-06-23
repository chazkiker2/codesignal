"""
You are given a directed acyclic graph_02 (DAG) that contains N nodes.

Write a function that can find all the possible paths from node `0` to node `N - 1`. You can return the path in any order.

`graph[a]` is a list of all nodes `b` for which the edge `a -> b` exists.

## Example:

- Input: graph_02 = [[1, 2],[3],[3],[4],[]]
- Output: [[0,1,3,4], [0,2,3,4]]

Note: The results must be returned in sorted order. You can use any built-in sort method on the results array at the end of your function before returning.


## Constraints

- [execution time limit] 4 seconds (py3)
- [input] array.array.integer graph_02
- [output] array.array.integer

"""


import unittest


all_paths = []
nodes = {}


def traversal(node, current_path):
    global all_paths, nodes

    current_path.append(node)

    if len(nodes[node]) < 1:
        all_paths.append(current_path)

    for edge in nodes[node]:
        traversal(edge, current_path.copy())


def find_paths(graph):
    global all_paths, nodes

    if not graph:
        return []

    nodes = {i: set(connections) for i, connections in enumerate(graph)}

    traversal(0, [])
    return all_paths


class Test(unittest.TestCase):
    def test_001(self):
        self.assertEqual(
            [
                [0, 1, 3],
                [0, 2, 3]
            ],
            find_paths(
                [
                    [1, 2],
                    [3],
                    [3],
                    []
                ]
            )
        )

    def test_002(self):
        expected = [[0, 1, 3],
                    [0, 2, 3],
                    [0, 1, 2, 3, 4],
                    [0, 1, 3, 4],
                    [0, 1, 4],
                    [0, 3, 4],
                    [0, 4]]

        actual = find_paths(
            [[4, 3, 1], [3, 2, 4], [3], [4], []])

        self.assertListEqual(expected, actual)

    def test_003(self):
        expected = [[0, 1, 3],
                    [0, 2, 3],
                    [0, 1, 2, 3, 4],
                    [0, 1, 3, 4],
                    [0, 1, 4],
                    [0, 3, 4],
                    [0, 4],
                    [0, 1]]
        actual = find_paths([[1], []])
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
