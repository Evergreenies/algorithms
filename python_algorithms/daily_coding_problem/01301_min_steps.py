"""
Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.

On the ith jump, you may move exactly i places to the left or right.

Find a path with the fewest number of jumps required to get from 0 to N.
"""


def min_jump_greedy(target: int) -> int:
    current_position, jumps = 0, 0
    while current_position < target:
        if target - current_position == jumps + 1:
            current_position = target
            jumps += 1
            break

        current_position = min(target, current_position + jumps)
        jumps += 1

    return jumps if current_position == target else -1


print(min_jump_greedy(7))
