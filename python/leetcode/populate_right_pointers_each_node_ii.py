"""
Given a binary tree

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



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100

"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def process_child(self, child, prev, leftmost):
        if child:

            # If the "prev" pointer is alread set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if prev:
                prev.next = child
            else:
                # Else it means this child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = child
            prev = child
        return prev, leftmost

    def connect_o1_space(self, root: Node) -> Node:
        if not root:
            return root

        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root

        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:

            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev = None
            current = leftmost

            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None

            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while current:

                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                prev, leftmost = self.process_child(
                    current.left, prev, leftmost
                )
                prev, leftmost = self.process_child(
                    current.right, prev, leftmost
                )

                # Move onto the next node.
                current = current.next

        return root

    def connect(self, root: Node) -> Node:
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
