"""
Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""

from typing import Generator
from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def generate() -> Generator:
    root = TreeNode(-1)
    queue = deque([root])
    current_id = 2

    while queue:
        node = queue.popleft()

        node.left = TreeNode(current_id)
        queue.append(node.left)
        current_id += 1

        node.right = TreeNode(current_id)
        queue.append(node.right)
        current_id += 1

        yield node


# Initialize the generator
tree_generator = generate()

# Retrieve a limited number of nodes (finite sampling)
for _ in range(10):  # Generate 10 nodes
    node = next(tree_generator)
    print(
        f"Node Value: {node.value}, Left: {node.left.value}, Right: {node.right.value}"
    )
