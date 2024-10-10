"""
Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \\
 5      15
       /  \\
     11    15
Return the nodes 5 and 15.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(node, stack):
    while node:
        stack.append(node)
        node = node.left


def reverse_inorder_traversal(node, stack):
    while node:
        stack.append(node)
        node = node.right


def find_two_nodes_with_sum(root, K):
    if not root:
        return None

    in_stack, rev_stack = [], []

    # Initialize the two stacks
    inorder_traversal(root, in_stack)  # Start in-order traversal
    reverse_inorder_traversal(root, rev_stack)  # Start reverse in-order traversal

    # Get the first elements from both stacks
    in_node = in_stack.pop() if in_stack else None
    rev_node = rev_stack.pop() if rev_stack else None

    while in_node and rev_node and in_node != rev_node:
        current_sum = in_node.value + rev_node.value

        if current_sum == K:
            return (in_node, rev_node)
        elif current_sum < K:
            # Move the in-order pointer forward
            inorder_traversal(in_node.right, in_stack)
            in_node = in_stack.pop() if in_stack else None
        else:
            # Move the reverse in-order pointer backward
            reverse_inorder_traversal(rev_node.left, rev_stack)
            rev_node = rev_stack.pop() if rev_stack else None

    return None


# Example usage
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(11)
root.right.right = TreeNode(15)

K = 20
result = find_two_nodes_with_sum(root, K)
if result:
    print(f"Nodes with sum {K}: {result[0].value} and {result[1].value}")
else:
    print("No pair found with the given sum.")
