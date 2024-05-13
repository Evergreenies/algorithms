"""
Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the 
constraint that the key in the left child must be less than or equal to the root and 
the key in the right child must be greater than or equal to the root.
"""


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, item):
        new_node = Node(item)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            if item < current.value:
                if not current.left:
                    current.left = new_node
                    return

                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    return

                current = current.right

    def search(self, item):
        current = self.root
        while current:
            if item == current.value:
                return True
            elif item < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def inorder_traversal(self):
        root = self.root

        output, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                output.append(temp.value)
                root = temp.right

        return output


if __name__ == "__main__":
    bst = BST()
    bst.insert(3)
    bst.insert(5)
    bst.insert(1)
    bst.insert(2)
    bst.insert(7)

    print(bst.inorder_traversal())
