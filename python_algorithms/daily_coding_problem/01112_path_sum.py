"""
Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \\
5    5
\\     \\
   2    1
       /
     -1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minPathSum(self, root: TreeNode) -> int:
        """
        Finds the minimum path sum from root to a leaf in a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            The minimum path sum from root to a leaf.
        """
        if not root:
            return float("inf")  # Infinity for empty tree

        min_sum = float("inf")  # Initialize with infinity

        def dfs(node, current_sum):
            """
            Performs a depth-first search to find the minimum path sum.

            Args:
                node: The current node in the traversal.
                current_sum: The current path sum from root to the current node.
            """
            nonlocal min_sum  # Access the non-local variable

            current_sum += node.val
            if not node.left and not node.right:  # Leaf node
                min_sum = min(min_sum, current_sum)
            if node.left:
                dfs(node.left, current_sum)
            if node.right:
                dfs(node.right, current_sum)

        dfs(root, 0)
        return min_sum


# Example usage
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(5)
root.left.right = TreeNode(2)
root.right.right = TreeNode(1)
root.right.right.left = TreeNode(-1)

min_sum = Solution().minPathSum(root)
print(min_sum)  # Output: 15
