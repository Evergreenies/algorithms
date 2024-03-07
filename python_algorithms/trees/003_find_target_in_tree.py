from typing import Any


class Node:
    def __init__(self, value: Any, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def find_target_in_tree_by_dfs(root: Node, target: Any) -> bool:
    if root is None:
        return False

    stack = [root]
    while len(stack) > 0:
        current = stack.pop()

        if current.value == target:
            return True

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return False


def find_target_in_tree_by_bfs(root: Node, target: Any) -> bool:
    if root is Node:
        return False

    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)

        if current.value == target:
            return True

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return False


if __name__ == "__main__":
    _root = Node("a", Node("b", Node("d"), Node("e")), Node("c", None, Node("f")))
    assert find_target_in_tree_by_dfs(_root, "a") is True
    assert find_target_in_tree_by_dfs(_root, "e") is True
    assert find_target_in_tree_by_dfs(_root, "f") is True
    assert find_target_in_tree_by_dfs(_root, "z") is False

    assert find_target_in_tree_by_bfs(_root, "a") is True
    assert find_target_in_tree_by_bfs(_root, "e") is True
    assert find_target_in_tree_by_bfs(_root, "f") is True
    assert find_target_in_tree_by_bfs(_root, "z") is False
