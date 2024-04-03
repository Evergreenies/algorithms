"""
Given a binary search tree, find the floor and ceiling of a given integer. 
The floor is the highest element in the tree less than or equal to an integer, 
while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.
"""
from typing import Any


class Node:
    def __init__(self, value: int, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def find_floor_and_ceil_from_bst(
    root: Node, target: int
) -> tuple[int | None, int | None]:
    if root is None:
        return None, None

    floor, ceil = None, None
    current_node = root

    while current_node:
        if target == current_node.value:
            return current_node.value, current_node.value
        elif target < current_node.value:
            ceil = current_node.value
            current_node = current_node.left
        else:
            floor = current_node.value
            current_node = current_node.right

    return floor, ceil


if __name__ == "__main__":
    _root = Node(10, Node(5, Node(3), Node(7)), Node(15, right=Node(18)))

    assert find_floor_and_ceil_from_bst(_root, 12) == (10, 15)
    assert find_floor_and_ceil_from_bst(_root, 20) == (18, None)
