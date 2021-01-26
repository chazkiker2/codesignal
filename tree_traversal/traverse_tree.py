"""
Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.

Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.
Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": null
    }
}
the output should be
traverseTree(t) = [1, 2, 4, 3, 5].

This t looks like this:

     1
   /   \
  2     4
   \   /
    3 5
Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

Guaranteed constraints:
0 ≤ tree size ≤ 104.

[output] array.integer

An array that contains the values at t's nodes, ordered as described above.


"""
from typing import List


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return self.queue == []


def traverse_tree(t: Tree) -> List[int]:
    nodes = []
    queue = Queue()
    queue.enqueue(t)
    while not queue.is_empty():
        current = queue.dequeue()
        if current is None:
            continue
        nodes.append(current.value)
        queue.enqueue(current.left)
        queue.enqueue(current.right)

    return nodes