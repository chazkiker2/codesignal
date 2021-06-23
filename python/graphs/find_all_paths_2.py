import unittest
from unittest.case import expectedFailure


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
        self.assertEqual([[0, 1, 3], [0, 2, 3]],
                         find_paths([[1, 2], [3], [3], []]))

    def test_002(self):
        """
        """
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
        """
        """
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
