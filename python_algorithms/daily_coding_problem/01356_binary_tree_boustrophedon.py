"""
In Ancient Greece, it was common to write text with the first line going left to right, 
the second line going right to left, and continuing to go back and forth. This style 
was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \\
  2         3
 / \\       / \\
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def boustrophedon_order(root: TreeNode) -> list:
    if not root:
        return []

    result, left_to_right = [], True
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_node = []

        for _ in range(level_size):
            node = queue.popleft()
            level_node.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if left_to_right:
            result.extend(level_node)
        else:
            result.extend(level_node[::-1])

        left_to_right = not left_to_right

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(boustrophedon_order(root))
