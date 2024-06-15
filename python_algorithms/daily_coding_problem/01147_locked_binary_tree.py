"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all
of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false.
Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise,
it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may
assume the class is used in a single-threaded program, so there is no need for actual locks or
mutexes. Each method should run in O(h), where h is the height of the tree.
"""


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

        self.parent = None
        self.locked = None
        self.locked_count = 0

    def is_locked(self) -> bool:
        return self.locked

    def can_lock_or_unlock(self) -> bool:
        current = self.parent
        while current:
            if current.locked:
                return False

            current = current.parent

        if self.locked_count > 0:
            return False

        return True

    def lock(self) -> bool:
        if self.locked:
            return False

        if not self.can_lock_or_unlock():
            return False

        current = self.parent
        while current:
            current.locked_count += 1
            current = current.parent

        return True

    def unlock(self) -> bool:
        if not self.locked:
            return False

        if not self.can_lock_or_unlock():
            return False

        self.locked = False
        current = self.parent
        while current:
            current.locked_count -= 1
            current = current.parent

        return True


def set_parent(node: TreeNode | None, parent: TreeNode | None = None):
    if node:
        node.parent = parent
        set_parent(node.left, parent)
        set_parent(node.right, parent)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Set parent pointers
set_parent(root)

# Test locking and unlocking
print(root.left.lock())  # True
print(root.left.left.lock())  # False (ancestor is locked)
print(root.left.unlock())  # True
print(root.left.left.lock())  # True (ancestor unlocked)
print(root.lock())  # False (descendant is locked)
