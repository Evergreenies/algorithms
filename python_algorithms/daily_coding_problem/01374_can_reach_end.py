"""
Given an integer list where each number represents the number of hops you can make, determine whether
you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""


def can_reach_end(hops: list[int]) -> bool:
    max_reachable = 0
    for index, hop in enumerate(hops):
        if index > max_reachable:
            return False

        max_reachable = max(max_reachable, index + hop)

    return max_reachable >= len(hops) - 1


print(can_reach_end([2, 0, 1, 0]))  # Output: True
print(can_reach_end([1, 1, 0, 1]))  # Output: False
