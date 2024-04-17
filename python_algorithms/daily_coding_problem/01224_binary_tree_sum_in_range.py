"""
Given a binary search tree and a range [a, b] (inclusive), return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \\/ \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).
"""

from typing import Any


class TreeNode:
    def __init__(self, value: int = 0, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def range_sum_bst(root: TreeNode, low: int, high: int) -> int:
    if not root:
        return 0

    if low <= root.value <= high:
        return (
            root.value
            + range_sum_bst(root.left, low, high)
            + range_sum_bst(root.right, low, high)
        )
    elif low > root.value:
        return range_sum_bst(root.right, low, high)
    else:
        return range_sum_bst(root.left, low, high)


if __name__ == "__main__":
    _root = TreeNode(
        5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8, TreeNode(6), TreeNode(10))
    )
    assert range_sum_bst(_root, 4, 9) == 23
