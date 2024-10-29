"""
Given a binary tree, return the level of the tree with minimum sum.
"""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def minimum_sum_leve(root: TreeNode | None) -> int | None:
    if not root:
        return None

    queue = deque([(root, 0)])
    level_sums = defaultdict(int)

    while queue:
        node, level = queue.popleft()
        level_sums[level] += node.val

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

    return min(level_sums, key=level_sums.get)


# Creating a simple binary tree:
#        1
#       / \
#      7   0
#     / \   \
#    7  -8   7
root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
root.right.right = TreeNode(7)

print(minimum_sum_leve(root))


# Creating a simple binary tree:
#        2
#       / \
#      7   0
#     / \   \
#    7  -8   0
root = TreeNode(2)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
root.right.right = TreeNode(0)

print(minimum_sum_leve(root))
