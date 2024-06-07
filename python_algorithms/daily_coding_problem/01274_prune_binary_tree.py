"""
Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:

   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.

"""


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def prune_tree(root: Node | None):
    if not root:
        return

    root.left = prune_tree(root.left)
    root.right = prune_tree(root.right)

    if root.value == 0 and root.left is None and root.right is None:
        return

    return root


def inorder_traversal(root: Node | None):
    if not root:
        return

    inorder_traversal(root.left)
    print(root.value, end=" ")
    inorder_traversal(root.right)


_root = Node(0)
_root.left = Node(1)
_root.right = Node(0)
_root.right.left = Node(1)
_root.right.right = Node(0)
_root.right.right.left = Node(0)
_root.right.right.right = Node(0)

pruned_tree = prune_tree(_root)
inorder_traversal(pruned_tree)
print()
