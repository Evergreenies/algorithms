"""
Given pre-order and in-order traversals of a binary tree, write a function 
to reconstruct the tree.

For example, given the following preorder traversal:
[a, b, d, e, c, f, g]

And the following inorder traversal:
[d, b, e, a, f, c, g]
"""

from typing import Any


class Node:
    def __init__(self, value: Any, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def build_tree(preorder: list[Any], inorder: list[Any]) -> Node | None:
    if not preorder or not inorder:
        return None

    root_value = preorder[0]
    root_index = preorder.index(root_value)

    left_preorder = preorder[1 : root_index + 1]
    left_inorder = inorder[:root_index]

    right_preorder = preorder[root_index + 1 :]
    right_inorder = inorder[root_index + 1 :]

    root = Node(root_value)
    root.left = build_tree(left_preorder, left_inorder)
    root.right = build_tree(right_preorder, right_inorder)

    return root


def print_preorder(node: Node | None) -> None:
    if not node:
        return

    print(node.value, end=" ")
    print_preorder(node.left)
    print_preorder(node.right)


if __name__ == "__main__":
    preorder = ["a", "b", "d", "e", "c", "f", "g"]
    inorder = ["d", "b", "e", "a", "f", "c", "g"]
    root = build_tree(preorder, inorder)
    print_preorder(root)
    print()
