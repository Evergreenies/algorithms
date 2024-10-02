"""
Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""

from typing import List, Tuple


class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def inorder_traversal(node: TreeNode | None) -> List:
    if node is None:
        return []

    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)


def find_two_nodes_with_sum(node: TreeNode, k: int) -> Tuple | None:
    arr = inorder_traversal(node)
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == k:
            return arr[left], arr[right]
        elif current_sum < k:
            left += 1
        else:
            right -= 1

    return None


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15, TreeNode(11), TreeNode(15))

print(find_two_nodes_with_sum(root, 20))
