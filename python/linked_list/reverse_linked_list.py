# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def reverse_linked_list(list_node):
    if list_node is None or list_node.next is None:
        return list_node

    rest_of_list = reverse_linked_list(list_node)
    list_node.next.next = list_node
    list_node.next = None
    return rest_of_list
