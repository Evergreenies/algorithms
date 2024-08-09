"""
You are given an array X of floating-point numbers x1, x2, ... xn. These can be rounded up or
down to create a corresponding array Y of integers y1, y2, ... yn.

Write an algorithm that finds an appropriate Y array with the following properties:

The rounded sums of both arrays should be equal.
The absolute pairwise difference between elements is minimized. In other words,
|x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.

For example, suppose your input is [1.3, 2.3, 4.4]. In this case you cannot do better than [1, 2, 5],
which has an absolute difference of |1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1
"""


def rounding_and_min_diff(arr: list) -> list:
    length = len(arr)
    total_sum = sum(arr)
    rounded_sum = int(round(total_sum))

    y = [int(round(num)) for num in arr]
    diff = rounded_sum - sum(y)

    if diff == 0:
        return arr

    indices = sorted(
        range(length), key=lambda index: abs(arr[index] - y[index]), reverse=True
    )

    for index in range(abs(diff)):
        y[indices[index]] += 1 if diff > 0 else -1

    return y


print(rounding_and_min_diff([1.3, 2.3, 4.4]))
print(rounding_and_min_diff([1, 2, 4]))
