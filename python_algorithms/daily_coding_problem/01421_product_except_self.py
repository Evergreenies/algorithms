"""
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product_except_self(arr: list) -> list:
    length = len(arr)
    if length == 0:
        return []

    output = [1] * length
    left_product = 1
    for index in range(length):
        output[index] = left_product
        left_product *= arr[index]

    right_product = 1
    for index in range(length - 1, -1, -1):
        output[index] *= right_product
        right_product *= arr[index]

    return output


print(product_except_self([1, 2, 3, 4, 5]))
