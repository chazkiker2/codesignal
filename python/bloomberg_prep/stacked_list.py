"""
Given a multi-level Linked List, modify the List to flatten it into one level.

## `Node` class

```python
class Node:
    def __init__(self, data, next=None, down=None):
        self.data = data
        self.next = next
        self.down = down
```

## INPUT:

- the head of the multi-level linked list. Each node has `data`, `next` and `down`
- assume if a Node does not have a Next node that `node.next` is `None`
- assume if a Node does not have a node below, that `node.down` is `None`

## OUTPUT:

- modify the linked list so that it is no longer multi-level
- return nothing



## Examples


### Example One

Input:

[1] -> [3]
 |
[2]


Output:

[1] -> [2] -> [3]


### Example Two

Input:

[1] -> [2] -> [3] -> [8] -> [10]
               |      |
               |     [9]
               |
              [4] -> [5] -> [6]
                             |
                            [7]

Output:

[1] -> [2] -> [3] -> [4] -> [5] -> [6] -> [7] -> [8] -> [9] -> [10]


### Example Three

Input:

[1] -> [2] -> [3] -> [10] -> [12]
               |      |
               |     [11]
               |
              [4] -> [7] -> [8]
               |             |
               |            [9]
               |
              [5] -> [6]

Output:

[1] -> [2] -> [3] -> [4] -> [5] -> [6] -> [7] -> [8] -> [9] -> [10] -> [11] -> [12]

"""

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
#
# - flatten linked list
# - while node has a down pointer, change down to right
# - once we're out of downs, go to next
# - assume input is head
# - assume if node doesn't have down, down is None
#
# while head.down:
#     head.down.next = head.next
#     head.next = head.down
#     head = head.next
#
# head ->
#
# [8] -> [10]
# [8] -> [10]
#  |
# [9] -> [10]
#  |
# [X]
#
# as soon as we hit a node with DOWN
# (TAIL of DOWN_LIST).next = head.next ---
#
# node.next HEAD of the DOWN_LIST
# tail
# head.down.nxt = head.nxt
# head.nxt = head.down # 8 -> 9 -> 10
# head = head.nxt  # 9

import unittest
from test_util import AbstractSuite


class Node(object):
    def __init__(self, data, next=None, down=None):
        super().__init__()
        self.data = data
        self.next = next
        self.down = down

    def __repr__(self):
        return f"Node({self.data})"

    def print(self):
        return f"<Node: {self.data=}, {self.next=}, {self.down=}>"


def flatten_linked_list_in_interview(head: Node):
    """
    :returns: head of the flattened linked list
    """
    # if our current node has a down, we want that down to be the next right
    # current.next = current.down if not None

    if not head:
        return

    while head.down or head.next:
        if head.down:

            tail = head.down

            while tail.nxt:
                tail = tail.nxt

            tail.nxt = head.next
            head.next = head.down
            head.down = None

            if head.next:
                head = head.next

        else:
            head = head.next


def flatten_linked_list(head: Node):
    """
    :returns: head of the flattened linked list
    """
    # if our current node has a down, we want that down to be the next right
    # current.next = current.down if not None

    if not head:
        return

    current = head

    while current.down or current.next:
        if current.down:

            tail = current.down

            while tail.next:
                tail = tail.next

            tail.next = current.next
            current.next = current.down
            current.down = None

            if current.next:
                current = current.next

        else:
            current = current.next


class Test(unittest.TestCase):
    def make_input_nodes(self, max_node, connections):
        nodes = {}
        output = {}
        for i in range(1, max_node+1):
            nodes[i] = Node(i)
            output[i] = Node(i)

        for node, next, down in connections:
            if next:
                nodes[node].next = nodes[next]
            if down:
                nodes[node].down = nodes[down]

        for i in range(1, max_node):
            output[i].next = output[i+1]
            output[i].down = None

        return nodes[1], output[1]

    def assert_linked_list(self, expected, actual):
        while expected:
            self.assertEqual(expected.data, actual.data)
            self.assertIsNone(actual.down)
            actual = actual.next
            expected = expected.next

        self.assertIsNone(actual)

    def make_test(self, max_node, connections):
        input_head, expected_head = self.make_input_nodes(
            max_node, connections)
        flatten_linked_list(input_head)
        self.assert_linked_list(expected_head, input_head)

    def test_001(self):
        self.make_test(
            max_node=3,
            connections=[(1, 3, 2)]
        )

    def test_002(self):
        self.make_test(
            max_node=10,
            connections=[
                (1, 2, None),
                (2, 3, None),
                (3, 8, 4),
                (4, 5, None),
                (5, 6, None),
                (6, None, 7),
                (8, 10, 9),
            ]
        )

    def test_003(self):
        self.make_test(
            max_node=12,
            connections=[
                (1, 2, None),
                (2, 3, None),
                (3, 10, 4),
                (4, 7, 5),
                (5, 6, None),
                (7, 8, None),
                (8, None, 9),
                (10, 12, 11),
            ]
        )

    # def test_001(self):
    #     nodes = {}

    #     for i in range(1, 11):
    #         nodes[i] = Node(i)

    #     connections = [
    #         (1, 2, None),
    #         (2, 3, None),
    #         (3, 8, 4),
    #         (4, 5, None),
    #         (5, 6, None),
    #         (6, None, 7),
    #         (8, 10, 9),
    #     ]
    #     for node, nxt, down in connections:
    #         if nxt:
    #             nodes[node].nxt = nodes[nxt]
    #         if down:
    #             nodes[node].down = nodes[down]


# [1] -> [2] -> [3] -> [8] -> [10]
#                |      |
#                |     [9]
#                |
#               [4] -> [5] -> [6]
#                              |
#                             [7]
if __name__ == "__main__":
    unittest.main()
    # AbstractSuite(Test, [flatten_linked_list]).run()
