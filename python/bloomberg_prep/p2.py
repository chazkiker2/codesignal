# Start typing here

#         B
#   C         D
# Z   F          A
#       B

# BFCB
# ZCB
# ADB

# ADB


# BFCB
# ZCB


"""
- binary tree
- each node is letter
- move up towards root -- from b to root -- BFCB
- sort lex
    - ADB, BFCB, ZCB
- given binary tree, find smallest path


APPROACH

- find every leaf,
- track their path
- once we have iterated through each path (found every single leaf)
- compare strings

- input: root of the tree

- a leaf node is a node with no left and no right child

Depth First

- if our current node has no left and no right, we have reached a leaf
    - then we have a full path
    - we want to store this somewhere to keep
- otherwise, we would append each child to our "to visit"  RECURSE
    - would pass that CURRENT_PATH in as an argument

AFTER ITER
- have each leaf node with the path to our root
"""

# define a Binary Tree Class

# Node: left, right, value


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.val = value
        self.left = left
        self.right = right


paths = []


def compare_leaf_to_root(root) -> str:
    global paths

    compare_leaf_to_root_util(root)
    paths.sort(key=lambda x: x[-1])
    # paths.sort()
    print(paths)

    return paths[0][::-1]


def compare_leaf_to_root_util(root: Node, current_path=None) -> str:
    global paths

    if not current_path:
        current_path = ""

    current_path += str(root.val)

    # - if our current node has no left and no right, we have reached a leaf
    #     - then we have a full path
    #     - we want to store this somewhere to keep
    if not root.right and not root.left:
        # then we have a leaf node.
        # we'd want this path to be compared at some point
        # shortest_path param
        paths.append(current_path)

    if root.right:
        compare_leaf_to_root_util(root.right, current_path)

    if root.left:
        compare_leaf_to_root_util(root.left, current_path)

    # - otherwise, we would append each child to our "to visit"  RECURSE
    #     - would pass that CURRENT_PATH in as an argument

    # AFTER ITER
    # - have each leaf node with the path to our root


if __name__ == "__main__":
    #         B
    #   C         D
    # Z   F          A
    #       B

    # ADB
    # BFCB
    # ZCB

    root = Node("B")
    root.right = Node("D")
    root.left = Node("C")
    root.left.left = Node("Z")
    root.left.right = Node("F")
    root.left.right.right = Node("B")
    root.right.right = Node("A")

    shortest = compare_leaf_to_root(root)

    print(shortest)
