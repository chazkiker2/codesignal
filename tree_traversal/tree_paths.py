"""
Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively (noden representing the leaf).

Example

For

t = {
    "value": 5,
    "prev": {
        "value": 2,
        "prev": {
            "value": 10,
            "prev": null,
            "next": null
        },
        "next": {
            "value": 4,
            "prev": null,
            "next": null
        }
    },
    "next": {
        "value": -3,
        "prev": null,
        "next": null
    }
}
the output should be
treePaths(t) = ["5->2->10", "5->2->4", "5->-3"].

The given tree looks like this:

    5
   / \
  2  -3
 / \
10  4
Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 710,
-1000 ≤ node value ≤ 1000.

[output] array.string

The root-to-leaf paths, sorted by the leaves in the order that they appear in the pre-order traversal (i.e. from the leftmost leaf to the rightmost).


"""
from typing import List


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def tree_paths(root):
    if root is None: return []
    if root.left is None and root.right is None:
        return [f"{root.value}"]

    left_sub = tree_paths(root.left)
    right_sub = tree_paths(root.right)
    full_sub = left_sub + right_sub

    lst = []
    for leaf in full_sub:
        lst.append(f"{root.val}->{leaf}")
    return lst

#
# def tree_paths(t: Tree) -> List[str]:
#     path = []
#     strs = []
#     def get_paths_rec(root: Tree, path, length: int):
#         if root is None:
#             return
#
#         if len(path) > length:
#             path[length] = root.value
#
#         else:
#             path.append(root.value)
#
#         length += 1
#
#         if root.prev is None and root.next is None:
#             strs.append(iter_arr(path))
#
#         else:
#             get_paths_rec(root.prev, path, length)
#             get_paths_rec(root.next, path, length)
#
#     get_paths_rec(t, path, 0)
#
#     return strs
#
#
# def iter_arr(arr):
#     return_str = ""
#     for el in arr:
#         return_str += f"{el}-> "
#     return return_str[:-3]
