"""
Given a string of parentheses, find the balanced string that can be produced from it using the
minimum number of insertions and deletions. If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".
"""


def balanced_parenthesis(string: str) -> str:
    stack, result = [], []
    for char in string:
        if char == "(":
            stack.append("(")
            result.append("(")
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                result.append(")")
            else:
                stack.append(")")
                result.append(")")

    print(f"{stack=} | {result=}")
    while stack:
        if stack[-1] == "(":
            result.append(")")
        if stack[-1] == ")":
            result1 = ["("]
            result1.extend(result)
            result = result1
        stack.pop()

    print(f"{stack=} | {result=}")
    return "".join(result)


assert balanced_parenthesis("(()") == "(())", "it must give (())"
assert balanced_parenthesis("(((") == "((()))"
assert balanced_parenthesis(")))") == "((()))"
