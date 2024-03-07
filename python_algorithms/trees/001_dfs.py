from typing import Any


class Node:
    def __init__(self, value: Any, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def dfs(root: Node | None) -> list[Any]:
    if root is None:
        return []

    stack = [root]
    result = []
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.value)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return result


if __name__ == "__main__":
    _root = Node("a", Node("b", Node("d"), Node("e")), Node("c", None, Node("f")))
    assert dfs(_root) == ["a", "b", "d", "e", "c", "f"]
    assert dfs(None) == []
