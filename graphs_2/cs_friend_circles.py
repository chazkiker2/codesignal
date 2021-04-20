"""
There are N students in a baking class together. Some of them are friends, while some are not friends.
The students' friendship can be considered transitive. This means that if Ami is a direct friend of Bill,
and Bill is a direct friend of Casey, Ami is an indirect friend of Casey. A friend circle is a group of students
who are either direct or indirect friends.

Given a N*N matrix M representing the friend relationships between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.

You need to write a function that can output the total number of friend circles among all the students.

Example 1:

Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation: The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.

    a   b   c
a   1   1   0
b   1   1   0
c   0   0   1
a: [b]
b: [a]
c: []


Example 2:

Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation: The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
    a   b   c
a   1   1   0
b   1   1   1
c   0   1   1

a: [b]
b: [a, c]
c: [b]


[execution time limit] 4 seconds (py3)

[input] array.array.integer friendships

[output] integer

MORE TESTS
[
[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
]
expected output: 8

[
[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
]
expected output: 3

"""

from collections import deque


class GraphNode():
    def __init__(self, value):
        self.value = value
        self.edges = set()


def depth_first_traversal(starting_vertex, visited=None):
    stack = deque()
    stack.append(starting_vertex)

    if not visited:
        visited = set()

    while len(stack) > 0:
        vert = stack.pop()
        if vert not in visited:
            visited.add(vert)

            for next_vert in vert.edges:
                stack.append(next_vert)


def cs_friend_circles(matrix):
    visited = set()
    friend_nodes = {i: GraphNode(i) for i in range(len(matrix))}
    friend_groups = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                friend_nodes[i].edges.add(friend_nodes[j])
                friend_nodes[j].edges.add(friend_nodes[i])

    while len(visited) < len(friend_nodes):
        for key in friend_nodes:
            if friend_nodes[key] not in visited:
                friend_groups += 1
                depth_first_traversal(friend_nodes[key], visited)

    return friend_groups


def friend_circles(matrix):
    visited = set()
    stack = deque()
    circle_list = []
    circle_list_02 = set()
    temp = []
    count = 0

    for is_friend in range(len(matrix)):
        if is_friend not in visited:
            circle_list.append(visited.copy())
            # temp = visited.copy()
            count += 1
            stack.append(is_friend)

        while stack:
            node = stack.pop()
            visited.add(node)

            for peer, is_friend in enumerate(matrix[node]):
                if is_friend == 1 and peer not in visited:
                    stack.append(peer)



        # tup = tuple(visited.copy())
        temp = visited.copy()
        res = visited.copy() - temp.copy()
        print(f"res: {res}, temp: {temp}")
        circle_list_02.add(tup)
        print(f"circle_list_02: {circle_list_02}")
        # circle_list.append(visited.copy())

    print(circle_list)
    print(circle_list_02)
    return count


if __name__ == '__main__':
    # 1 1 0
    # 1 1 0
    # 0 0 1
    res_1 = friend_circles([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(res_1 == 2)

# class Vertex:
#     def __init__(self, value):
#         self.value = value
#         self.connections = {}
#
#
# class Graph:
#     def __int__(self):
#         self.vertices = {}
#
#     def __contains__(self, vert):
#         return vert in self.vertices
#
#     def __iter__(self):
#         return iter(self.vertices.values())
#
#     def add_vertex(self, value):
#         pass
#
#     def add_edge(self, v1, v2, weight=0):
#         pass


# class Stack():
#     def __init__(self):
#         self.stack = []
#
#     def push(self, value):
#         self.stack.append(value)
#
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#
#     def size(self):
#         return len(self.stack)
#
#
#
# def depth_first_search(starting_vert):
#     stack = Stack()
#     stack.push(starting_vert)
#     visited = set()
#     while stack.size() > 0:
#         vert = stack.pop()
#         if vert not in visited:
#             print(vert)
#             visited.add(vert)
#             for next_vert in vert.get_neighbors():
#                 stack.push(next_vert)
# class GraphNode():
#     def __init__(self, value):
#         self.value = value
#         self.edges = []
#
# def convert_to_graph(matrix):
#
#     for sub_arr in matrix:
#         for friend in sub_arr:
#             GraphNode(friend)
#
# # Create a visited set to track visited nodes
# # Go through all nodes, for each:
# #   if node hasn't been visited:
# #       increment count
# #       do a traversal (marking all nodes as visited)
# def friend_circles(matrix):
#     visited = set()
#     friend_nodes = [GraphNode(i) for i in range(len(matrix))]
#
#     for el in friend_nodes:
#
#
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] in visit
