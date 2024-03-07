from typing import Any


class Node:
    def __init__(self, value: Any, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def bfs(root: Node | None) -> list[Any]:
    result = []

    if root is None:
        return result

    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current.value)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result


if __name__ == "__main__":
    _root = Node("a", Node("b", Node("d"), Node("e")), Node("c", None, Node("f")))
    assert bfs(_root) == ["a", "b", "c", "d", "e", "f"]
    assert bfs(None) == []
