"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes v and w as the lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself).”
"""


class TreeNode:
    def __init__(self, value, left=None, right=None, parent=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def lowest_common_ancestor(p, q):
    ancestors = set()

    while p:
        ancestors.add(p)
        p = p.parent

    while q:
        if q in ancestors:
            return q.value

        q = q.parent

    return


if __name__ == "__main__":
    root = TreeNode(3)
    node5 = TreeNode(5, parent=root)
    node1 = TreeNode(1, parent=root)
    root.left = node5
    root.right = node1
    node6 = TreeNode(6, parent=node5)
    node2 = TreeNode(2, parent=node5)
    node5.left = node6
    node5.right = node2
    node0 = TreeNode(0, parent=node1)
    node8 = TreeNode(8, parent=node1)
    node1.left = node0
    node1.right = node8
    node7 = TreeNode(7, parent=node2)
    node4 = TreeNode(4, parent=node2)
    node2.left = node7
    node2.right = node4

    assert lowest_common_ancestor(node7, node4) == 2
