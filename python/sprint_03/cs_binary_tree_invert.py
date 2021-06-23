"""
Given a binary tree, write a function that inverts the tree.

Example:

Input:
     6
   /   \
  4     8
 / \   / \
2   5 7   9

Output:
     6
   /   \
  8     4
 / \   / \
9   7 5   2
[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] tree.integer


"""


#
# Binary trees are already defined with this interface:
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class InvertNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


def invert(node):
    if node is None:
        return

    temp = node
    invert(node.left)
    invert(node.right)

    temp, node.left, node.right = node.left, node.right, temp


def csBinaryTreeInvert(root):
    invert(root)
    return root
