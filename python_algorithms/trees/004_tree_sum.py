from typing import Any


class Node:
    def __init__(self, value: int, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def tree_sum(root: Node) -> int:
    if root is None:
        return 0
    return root.value + tree_sum(root.left) + tree_sum(root.right)


if __name__ == "__main__":
    _root = Node(1, Node(6, Node(3), Node(-6)), Node(0, right=Node(2)))
    assert tree_sum(_root) == 6
