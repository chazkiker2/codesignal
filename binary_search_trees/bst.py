# Binary Search Tree
# ------------------
# class ListNode: # for analogy
#   def __init__(self, val):
#       self.value = val
#       self.next = None

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.value})"


def search(root, value):
    cur = root
    while cur is not None:
        # compare to see if we have found it
        if cur.value == value:
            return True  # True, we found it

        # if not, go to proper next node
        if value < cur.value:
            cur = cur.left
        else:  # value > cur.value
            cur = cur.right

    # if we make it here, we did not find it
    return False


def search_recursive(cur, value):
    if cur is None:
        return False
    if cur.value == value:
        return True
    if value < cur.value:
        return search_recursive(cur.left, value)
    else:
        return search_recursive(cur.right, value)


def pre_order(cur):
    if cur is None:
        return
    print(cur.value)
    # go as far left and as far right as possible
    pre_order(cur.left)
    pre_order(cur.right)


def in_order(cur):
    if cur is None:
        return

    in_order(cur.left)
    print(cur.value)
    in_order(cur.right)


def in_order_to_list(cur, lst):
    if cur is None:
        return

    in_order_to_list(cur.left, lst)
    lst.append(cur.value)
    in_order_to_list(cur.right, lst)


def max_depth(root):
    if root is None:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(6)
    print(max_depth(root))
    in_order(root)

    print(search(root, 2))  # -> True
    print(search(root, 5))  # -> True
    print(search(root, 99))  # -> False
    print(search_recursive(root, 2))  # -> True
    print(search_recursive(root, 5))  # -> True
    print(search_recursive(root, 99))  # -> False
