"""
Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?
"""


def pascal_triangle(k: int) -> list[int]:
    curr, prev = [1], [1]  # current and previous row

    for _ in range(2, k + 1):
        curr = [1]

        for index in range(1, len(prev)):
            curr.append(prev[index - 1] + prev[index])

        curr.append(1)
        prev = curr

    return curr


assert pascal_triangle(5) == [1, 4, 6, 4, 1]
