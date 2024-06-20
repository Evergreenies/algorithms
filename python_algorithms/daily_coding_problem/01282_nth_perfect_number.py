"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""


def digits_sum(number: int) -> int:
    return sum(int(num) for num in str(number))


def nth_perfect_number(number: int) -> int:
    count, num = 0, 18

    while count < number:
        num += 1

        if digits_sum(num) == 10:
            count += 1

    return num


assert nth_perfect_number(1) == 19
assert nth_perfect_number(2) == 28
assert nth_perfect_number(3) == 37
