"""
Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.
"""


class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right, self.parent = None, None, None


def find_min(node: TreeNode) -> TreeNode:
    while node.left:
        node = node.left

    return node


def inorder_successor(node: TreeNode) -> TreeNode | None:
    if node.right:
        return find_min(node.right)

    current = node
    while current.parent and current.parent.right == current:
        current = current.parent

    return current.parent


root = TreeNode(10)
node5 = TreeNode(5)
node30 = TreeNode(30)
node22 = TreeNode(22)
node35 = TreeNode(35)

root.left = node5
root.right = node30
node5.parent = root
node30.parent = root
node30.left = node22
node30.right = node35
node22.parent = node30

print(inorder_successor(node22).value)
