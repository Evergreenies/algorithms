"""
Given a set of distinct positive integers, find the largest subset such 
that every pair of elements in the subset (i, j) satisfies either 
i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. 
Given [1, 3, 6, 24], return [1, 3, 6, 24].
"""


def largest_divisible_subset(arr: list[int]) -> list[int]:
    if not arr:
        return []

    if len(arr) <= 1:
        return arr

    arr = sorted(arr)
    result, dp = [], {}

    for num in arr:
        is_divisible = True
        for element in result:
            if (num % element) != 0 and (element % num) != 0:
                is_divisible = False
                dp[len(result)] = result
                result = [num]
                break

        if is_divisible:
            result.append(num)

    dp[len(result)] = result
    return dp[max(dp.keys())]


if __name__ == "__main__":
    assert largest_divisible_subset([3, 5, 10, 20, 21]) == [5, 10, 20]
    assert largest_divisible_subset([1, 3, 6, 24]) == [1, 3, 6, 24]
