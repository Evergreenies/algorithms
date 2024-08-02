"""
Given a sorted array, convert it into a height-balanced binary search tree.
"""


class Node:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left, self.right = left, right


def sorted_array_to_bst(arr: list[int]):
    if not arr:
        return None

    middle = len(arr) // 2
    root = Node(arr[middle])
    root.left = sorted_array_to_bst(arr[:middle])
    root.right = sorted_array_to_bst(arr[middle + 1 :])

    return root


def inorder_traversal(root):
    if not root:
        return []

    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)


print(inorder_traversal(sorted_array_to_bst([-10, -3, 0, 5, 9])))
