def is_valid(expr, target):
    """
    Evaluates an expression and checks if it equals the target value.

    Args:
        expr: A string representing the mathematical expression.
        target: The target value to reach.

    Returns:
        True if the expression evaluates to the target value, False otherwise.
    """
    try:
        return eval(expr) == target
    except ZeroDivisionError:
        return False


def play_24_recursive(numbers, index, expr):
    """
    Recursively explores all possible combinations of operators and parentheses
    to reach the target value (24).

    Args:
        numbers: The list of four integers.
        index: The current index in the numbers list.
        expr: The current expression being built.

    Returns:
        True if a valid expression to reach 24 is found, False otherwise.
    """
    if index == len(numbers):  # Reached the end of the list
        return is_valid(expr, 24)

    # Try all possible placements of operators and parentheses
    for i in range(index, len(numbers)):
        # Case 1: No operator between current and next number
        next_expr = expr + str(numbers[index])
        if play_24_recursive(numbers, index + 1, next_expr):
            return True

        # Case 2: Add operator between current and next number
        for op in "+-*/":
            remaining_expr = str(numbers[index]) + op + str(numbers[i + 1 :])
            if index + 1 < len(numbers):
                remaining_expr = (
                    "(" + remaining_expr + ")"
                )  # Enclose remaining for order of operations
            next_expr = expr + op + remaining_expr
            if play_24_recursive(numbers, index + 1, next_expr):
                return True

    return False


def play_24(numbers):
    """
    Checks if it's possible to reach the target value (24) using the given numbers.

    Args:
        numbers: A list of four integers between 1 and 9.

    Returns:
        True if it's possible to reach 24, False otherwise.
    """
    return play_24_recursive(numbers, 0, "")


# Example usage
numbers = [5, 2, 7, 8]
result = play_24(numbers)
print(result)  # Output: True
