"""
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
"""


def fib(num: int) -> int:
    if num <= 1:
        return num

    old_sum, latest_sum = 0, 1
    for _ in range(2, num + 1):
        current_sum = latest_sum + old_sum
        old_sum = latest_sum
        latest_sum = current_sum

    return latest_sum


if __name__ == "__main__":
    assert fib(5) == 5
