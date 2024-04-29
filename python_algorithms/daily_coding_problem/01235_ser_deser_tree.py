"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Node) -> str:
    result = []

    def preorder_dfs(node: Node | None) -> None:
        if not node:
            result.append("#")
            return

        result.append(str(node.val))
        preorder_dfs(node.left)
        preorder_dfs(node.right)

    preorder_dfs(root)

    return ",".join(result)


def deserialize(string: str) -> Node | None:
    nodes = string.split(",")

    def build_tree(index: int) -> Node | None:
        if nodes[index] == "#":
            return

        root = Node(nodes[index])
        index += 1
        root.left = build_tree(index)
        index += 1
        root.right = build_tree(index)

        return root

    return build_tree(0)


if __name__ == "__main__":
    node = Node("root", Node("left", Node("left.left")), Node("right"))
    assert deserialize(serialize(node)).left.left.val == "left.left"
