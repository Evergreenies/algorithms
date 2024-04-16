"""
You are given a binary tree in a peculiar string representation. Each node is written in the form (lr), where l 
corresponds to the left child and r corresponds to the right child.

If either l or r is null, it will be represented as a zero. Otherwise, it will be represented by a new (lr) pair.

Here are a few examples:

A root node with no children: (00)
A root node with two children: ((00)(00))
An unbalanced tree with three consecutive left children: ((((00)0)0)0)
Given this representation, determine the depth of the tree.
"""


def max_depth(string: str) -> int:
    stack, depth = [], 0

    for char in string:
        if char == "(":
            stack.append(char)
            depth = max(depth, len(stack))
        elif char == ")":
            if stack:
                stack.pop()

    return depth


if __name__ == "__main__":
    assert max_depth("((00)(00))") == 2
    assert max_depth("(00)") == 1
    assert max_depth("((((00)0)0)0)") == 4
