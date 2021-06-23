"""
Note: Your solution should have O(l.length) time complexity and O(1) space complexity, since this is what you will be asked to accomplish in an interview.

Given a singly linked list, reverse and return it.

Example

For l = [1, 2, 3, 4, 5], the output should be
reverseLinkedList(l) = [5, 4, 3, 2, 1].

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ l.length ≤ 105,
-109 ≤ l.value ≤ 109.

[output] linkedlist.integer

Reversed l.


"""


class ListNode(object):
    _slots_ = ('value', 'next')

    def __init__(self, x):
        self.value = x
        self.next = None


def reverseLinkedList(l):
    if l is None or l.next is None:  # if list is empty we've reached the end
        return l

    rest_of_list = reverseLinkedList(l.next)

    l.next.next = l
    l.next = None

    return rest_of_list

    # current_node = l
    # prev_node, next_node = None, None
    # while current_node is not None:
    #     next_node = current_node.next
    #     current_node.next = next_node
    #     prev_node, current_node = current_node, prev_node
    #
    #
    # list_ = reverseLinkedList(l)


# if __name__ == "main":
#     # [1, 2, 3, 4, 5]
nodes = [n1, n2, n3, n4, n5] = [ListNode(i) for i in range(1, 6)]
# for node in nodes:
#     print(node.value)
new_head = reverseLinkedList(n1)

reversed_nodes = []
current = new_head
while current.next is not None:
    reversed_nodes.append(current)
    current = current.next
print(len(reversed_nodes))

# print(new_head)
# for node in nodes:
#     print(node.value)
