"""
You have N stones in a row, and would like to create from them a pyramid. This pyramid should be
constructed such that the height of each stone increases by one until reaching the tallest stone,
after which the heights decrease by one. In addition, the start and end stones of the pyramid
should each be one stone high.

You can change the height of any stone by paying a cost of 1 unit to lower its height by 1, as
many times as necessary. Given this information, determine the lowest cost method to produce
this pyramid.

For example, given the stones [1, 1, 3, 3, 2, 1],
the optimal solution is to pay 2 to create [0, 1, 2, 3, 2, 1].
"""


def min_cost_to_pyramid(stones: list[int]) -> int | float:
    length = len(stones)
    if length < 3:
        return 0

    left, right = [0] * length, [0] * length

    # left traverse
    left[0] = min(stones[0], 1)
    for index in range(1, length):
        left[index] = min(stones[index], min(left[index - 1] + 1, index + 1))

    # right traverse
    right[length - 1] = min(stones[length - 1], 1)
    for index in range(length - 2, -1, -1):
        right[index] = min(stones[index], min(right[index + 1] + 1, length - index))

    # find minimum possible
    total = [0] * length
    for index in range(length):
        total[index] = min(right[index], left[index])

    # find maximum height of pyramid
    max_idx = 0
    for index in range(length):
        if total[index] > total[max_idx]:
            max_idx = index

    cost, height = 0, total[max_idx]
    # calculate max of left half
    for index in range(max_idx, -1, -1):
        cost += stones[index] - height
        height = max(0, height - 1)

    # calculate cost of right half
    height = total[max_idx] - 1
    for index in range(max_idx + 1, height):
        cost += stones[index] - height
        height = max(0, height - 1)

    return cost


print(min_cost_to_pyramid([1, 1, 3, 3, 2, 1]))
