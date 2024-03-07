import math

from typing import Any


class Node:
    def __init__(self, value: Any, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def max_path_sum(root: Node | None) -> int | float:
    if root is None:
        return -math.inf

    if root.left is None and root.right is None:
        return root.value

    return root.value + max(max_path_sum(root.left), max_path_sum(root.right))


if __name__ == "__main__":
    _root = Node(5, Node(11, Node(4), Node(2)), Node(3, right=Node(1)))
    assert max_path_sum(_root) == 20
    assert max_path_sum(None) == -math.inf
