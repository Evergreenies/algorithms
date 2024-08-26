"""
Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \\
  3   7
 / \\   \\
2   4    8
"""


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left, self.right = None, None


def build_tree_from_postorder(arr: list[int]) -> None | Node:
    if not arr:
        return None

    # last element of postorder is the root of the current subtree
    root_value = arr[-1]
    root = Node(root_value)

    # find the index where the right subtree startes
    # this is the first element greater than the root root_value
    index = 0
    while index < len(arr) - 1 and arr[index] < root_value:
        index += 1

    # recursivelly build left and right subtree
    root.left = build_tree_from_postorder(arr[:index])
    root.right = build_tree_from_postorder(arr[index:-1])

    return root


def print_preorder(node: Node | None) -> None:
    if not node:
        return

    print(node.value, end=" ")
    print_preorder(node.left)
    print_preorder(node.right)


print_preorder(build_tree_from_postorder([2, 4, 3, 8, 7, 5]))
print()
