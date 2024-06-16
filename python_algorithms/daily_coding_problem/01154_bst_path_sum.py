r"""
Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def min_path_sum(root: TreeNode) -> int | float:
    if not root:
        return 0

    def dfs(node: TreeNode, current_sum: int) -> int | float:
        if not node:
            return float("inf")

        current_sum += node.value
        if not node.left and not node.right:
            return current_sum

        left = dfs(node.left, current_sum)
        right = dfs(node.right, current_sum)

        return min(left, right)

    return dfs(root, 0)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(5)
root.left.right = TreeNode(2)
root.right.right = TreeNode(1)
root.right.right.left = TreeNode(-1)

print(min_path_sum(root))
