"""
Find the pair of elements whose sum is exact k.
"""


def find_paris(arr: list[int], target: int) -> tuple | None:
    if not arr:
        return

    memoize = dict()
    for item in arr:
        diff = target - item
        if memoize.get(diff):
            return item, diff

        memoize[item] = True

    return


print(find_paris([6, 3, 8, 10, 16, 7, 5, 2, 4, 14], 10))
