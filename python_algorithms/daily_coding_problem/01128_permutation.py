"""
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""


def permute(arr: list[int]) -> list[list]:
    if len(arr) <= 1:
        return [arr]

    premutations = []
    for index in range(len(arr)):
        for permutation in permute(arr[:index] + arr[index + 1 :]):
            premutations.append([arr[index]] + permutation)

    return premutations


if __name__ == "__main__":
    assert len(permute([1, 2, 3])) == 6
