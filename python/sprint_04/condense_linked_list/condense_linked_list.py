"""
Given a linked list of integers, remove any nodes from the linked list that
have values that have previously occurred in the linked list.
Your function should return a reference to the head of the updated linked list.

Example:
Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer node
    The head node of the linked list.

[output] linkedlist.integer
    The head node of the updated linked list.
"""


# Singly-Linked lists are already defined with this interface
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def condense_linked_list_first_pass(node):
    visited = {node.value}
    init_head = new_head = node
    current_node = node.next
    init_head.next = new_head.next = None

    while current_node is not None:
        if current_node.value not in visited:
            visited.add(current_node.value)
            new_head.next = ListNode(current_node.value)
            new_head = new_head.next

        current_node = current_node.next

    return init_head
