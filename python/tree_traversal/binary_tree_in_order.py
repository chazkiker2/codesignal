"""
You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.

Example:
Input: [2,None,3,4]

   2
    \
     3
    /
   4
Output: [2,4,3]

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] array.integer
"""
from typing import List


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def binary_tree_in_order_traversal(root: Tree) -> List[int]:
    nodes = []

    def traverse_in_order(node: Tree):
        if node.left:
            traverse_in_order(node.left)
        nodes.append(node.value)
        if node.right:
            traverse_in_order(node.right)

    traverse_in_order(root)
    return nodes
