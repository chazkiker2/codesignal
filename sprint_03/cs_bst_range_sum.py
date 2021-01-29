"""
You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of values of all
the nodes with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.

Example 1:

    Input:
        root = [10, 5, 15, 3, 7, null, 18]
        lower = 7
        upper = 15

             10
             / \
            5  15
           / \    \
          3   7    18

    Output:
        32


Example 2:

    Input:
        root = [10,5,15,3,7,13,18,1,null,6]
        lower = 6
        upper = 10

               10
              /  \
           5       15
         / \     /   \
        3   7  13   18
       /   /
      1   6

    Output: 23

[execution time limit] 4 seconds (py3)

[I/O] (root: Tree.int, lower: int, upper: int) -> int

[input] tree.integer root

[input] integer lower

[input] integer upper

[output] integer


"""
from collections import deque


# Binary trees are already defined with this interface:
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def cs_bst_range_sum_draft(root, lower, upper):
    if not root:
        return 0

    nodes = []

    def in_order_trav(node):
        nonlocal nodes

        if node.left:
            in_order_trav(node.left)

        nodes.append(node.value)

        if node.right:
            in_order_trav(node.right)

    in_order_trav(root)

    sum_count = 0
    stack = deque()
    stack.append(root)
    counting = False
    while len(stack) > 0:
        current = stack.pop()
        if current.left:
            stack.append(current.left)

        if current.value == lower:
            counting = True

        if counting:
            sum_count += current.value

        if current.value == upper:
            return counting

        if current.right:
            stack.append(current.right)

    return sum_count


def cs_bst_range_sum(root, lower, upper):
    if not root:
        return 0

    nodes = []

    def in_order_trav(node):
        nonlocal nodes

        if node.left:
            in_order_trav(node.left)

        if lower <= node.value <= upper:
            nodes.append(node.value)

        if node.right:
            in_order_trav(node.right)

    in_order_trav(root)

    return sum(nodes)


if __name__ == '__main__':
    input_1 = {
        "root": {
            "value": 10,
            "left": {
                "value": 5,
                "left": {
                    "value": 3,
                    "left": None,
                    "right": None
                },
                "right": {
                    "value": 7,
                    "left": None,
                    "right": None
                }
            },
            "right": {
                "value": 15,
                "left": None,
                "right": {
                    "value": 18,
                    "left": None,
                    "right": None
                }
            }
        },
        "lower": 7,
        "upper": 15,
    }
    # tree1 = Tree(10)
    # tree1.right = Tree(7)
    # tree1.left = Tree(5)
    expected_1 = 32
    actual_1 = cs_bst_range_sum(input_1["root"], input_1["lower"], input_1["upper"])

    input_2 = {
        "root": {
            "value": 10,
            "left": {
                "value": 5,
                "left": {
                    "value": 3,
                    "left": {
                        "value": 1,
                        "left": None,
                        "right": None
                    },
                    "right": None
                },
                "right": {
                    "value": 7,
                    "left": {
                        "value": 6,
                        "left": None,
                        "right": None
                    },
                    "right": None
                }
            },
            "right": {
                "value": 15,
                "left": {
                    "value": 13,
                    "left": None,
                    "right": None
                },
                "right": {
                    "value": 18,
                    "left": None,
                    "right": None
                }
            }
        },
        "lower": 6,
        "upper": 10
    }
    expected_2 = 23
    actual_2 = cs_bst_range_sum(input_2["root"], input_2["lower"], input_2["upper"])

    input_3 = {
        "root": {
            "value": 1,
            "left": {
                "value": 2,
                "left": {
                    "value": 5,
                    "left": None,
                    "right": {
                        "value": 3,
                        "left": {
                            "value": 2,
                            "left": {
                                "value": 3,
                                "left": None,
                                "right": None
                            },
                            "right": {
                                "value": 1,
                                "left": None,
                                "right": None
                            }
                        },
                        "right": None
                    }
                },
                "right": None
            },
            "right": {
                "value": 2,
                "left": None,
                "right": {
                    "value": 3,
                    "left": {
                        "value": 5,
                        "left": None,
                        "right": None
                    },
                    "right": {
                        "value": 2,
                        "left": {
                            "value": 3,
                            "left": None,
                            "right": None
                        },
                        "right": {
                            "value": 1,
                            "left": None,
                            "right": None
                        }
                    }
                }
            }
        },
        "lower": 10,
        "upper": 15
    }
    expected3 = 0

    actual3 = cs_bst_range_sum(input_3["root"], input_3["lower"], input_3["upper"])

    print("-------------------------------------")
    print("TEST 1")
    print(f"Expected: {expected_1}")
    print(f"Actual: {actual_1}")
    print(f"Passed: {expected_1 == actual_1}")
    print("-------------------------------------")
    print("TEST 2")
    print(f"Expected: {expected_2}")
    print(f"Actual: {actual_2}")
    print(f"Passed: {expected_2 == actual_2}")
    print("-------------------------------------")
    print("TEST 3")
    print(f"Expected: {expected3}")
    print(f"Actual: {actual3}")
    print(f"Passed: {expected3 == actual3}")
    print("-------------------------------------")
