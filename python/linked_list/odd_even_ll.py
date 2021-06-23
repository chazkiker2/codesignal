from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return f"Node({self.val}) -> {self.next}"


def odd_even_list(head: ListNode) -> Optional[ListNode]:
    """
    Test Cases:
    head = [5, 6, 8, 10]
    output --> [5, 8, 6, 10]
    Plan:
    1. Check edge case of the given input is empty.
    2. Using the "Dummy Node" pattern, create a new linked list for odd nodes and one for even nodes.
    3. Iterate through the given list and add the even nodes to the even dummy list and the odd nodes to the odd dummy list.
    4. Concatenate the odd dummy list with the even dummy list.
    T: O(n)
    S: O(1)
    """

    if head is None:
        return
    odd_dummy = ListNode('*')
    even_dummy = ListNode('*')
    odd_curr = odd_dummy
    even_curr = even_dummy
    counter = 1
    curr = head
    while curr is not None:
        if counter % 2 == 0:
            even_curr.next = curr
            even_curr = even_curr.next
        else:
            odd_curr.next = curr
            odd_curr = odd_curr.next
        counter += 1
        temp = curr.next
        curr.next = None
        curr = temp
    odd_curr.next = even_dummy.next
    return odd_dummy.next


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]

    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = ListNode(5)

    x = odd_even_list(h)
    print(f"RETURNED: {x}")

    # ListNode.odd_even_list(ListNode, head=[1, 2, 3, 4, 5])
