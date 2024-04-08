"""
Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.

For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.
"""


def min_steps_to_one(num: int) -> int:
    dp = [0 for _ in range(num + 1)]
    dp[0] = 1

    for index in range(2, num + 1):
        min_steps = float("inf")
        min_steps = min(min_steps, dp[index - 1] + 1)

        for index_j in range(1, int(index**0.5) + 1):
            if index % index_j:
                min_steps = min(min_steps, dp[index // index_j] + 1)

        dp[index] = int(min_steps)

    return dp[num]


if __name__ == "__main__":
    # TODO: Pending correction
    assert min_steps_to_one(100) == 4
    assert min_steps_to_one(64) == 4
