"""
Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum 
of all values under a node, including the node itself.
"""

from typing import Any, DefaultDict
from collections import defaultdict


class TreeNode:
    def __init__(self, value: int = 0, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def dfs(node: TreeNode, subtree_sum_counts: DefaultDict) -> int:
    if not node:
        return 0

    subtree_sum = (
        node.value
        + dfs(node.left, subtree_sum_counts)
        + dfs(node.right, subtree_sum_counts)
    )
    subtree_sum_counts[subtree_sum] += 1

    return subtree_sum


def find_frequent_tree_sum(root: TreeNode) -> tuple[int | None, int]:
    subtree_sum_counts = defaultdict(int)

    dfs(root, subtree_sum_counts)

    max_count = 0
    most_frequent_sum = None
    for _sum, count in subtree_sum_counts.items():
        if count > max_count:
            max_count = count
            most_frequent_sum = _sum

    return most_frequent_sum, max_count


if __name__ == "__main__":
    root = TreeNode(5, TreeNode(1), TreeNode(9, TreeNode(5), TreeNode(2)))
    most_frequent_sum = find_frequent_tree_sum(root)
    assert most_frequent_sum[0] == 1

    root = TreeNode(5, TreeNode(2), TreeNode(-5))
    most_frequent_sum = find_frequent_tree_sum(root)
    assert most_frequent_sum[0] == 2
