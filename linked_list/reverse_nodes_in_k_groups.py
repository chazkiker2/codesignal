def check_remaining_node_count(list_node, k):
    index = 0
    current_node = list_node
    failed = False
    while index < k and not failed:
        if current_node is None:
            failed = True
        else:
            current_node = current_node.next
        index += 1

    return failed


def reverse_nodes_in_k_groups(list_node, k):
    current_node = list_node
    next_node = prev_node = None
    count = 0

    while current_node is not None and count < k:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
        count += 1

    if next_node is not None:
        multiples_available = check_remaining_node_count(next_node, k)

        if not multiples_available:
            list_node.next = reverse_nodes_in_k_groups(next_node, k)
        else:
            list_node.next = next_node

        return prev_node
