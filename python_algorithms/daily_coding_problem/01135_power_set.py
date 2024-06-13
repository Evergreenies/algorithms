"""
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""


def power_set(nums):
    power_set = [[]]  # Initialize with the empty subset

    for num in nums:
        new_subsets = []
        for subset in power_set:
            new_subset = subset + [num]
            new_subsets.append(new_subset)
        power_set.extend(new_subsets)

    return power_set


# Example usage:
nums = [1, 2, 3]
result = power_set(nums)
print(result)
