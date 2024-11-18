"""
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each 
internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \\
  +    +
 / \\  / \\
3   2 4   5
You should return 45, as it is (3 + 2) * (4 + 5).
"""


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def evaluate(root: Node | None) -> int:
    if not root:
        return 0

    if not root.left and not root.right:
        return int(root.value)

    left_value = evaluate(root.left)
    right_value = evaluate(root.right)

    if root.value == "+":
        return left_value + right_value
    elif root.value == "-":
        return left_value - right_value
    elif root.value == "*":
        return left_value * right_value
    elif root.value == "/":
        if right_value == 0:
            raise ZeroDivisionError()

        return left_value // right_value
    else:
        raise ValueError(f"invalid operator {root.value}")


rt = Node("*", Node("+", Node("3"), Node("2")), Node("+", Node("4"), Node("5")))
print(evaluate(rt))
