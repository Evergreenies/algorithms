"""
Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum 
of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree should match 
that input node.
"""

from typing import Any


class TreeNode:
    def __init__(self, value: int = 0, left: Any = None, right: Any = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def merge_two_lists(list1: TreeNode, list2: TreeNode) -> TreeNode:
    if not list1:
        return list2
    elif not list2:
        return list1

    new_node = TreeNode(list1.value + list2.value)
    new_node.left = merge_two_lists(list1.left, list2.left)
    new_node.right = merge_two_lists(list1.right, list2.right)

    return new_node


def print_tree(root: TreeNode) -> None:
    if not root:
        return

    queue = [root]
    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.pop(0)
            print(f"{current_node.value} -> ", end="")
            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

    print("None")


if __name__ == "__main__":
    root1 = TreeNode(10, TreeNode(20), TreeNode(30))
    root2 = TreeNode(40, TreeNode(50), TreeNode(60))
    merged_tree = merge_two_lists(root1, root2)
    print_tree(merged_tree)
