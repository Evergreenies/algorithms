"""
Given the root to a binary search tree, find the second largest node in the tree.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_largest(node):
    current = node
    while current.right:
        current = current.right
    return current


def find_second_largest(node):
    if not node or (not node.left and not node.right):
        return (
            None  # There is no second largest if the tree has only one node or is empty
        )

    current = node

    while current:
        # Case 1: Current node is the largest, and has a left subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # Case 2: Current node is the parent of the largest, which has no children
        if current.right and not current.right.left and not current.right.right:
            return current

        current = current.right


# Example usage
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

second_largest = find_second_largest(root)
if second_largest:
    print(f"The second largest node is: {second_largest.value}")
else:
    print("There is no second largest node.")
