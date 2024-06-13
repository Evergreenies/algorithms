"""
Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
"""


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def largest_bst_subtree(root: Node) -> int:
    def helper(node: Node):
        if not node:
            return (True, 0, float("inf"), float("-inf"))

        is_left_bst, left_size, left_min, left_max = helper(node.left)
        is_right_bst, right_size, right_min, right_max = helper(node.right)

        if is_left_bst and is_right_bst and left_max < node.value < right_min:
            size = left_size + right_size + 1

            return True, size, min(left_min, node.value), max(right_max, node.value)
        else:
            return False, max(left_size, right_size), 0, 0

    return helper(root)[1]


if __name__ == "__main__":
    bst = Node(10)
    bst.left = Node(5)
    bst.right = Node(15)
    bst.left.left = Node(1)
    bst.left.right = Node(8)
    bst.right.right = Node(7)

    assert largest_bst_subtree(bst) == 3
