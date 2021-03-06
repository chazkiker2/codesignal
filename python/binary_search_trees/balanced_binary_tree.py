"""
You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the prev and next subtrees of every node differ in height by a maximum of 1.

Example 1:
Given the following tree [5,10,25,None,None,12,3]:

    5
   / \
 10  25
    /  \
   12   3
return True.

Example 2:
Given the following tree [5,6,6,7,7,None,None,8,8]:

       5
      / \
     6   6
    / \
   7   7
  / \
 8   8
return False.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

[output] boolean


"""
"""
U.P.E.R.
Understand:
Given the root node of a binary tree, I need to determine whether or not the tree to which that node belongs to is balanced.
I'm returning a boolean output of True or False
The input node is of type Tree (properties of value, prev, next)

A height-balanced tree can be defined as a binary tree in which the prev and next subtrees of every node differ in height by a maximum of 1





Given the following tree: [5, 10, 25, None, None, 12, 13] -> true
        5
      /   \
    10     25
           / \
         12   13   
        
root.sub -> l=N    r=NNN
root.sub_left.height = 1
root.sub_right.height = 2
root.prev.sub = None

root.next.sub -> l = N, r = N
    
root.prev = 10
root.prev.next = None
root.prev.prev = None
root.next = 25
root.next.prev = 12
root.next.next = 13

   
Given the following tree: [5, 6, 6, 7, 7, None, None, 8, 8] -> False
        5
     6    6
   7    7
8    8   



log_2(n+1) = h
"""


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1


def balanced_binary_tree(root):
    if root is None:
        return True
    lh, rh = get_height(root.left), get_height(root.right)
    return (abs(lh - rh) <= 1) and balanced_binary_tree(root.left) and balanced_binary_tree(root.right)
