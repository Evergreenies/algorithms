"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""


def find_contiguous_sum(arr: list[int], target: int) -> list[int]:
    current_sum, start_index = 0, 0

    for index in range(len(arr)):
        # check if current_sum is equal to target sum
        if current_sum == target:
            return arr[start_index:index]

        # add next position value to current_sum
        current_sum += arr[index]

        # if current_sum greater than target sum then adjust start_index
        while current_sum > target:
            current_sum -= arr[start_index]
            start_index += 1

    return []


if __name__ == "__main__":
    assert find_contiguous_sum([1, 2, 3, 4, 5], 9) == [2, 3, 4]
