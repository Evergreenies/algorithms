"""
Given a string of parentheses, write a function to compute the minimum number of parentheses to be 
removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should 
return 2, since we must remove all of them.
"""


def make_parenthesis_balanced(string: str) -> int:
    stack = []
    for index, char in enumerate(string):
        if char == "(":
            stack.append(index)
        elif char == ")":
            if stack and string[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(index)

    return len(stack)


if __name__ == "__main__":
    assert make_parenthesis_balanced("()())()") == 1
    assert make_parenthesis_balanced(")(") == 2
    assert make_parenthesis_balanced(")()") == 1
