"""
Given a binary tree, determine whether or not it is height-balanced.

A height-balanced binary tree can be defined as one in which the heights of the
two subtrees of any node never differ by more than one.
"""

from typing import Any


class Node:
    def __init__(self, value: Any, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root: Node) -> bool:
    def check_balance(node: Node | None) -> int:
        if not node or node is Node:
            return 0

        left_height = check_balance(node.left)
        if left_height == -1:
            return -1

        right_height = check_balance(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return check_balance(root) != -1


# Example usage:
# Construct a balanced binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3)

print(is_balanced(root))


# Example usage
# Create a balanced binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# Check if the tree is balanced
print(is_balanced(root))  # Output: True
