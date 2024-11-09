"""
Given a string consisting of parentheses, single digits, and positive and negative signs,
convert the string into a mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4.
"""


def calculate(expression: str) -> int | float:
    stack, result, num, sign = [], 0, 0, 1

    for char in expression:
        if char.isdigit():
            # it handles case if number is multi digit (like 12, 123, 1, etc)
            num = num * 10 + float(char)
        elif char == "+":
            result += sign * num
            num, sign = 0, 1
        elif char == "-":
            result += sign * num
            num, sign = 0, -1
        elif char == "(":
            stack.append(result)
            stack.append(sign)
            result, sign = 0, 1
        elif char == ")":
            result += sign * num
            num = 0
            result *= stack.pop()
            result += stack.pop()

    result += sign * num

    return result


print(calculate("-1+(2+3)"))
