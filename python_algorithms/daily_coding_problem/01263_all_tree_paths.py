"""
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""

from typing import Any


class Node:
    def __init__(self, value: Any, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def binary_tree_paths(root: Node) -> list[list]:
    if not root:
        return []

    paths = []
    dfs(root, [], paths)

    return paths


def dfs(node: Node, current_path: list, paths: list[list]) -> None:
    current_path.append(node.value)

    if not node.left and not node.right:
        paths.append(list(current_path))
    else:
        if node.left:
            dfs(node.left, current_path.copy(), paths)

        if node.right:
            dfs(node.right, current_path.copy(), paths)

    del current_path[-1]


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)

    assert binary_tree_paths(root) == [[1, 2, 4], [1, 3, 5]]

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)

    assert binary_tree_paths(root) == [[1, 2], [1, 3, 4], [1, 3, 5]]
