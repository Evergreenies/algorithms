"""
You are given an array of length N, where each element i represents the 
number of ways we can produce i units of change. For example, [1, 0, 1, 1, 2] 
would indicate that there is only one way to make 0, 2, or 3 units, and 
two ways of making 4 units.

Given such an array, determine the denominations that must be in use. In 
the case above, for example, there must be coins with value 2, 3, and 4.
"""


def find_the_denominations(coins: list[int]) -> set[int]:
    denominations = set()
    for index in range(2, len(coins)):
        if coins[index] > 0:
            denominations.add(index)

            index_j = 1
            while index_j < index:
                if coins[index_j] > 0 and coins[index - index_j] > 0:
                    denominations.add(index_j)
                    denominations.add(index - index_j)

                index_j += 1

    return denominations


if __name__ == "__main__":
    assert find_the_denominations([1, 0, 1, 1, 2]) == {2, 3, 4}
