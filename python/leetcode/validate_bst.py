"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


import unittest
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]

        while stack:
            root, lo, hi = stack.pop()

            if not root:
                continue

            val = root.val

            if val <= lo or val >= hi:
                return False

            stack.extend([(root.right, val, hi), (root.left, lo, val)])

        return True


class Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.fn = Solution().isValidBST

    def test_001(self):
        # [2, 1, 3]
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(self.fn(root))


if __name__ == "__main__":
    unittest.main()
