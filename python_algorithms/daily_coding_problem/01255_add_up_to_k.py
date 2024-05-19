"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def add_up_to_k(arr: list[int], target: int) -> bool:
    if not arr:
        return False

    for index, item in enumerate(arr):
        sub = target - item
        if sub == 0:
            return True
        if sub in arr[:index] + arr[index + 1 :]:
            return True

    return False


if __name__ == "__main__":
    assert add_up_to_k([10, 15, 3, 7], 17) is True
    assert add_up_to_k([10, 15, 3, 7], 10) is True
    assert add_up_to_k([10, 10, 3, 7], 20) is True
