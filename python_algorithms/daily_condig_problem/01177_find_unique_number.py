"""
Given an array of integers where every integer occurs three times except 
for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""


def find_unique_number(arr: list[int]) -> int:
    eliminate_thrice, eliminate_twice = 0, 0
    for num in arr:
        eliminate_thrice = (eliminate_thrice ^ num) & ~eliminate_twice
        eliminate_twice = (eliminate_twice ^ num) & ~eliminate_thrice

    return eliminate_thrice


if __name__ == "__main__":
    assert find_unique_number([6, 1, 3, 3, 3, 6, 6]) == 1
    assert find_unique_number([13, 19, 13, 13]) == 19
    assert find_unique_number([13, 13, 13]) == 0
