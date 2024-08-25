"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32 bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""


def array_product(nums: list[int]) -> list[int]:
    if not nums:
        return []

    length = len(nums)
    answer = [1 for _ in range(length)]
    prefix, postfix = 1, 1

    for index in range(length):
        answer[index] = prefix
        prefix *= nums[index]

    for index in range(length-1, -1, -1):
        answer[index] *= postfix
        postfix *= nums[index]

    return answer


print(array_product([1, 2, 3, 4]))
