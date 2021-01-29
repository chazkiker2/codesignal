from collections import deque


def micah_refactored(matrix):
    visited = set()
    stack = deque()
    count = 0
    for i in range(len(matrix)):
        if i not in visited:
            count += 1
            stack.append(i)
        while stack:
            node = stack.pop()
            visited.add(node)
            for j, friend in enumerate(matrix[node]):
                if friend == 1 and j not in visited:
                    stack.append(j)
    return count


def friend_circles_micah(friendships):
    visited = []
    stack = []
    count = 0
    for i in range(len(friendships)):
        if i not in visited:
            count += 1
            stack.append(i)
        while stack:
            node = stack.pop()
            visited.append(node)
            for j, friend in enumerate(friendships[node]):
                if friend == 1 and j not in visited:
                    stack.append(j)

    return count
