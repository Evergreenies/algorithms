"""
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def find_gcd(arr: list[int]) -> int:
    if not arr:
        return -1

    if len(arr) == 1:
        return arr[0]

    a = arr[0]
    for b in arr[1:]:
        a = gcd(a, b)

    return a


if __name__ == "__main__":
    assert find_gcd([42, 56, 14]) == 14
    assert find_gcd([]) == -1
    assert find_gcd([1]) == 1
    assert find_gcd([0, 28]) == 28
    assert find_gcd([17, 23]) == 1
