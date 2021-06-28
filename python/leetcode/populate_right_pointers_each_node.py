"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""


from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        """
        Complexity Analysis

        - Time Complexity: O(N) since we process each node exactly once.
          Note that processing a node in this context means popping the node from the queue and then establishing the next pointers.
        - Space Complexity: O(N). This is a perfect binary tree which means the last level contains N/2 nodes.
          The space complexity for breadth first traversal is the space occupied by the queue which is dependent upon the
          maximum number of nodes in particular level. So, in this case, the space complexity would be O(N).
        """
        if not root:
            return root

        q = deque([root])

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                if i < size - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return root

    def connect_o1_space(self, root: Node) -> Node:
        """
        Complexity Analysis

        - Time Complexity: O(N) since we process each node exactly once.
        - Space Complexity: O(1) since we don't make use of any additional data structure for traversing nodes on a particular level like the approach in `connect` does.
        """

        if not root:
            return root

        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root

        # Once we reach the final level, we are done
        while leftmost.left:

            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the
            # corresponding links for the next level
            head = leftmost
            while head:

                # CONNECTION 1
                head.left.next = head.right

                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left

                # Progress along the list (nodes on the current level)
                head = head.next

            # Move onto the next level
            leftmost = leftmost.left

        return root
