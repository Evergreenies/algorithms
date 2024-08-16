"""
On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that
have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the
number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered
the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
"""


def count_attacking_pairs(bishops: list[tuple]) -> int:
    left_top_diag1, right_top_diag2 = dict(), dict()
    count = 0

    for row, col in bishops:
        # count pairs in diagonal (top-left to bottom-right)
        left_top_index = row - col
        count += left_top_diag1.get(left_top_index, 0)
        left_top_diag1[left_top_index] = left_top_diag1.get(left_top_index, 0) + 1

        # count pairs in diagonal (top-right to bottom-left)
        right_top_index = row + col
        count += right_top_diag2.get(right_top_index, 0)
        right_top_diag2[right_top_index] = right_top_diag2.get(right_top_index, 0) + 1

    return count


print(count_attacking_pairs([(0, 0), (1, 2), (2, 2), (4, 0)]))
