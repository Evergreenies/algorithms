"""
Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have 
different parents. For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \\   \
4   5   6
Given a binary tree and a particular node, find all cousins of that node.
"""

from typing import Any


class TreeNode:
    def __init__(self, value: Any, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def find_cousins(root: TreeNode, cousins_of_node: TreeNode) -> list[Any]:
    cousins = []
    dfs(
        root,
        cousins_of_node,
        None,
        0,
        find_level_of_target(root, cousins_of_node),
        cousins,
    )

    return cousins


def find_level_of_target(
    root: TreeNode, cousins_of_target: TreeNode, level: int = 1
) -> int:
    if not root:
        return -1

    if root is cousins_of_target:
        return level

    left_level = find_level_of_target(root.left, cousins_of_target, level + 1)
    if left_level != -1:
        return left_level

    return find_level_of_target(root.right, cousins_of_target, level + 1)


def dfs(
    node: TreeNode,
    cousions_of_node: TreeNode,
    parent: TreeNode | None,
    current_level: int,
    level: int,
    cousins: list[Any],
) -> None:
    if not node:
        return

    if current_level == level and node is not parent:
        cousins.append(node.value)

    dfs(node.left, cousions_of_node, node, current_level + 1, level, cousins)
    dfs(node.right, cousions_of_node, node, current_level + 1, level, cousins)


if __name__ == "__main__":
    root = TreeNode(
        1,
        TreeNode(2, None, TreeNode(4)),
        TreeNode(3, TreeNode(5, None, TreeNode(6)), None),
    )
    target_node = root.left.right

    assert find_cousins(root, target_node) == [6]
