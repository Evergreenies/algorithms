"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.
"""


from typing import Any


class TreeNode:
    def __init__(self, value: int = 0, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def check_unival(node: TreeNode, count: int = 0) -> tuple[bool, int | None, int]:
    if not node:
        return True, None, count

    left_unival, left_value, count = check_unival(node.left, count)
    right_unival, right_value, count = check_unival(node.right, count)

    if (
        left_unival
        and right_unival
        and (not node.left or node.value == left_value)
        and (not node.right or node.value == right_value)
    ):
        count += 1
        return True, node.value, count

    return False, None, count


def count_unival_sub_trees(root: TreeNode) -> int:
    if not root:
        return -1

    _, _, count = check_unival(node=root, count=1)

    return count


if __name__ == "__main__":
    root = TreeNode(
        0, TreeNode(1), TreeNode(0, TreeNode(1, TreeNode(1), None), TreeNode(0))
    )
    assert count_unival_sub_trees(root) == 5
