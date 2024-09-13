"""
Given a complete binary tree, count the number of nodes in faster than O(n) time.
Recall that a complete binary tree has every level filled except the last, and the nodes in
the last level are filled starting from the left.
"""


class TreeNode:
    def __init__(self, value: int = 0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def count_nodes(root: TreeNode | None):
    def compute_height(node: TreeNode | None) -> int:
        height = 0
        while node:
            height += 1
            node = node.left

        return height

    if not root:
        return 0

    left_height = compute_height(root.left)
    right_height = compute_height(root.right)

    if left_height == right_height:
        return (2 ** (left_height + 1)) - 1

    return count_nodes(root.left) + count_nodes(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(count_nodes(root))
