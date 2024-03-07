import math

from typing import Any


class Node:
    def __init__(self, value: Any, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def find_min_value_dfs(root: Node | None) -> int | None | float:
    if root is None:
        return math.inf

    min_value = math.inf
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        if current.value < min_value:
            min_value = current.value

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return min_value


if __name__ == "__main__":
    assert find_min_value_dfs(None) == math.inf
    _root = Node(5, Node(11, Node(4), Node(15)), Node(3, right=Node(12)))
    assert find_min_value_dfs(_root) == 3
