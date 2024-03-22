"""
Suppose you are given two lists of n points, one list p1, p2, ..., pn 
on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. 
Imagine a set of n line segments connecting each point pi to qi. Write 
an algorithm to determine how many pairs of the line segments intersect.
"""


def line_segments_intersect(p_arr: list[int], q_arr: list[int]) -> int:
    intersection = 0

    for p_index in range(len(p_arr)):
        for q_index in range(p_index + 1, len(q_arr)):
            diff_p = p_arr[q_index] - p_arr[p_index]
            diff_q = q_arr[q_index] - q_arr[p_index]

            if (diff_p < 0 and diff_q > 0) or (diff_p > 0 and diff_q < 0):
                intersection += 1

    return intersection


if __name__ == "__main__":
    assert line_segments_intersect([], []) == 0
    assert line_segments_intersect([1, 3, 5, 7], [2, 4, 6, 8]) == 0
    assert line_segments_intersect([3, 1], [1, 3]) == 1
    assert (
        line_segments_intersect([0, 10, 7, 4, 12, 9, 2], [3, 5, 11, 6, 1, 13, 8]) == 11
    )
