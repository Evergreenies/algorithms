r"""
Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def level_order_traversal(root: TreeNode) -> None:
    if not root:
        return

    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    print()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

level_order_traversal(root)
