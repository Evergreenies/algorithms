"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.
For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""


def find_contiguous_sum(arr: list[int], k: int) -> list[int]:
    start, current_sum = 0, 0
    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > k and start < end:
            current_sum -= arr[start]
            start += 1

        if current_sum == k:
            return arr[start : end + 1]
    return []


print(find_contiguous_sum([1, 2, 3, 4, 5], 9))
