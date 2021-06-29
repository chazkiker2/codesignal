# class Node:
#     Node next
#     Node down
#     int data

# [1] -> [2] -> [3] -> [8] -> [10]
#                |      |
#                |     [9]
#                |
#               [4] -> [5] -> [6]
#                              |
#                             [7]

# [1] -> [2] -> [3] -> [8] -> [10]
#                |      |
#                |     [9]
#                |
#               [4] -> [5] -> [6]
#                |              |
#               [X]            [7]


# [1] -> [2] -> [3]                  [8] -> [10]
#                |                   |
#                |                      [9]
#                |
#               [4] -> [5] ->[6]
#                |              |
#               [X]            [7]


# node.next into COLLECTION
#
# as soon as we hit a node with DOWN
# node.next HEAD of the DOWN_LIST
# (TAIL of DOWN_LIST).next = head.next ---
#

# [8] -> [10]
#  |
# [9]


# [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> [7] -> [8] -> [9] -> [10]


# [1] -> [2] -> [3] -> [8] -> [10]
#                |      |
#                |     [9]
#                |
#               [4] -> [5] -> [6]
#                              |
#                             [7]

"""
- flatten linked list
- while node has a down pointer, change down to right
- once we're out of downs, go to next
- assume input is head
- assume if node doesn't have down, down is None


while head.down:
    head.down.next = head.next
    head.next = head.down
    head = head.next

head ->

"""


import unittest
from python.test_util import AbstractSuite


class Node(object):
    def __init__(self, data, nxt=None, down=None):
        super().__init__()
        self.data = data
        self.nxt = nxt
        self.down = down

    def __repr__(self):
        return f"Node({self.data})"

    def print(self):
        return f"<Node: {self.data=}, {self.nxt=}, {self.down=}>"


def flatten_linked_list_in_interview(head: Node) -> Node:
    """
    :returns: head of the flattened linked list
    """
    # if our current node has a down, we want that down to be the next right
    # current.next = current.down if not None

    if not head:
        return head

    while head.down or head.nxt:
        if head.down:

            tail = head.down

            while tail.nxt:
                tail = tail.nxt

            tail.nxt = head.nxt
            head.nxt = head.down
            head.down = None

            if head.nxt:
                head = head.nxt

        else:
            head = head.nxt

    return head


def flatten_linked_list(head: Node) -> Node:
    """
    :returns: head of the flattened linked list
    """
    # if our current node has a down, we want that down to be the next right
    # current.next = current.down if not None

    if not head:
        return head

    current = head

    dummy_node = Node("*")
    dummy_node.nxt = current

    while current.down or current.nxt:
        if current.down:

            tail = current.down

            while tail.nxt:
                tail = tail.nxt

            tail.nxt = current.nxt
            current.nxt = current.down
            current.down = None

            if current.nxt:
                current = current.nxt

        else:
            current = current.nxt

    return dummy_node.nxt

    # [8] -> [10]
    #  |
    # [9] -> [10]
    #  |
    # [X]

    # as soon as we hit a node with DOWN
    # (TAIL of DOWN_LIST).next = head.next ---

    # node.next HEAD of the DOWN_LIST
    # tail
    # head.down.nxt = head.nxt
    # head.nxt = head.down # 8 -> 9 -> 10
    # head = head.nxt  # 9


class Test(unittest.TestCase):
    def test_001(self):
        nodes = {}

        for i in range(1, 11):

            nodes[i] = Node(i)

        connections = [
            (1, 2, None),
            (2, 3, None),
            (3, 8, 4),
            (4, 5, None),
            (5, 6, None),
            (6, None, 7),
            (8, 10, 9),
        ]
        for node, nxt, down in connections:
            if nxt:
                nodes[node].nxt = nodes[nxt]
            if down:
                nodes[node].down = down

        nodes[1].next = nodes[2]
        new_head = self.fn(nodes[1])


# [1] -> [2] -> [3] -> [8] -> [10]
#                |      |
#                |     [9]
#                |
#               [4] -> [5] -> [6]
#                              |
#                             [7]
if __name__ == "__main__":
    AbstractSuite(Test, [flatten_linked_list]).run()
