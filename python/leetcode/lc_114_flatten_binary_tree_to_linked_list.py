"""
# LeetCode 114: Flatten Binary Tree to Linked List

Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
- The "linked list" should be in the same order as a [pre-order traversal] of the binary tree.

Pre-Order Traversal: Current -> Left -> Right

[Pre-Order Traversal]: https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR

## Examples

### Example 1:

- Input: root = [1,2,5,3,4,null,6]
- Output: [1,null,2,null,3,null,4,null,5,null,6]

### Example 2:

- Input: root = []
- Output: []

### Example 3:

- Input: root = [0]
- Output: [0]

### Constraints:

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

## Follow Up

Can you flatten the tree in-place (with `O(1)` extra space)?
"""


from collections import deque
import unittest
from test_util import AbstractSuite


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten_alt(self, root):
        if not root:
            return

        stack = deque([root])
        prev = None

        while stack:
            node = stack.pop()

            if node:
                stack.append(node.right)
                stack.append(node.left)

                if prev:
                    prev.right = node
                    prev.left = None
                    node.left = None

                prev = node

    def flatten_o1_space(self, root: TreeNode) -> None:
        # handle `None`
        if not root:
            return

        node = root
        while node:

            # if node has a left child, we need to rewire connections
            if node.left:
                # find rightmost node under left child
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                rightmost.right = node.right
                node.right = node.left
                node.left = None

            # implicit else: if node does not have a left child, we simply continue

            node = node.right

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Handle the null scenario
        if not root:
            return None

        START, END = 1, 2

        tail = None
        stack = deque([(root, START)])

        while stack:

            current, recursion = stack.pop()

            if not current.left and not current.right:
                tail = current
                continue

            # If the node is in the START state, it means we still
            # haven't processed it's left child yet.
            if recursion == START:

                # If the current node has a left child, we add it
                # to the stack AFTER adding the current node again
                # to the stack with the END recursion state.
                if current.left:
                    stack.append((current, END))
                    stack.append((current.left, START))
                elif current.right:

                    # In case the current node didn't have a left child
                    # we will add it's right child
                    stack.append((current.right, START))
            else:
                # If the current node is in the END recursion state,
                # that means we did process one of it's children. Left
                # if it existed, else right.
                rightNode = current.right

                # If there was a left child, there must have been a leaf
                # node and so, we would have set the tailNode
                if tail:

                    # Establish the proper connections.
                    tail.right = current.right
                    current.right = current.left
                    current.left = None
                    rightNode = tail.right

                if rightNode:
                    stack.append((rightNode, START))


class TrialTestBaseCase(unittest.TestCase):
    def assert_nodes(self, expected_list, node):
        actual_list = self.get_nodes_list(node)
        self.assertListEqual(expected_list, actual_list)

    def get_nodes_list(self, node):
        ret = []

        if not node:
            return ret

        stack = deque([node])

        while stack:
            current = stack.pop()

            ret.append(current.val)

            current.right and stack.append(current.right)
            current.left and stack.append(current.left)

        return ret

    def make_output_root(self, lst):
        dummy_head = TreeNode("*")
        dummy_head.next = root = TreeNode(lst.pop(0))

        while lst:
            root.right = TreeNode(lst.pop(0))
            root = root.right

        return dummy_head.next

    def test_001(self):
        input_root = TreeNode(1)
        input_root.left = TreeNode(2)
        input_root.right = TreeNode(5)
        input_root.left.left = TreeNode(3)
        input_root.left.right = TreeNode(4)
        input_root.right.right = TreeNode(6)

        self.fn(input_root)

        self.assert_nodes([1, 2, 3, 4, 5, 6], input_root)

    def test_002(self):
        root = None
        self.fn(root)

        self.assert_nodes([], root)

    def test_003(self):
        root = TreeNode(0)
        self.fn(root)
        self.assert_nodes([0], root)


if __name__ == "__main__":
    sol = Solution()
    suite = AbstractSuite(
        TrialTestBaseCase,
        [sol.flatten, sol.flatten_alt, sol.flatten_o1_space],
    )
    suite.run()
