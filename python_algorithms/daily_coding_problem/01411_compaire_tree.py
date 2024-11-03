"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all
of this node's descendants. The tree s could also be considered as a subtree of itself.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class TreeComparision:
    def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.is_same_tree(s, t):
            return True

        return self.is_subtree(s.left, t) or self.is_subtree(s.right, t)

    def is_same_tree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False

        return self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)


# Create tree nodes for s
s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)

# Create tree nodes for t
t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)

sol = TreeComparision()
print(sol.is_subtree(s, t))
