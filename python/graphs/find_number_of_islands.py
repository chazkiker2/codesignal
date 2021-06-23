"""
Given a 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands:

Input: mat[][] = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]
Output: 5
"""


class Graph:
    def __init__(self, row, col, g):
        self.row = row
        self.col = col
        self.graph = g

    def is_safe(self, i, j, visited):
        return (0 <= i < self.row and
                0 <= j < self.col and
                not visited[i][j] and self.graph[i][j])

    def dfs(self, i, j, visited):
        row_n_br = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_n_br = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True
        for k in range(8):
            if self.is_safe(i + row_n_br[k], j + col_n_br[k], visited):
                self.dfs(i + row_n_br[k], j + col_n_br[k], visited)

    def count_islands(self):
        visited = [[False for _ in range(self.col)] for _ in range(self.row)]
        count = 0

        for i in range(self.row):
            for j in range(self.col):
                if not visited[i][j] and self.graph[i][j] == 1:
                    self.dfs(i, j, visited)
                    count += 1

        return count


if __name__ == '__main__':
    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]

    row = len(graph)
    col = len(graph[0])

    g = Graph(row, col, graph)

    print("Number of islands is:")
    print(g.count_islands())
