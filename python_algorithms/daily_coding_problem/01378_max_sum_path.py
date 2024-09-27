"""
Given a binary tree of integers, find the maximum path sum between two nodes. The path must go
through at least one node, and does not need to go through the root.
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode | None) -> int | float:
    max_sum = float("-inf")

    def helper(node: TreeNode | None) -> float:
        nonlocal max_sum

        if not node:
            return 0

        left_max = max(helper(node.left), 0)
        right_max = max(helper(node.right), 0)

        current_max = node.value + left_max + right_max

        max_sum = max(max_sum, current_max)

        return node.value + max(left_max, right_max)

    return helper(root)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(max_path_sum(root))
